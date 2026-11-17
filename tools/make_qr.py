# -*- coding: utf-8 -*-
"""生成作品集访问二维码。

用法：
    python tools/make_qr.py https://yourname.github.io/portfolio/
    python tools/make_qr.py https://yourname.github.io/portfolio/ --out assets/images/qr.png
"""
import argparse
import os
import sys

import qrcode
from qrcode.constants import ERROR_CORRECT_H

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def build(url: str, out: str) -> str:
    qr = qrcode.QRCode(
        version=None,
        error_correction=ERROR_CORRECT_H,
        box_size=14,
        border=3,
    )
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="#16150f", back_color="#f4f1ea").convert("RGB")

    if not os.path.isabs(out):
        out = os.path.join(ROOT, out)
    os.makedirs(os.path.dirname(out), exist_ok=True)
    img.save(out, "PNG", optimize=True)
    return out


def main() -> int:
    parser = argparse.ArgumentParser(description="生成作品集访问二维码")
    parser.add_argument("url", help="线上访问地址，例如 https://name.github.io/portfolio/")
    parser.add_argument("--out", default="assets/images/qr.png", help="输出文件路径")
    args = parser.parse_args()

    if not args.url.startswith(("http://", "https://")):
        print("请提供完整的 http(s) 地址")
        return 1

    path = build(args.url, args.out)
    print(f"已生成：{path}")
    print(f"内容：{args.url}")
    print("提示：二维码会随内容变化，部署地址确定后重新生成即可。")
    return 0


if __name__ == "__main__":
    sys.exit(main())
