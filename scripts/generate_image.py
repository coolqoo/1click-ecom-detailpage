#!/usr/bin/env python3
"""使用 OpenAI 兼容图片接口生成图片。

配置来自环境变量或项目根目录 `.env`：
- IMG_BASE_URL: API 根地址，例如 https://api.openai.com/v1
- IMG_MODEL: 图片模型名，例如 gpt-image-1.5
- IMG_API_KEY: 使用者自己的 API key
"""

from __future__ import annotations

import argparse
import base64
import binascii
import http.client
import json
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any


ENV_BASE_URL = "IMG_BASE_URL"
ENV_MODEL = "IMG_MODEL"
ENV_API_KEY = "IMG_API_KEY"
ENV_ALIASES = {
    ENV_BASE_URL: ("OPENAI_BASE_URL", "OPENAI_API_BASE", "BASE_URL"),
    ENV_MODEL: ("OPENAI_IMAGE_MODEL", "IMAGE_MODEL", "OPENAI_MODEL"),
    ENV_API_KEY: ("OPENAI_API_KEY", "API_KEY"),
}


def fail(message: str, exit_code: int = 1) -> None:
    print(f"错误：{message}", file=sys.stderr)
    raise SystemExit(exit_code)


def read_prompt(args: argparse.Namespace) -> str:
    if args.prompt:
        prompt = args.prompt.strip()
    else:
        try:
            prompt = Path(args.prompt_file).read_text(encoding="utf-8").strip()
        except OSError as exc:
            fail(f"无法读取 prompt 文件：{exc}")

    if not prompt:
        fail("prompt 不能为空。")
    return prompt


def strip_env_value(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
        return value[1:-1]
    return value


def find_default_env_file() -> Path | None:
    for directory in (Path.cwd(), *Path.cwd().parents):
        env_file = directory / ".env"
        if env_file.is_file():
            return env_file
    return None


def load_env_file(env_file: Path | None) -> None:
    if env_file is None:
        return
    try:
        lines = env_file.read_text(encoding="utf-8").splitlines()
    except OSError as exc:
        fail(f"无法读取 .env 文件：{exc}")

    for line_number, raw_line in enumerate(lines, start=1):
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        if line.startswith("export "):
            line = line[len("export ") :].strip()
        if "=" not in line:
            fail(f".env 第 {line_number} 行格式不正确，应为 KEY=value。")
        key, value = line.split("=", 1)
        key = key.strip()
        if not key:
            fail(f".env 第 {line_number} 行缺少变量名。")
        if key not in os.environ:
            os.environ[key] = strip_env_value(value)


def require_config(name: str) -> str:
    candidates = (name, *ENV_ALIASES.get(name, ()))
    for candidate in candidates:
        value = os.environ.get(candidate, "").strip()
        if value:
            return value

    accepted = "、".join(candidates)
    if not value:
        fail(
            f"缺少配置 {name}。请在 .env 中设置 IMG_BASE_URL、IMG_MODEL、IMG_API_KEY；"
            f"也兼容这些变量名：{accepted}。"
        )
    return value


def build_payload(args: argparse.Namespace, prompt: str, model: str) -> dict[str, Any]:
    payload: dict[str, Any] = {
        "model": model,
        "prompt": prompt,
        "n": args.n,
        "size": args.size,
    }
    if args.quality:
        payload["quality"] = args.quality
    if args.format:
        # OpenAI 兼容服务通常使用 output_format 控制返回图片格式。
        payload["output_format"] = args.format
    return payload


def post_json(url: str, api_key: str, payload: dict[str, Any]) -> dict[str, Any]:
    body = json.dumps(payload).encode("utf-8")
    request = urllib.request.Request(
        url,
        data=body,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        method="POST",
    )

    try:
        with urllib.request.urlopen(request, timeout=120) as response:
            raw = response.read().decode("utf-8")
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")
        fail(f"图片接口返回 HTTP {exc.code}：{detail}")
    except urllib.error.URLError as exc:
        fail(f"无法连接图片接口：{exc.reason}")
    except http.client.RemoteDisconnected:
        fail("图片接口远端断开连接，请稍后重试。")
    except TimeoutError:
        fail("图片接口请求超时。")

    try:
        parsed = json.loads(raw)
    except json.JSONDecodeError:
        fail(f"图片接口返回的不是有效 JSON：{raw[:500]}")

    if not isinstance(parsed, dict):
        fail("图片接口返回格式不正确：顶层结果不是对象。")
    return parsed


def filename_for(index: int, suffix: str) -> str:
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    return f"image-{timestamp}-{index + 1:02d}.{suffix.lstrip('.')}"


def suffix_from_url(url: str, fallback: str) -> str:
    path = urllib.parse.urlparse(url).path
    suffix = Path(path).suffix.lower().lstrip(".")
    if suffix in {"png", "jpg", "jpeg", "webp"}:
        return "jpg" if suffix == "jpeg" else suffix
    return fallback


def save_b64_image(item: dict[str, Any], output_dir: Path, index: int, fmt: str) -> Path:
    encoded = item.get("b64_json")
    if not isinstance(encoded, str) or not encoded:
        fail("图片结果缺少 b64_json。")

    try:
        image_bytes = base64.b64decode(encoded)
    except (binascii.Error, ValueError) as exc:
        fail(f"无法解码 b64_json 图片：{exc}")

    output_path = output_dir / filename_for(index, fmt)
    try:
        output_path.write_bytes(image_bytes)
    except OSError as exc:
        fail(f"无法写入图片文件：{exc}")
    return output_path


def save_url_image(item: dict[str, Any], output_dir: Path, index: int, fmt: str) -> Path:
    image_url = item.get("url")
    if not isinstance(image_url, str) or not image_url:
        fail("图片结果缺少 url。")

    suffix = suffix_from_url(image_url, fmt)
    output_path = output_dir / filename_for(index, suffix)

    try:
        with urllib.request.urlopen(image_url, timeout=120) as response:
            image_bytes = response.read()
    except urllib.error.URLError as exc:
        fail(f"无法下载图片 URL：{exc.reason}")
    except TimeoutError:
        fail("下载图片超时。")

    try:
        output_path.write_bytes(image_bytes)
    except OSError as exc:
        fail(f"无法写入图片文件：{exc}")

    return output_path


def save_images(result: dict[str, Any], output_dir: Path, fmt: str) -> list[Path]:
    data = result.get("data")
    if not isinstance(data, list) or not data:
        fail("图片接口返回中没有 data 图片数组。")

    output_dir.mkdir(parents=True, exist_ok=True)
    paths: list[Path] = []
    for index, item in enumerate(data):
        if not isinstance(item, dict):
            fail("图片接口返回格式不正确：data 中包含非对象项目。")
        if item.get("b64_json"):
            paths.append(save_b64_image(item, output_dir, index, fmt))
        elif item.get("url"):
            paths.append(save_url_image(item, output_dir, index, fmt))
        else:
            fail("图片结果既没有 b64_json，也没有 url。")
    return paths


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="使用 IMG_* 环境变量调用 OpenAI 兼容图片接口生成图片。"
    )
    prompt_group = parser.add_mutually_exclusive_group(required=True)
    prompt_group.add_argument("--prompt", help="直接传入图片生成 Prompt。")
    prompt_group.add_argument("--prompt-file", help="从文本文件读取图片生成 Prompt。")
    parser.add_argument(
        "--output-dir",
        default="generated-images",
        help="图片输出目录，默认 generated-images。",
    )
    parser.add_argument(
        "--env-file",
        help="指定 .env 配置文件；不指定时从当前目录向上查找 .env。",
    )
    parser.add_argument("--size", default="1024x1024", help="图片尺寸，默认 1024x1024。")
    parser.add_argument("--quality", help="图片质量参数，例如 low、medium、high。")
    parser.add_argument(
        "--format",
        choices=("png", "jpeg", "webp"),
        default="png",
        help="期望图片格式，默认 png。",
    )
    parser.add_argument(
        "--n",
        type=int,
        default=1,
        help="生成图片数量，默认 1。",
    )
    args = parser.parse_args()
    if args.n < 1:
        fail("--n 必须大于等于 1。")
    return args


def main() -> None:
    args = parse_args()
    env_file = Path(args.env_file) if args.env_file else find_default_env_file()
    load_env_file(env_file)
    prompt = read_prompt(args)
    base_url = require_config(ENV_BASE_URL).rstrip("/")
    model = require_config(ENV_MODEL)
    api_key = require_config(ENV_API_KEY)

    payload = build_payload(args, prompt, model)
    endpoint = f"{base_url}/images/generations"
    result = post_json(endpoint, api_key, payload)
    paths = save_images(result, Path(args.output_dir), args.format)

    print("生成完成：")
    for path in paths:
        print(path)


if __name__ == "__main__":
    main()
