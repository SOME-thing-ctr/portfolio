# -*- coding: utf-8 -*-
"""压缩项目图片资源并复制视频（源文件不做修改）。"""
import os
import shutil
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.dirname(ROOT)
IMG_OUT = os.path.join(ROOT, "assets", "images")
VID_OUT = os.path.join(ROOT, "assets", "videos")
os.makedirs(IMG_OUT, exist_ok=True)
os.makedirs(VID_OUT, exist_ok=True)


def save_jpg(src, dst, max_width, quality):
    im = Image.open(src)
    if im.mode in ("RGBA", "LA", "P"):
        im = im.convert("RGBA")
        bg = Image.new("RGB", im.size, (12, 12, 12))
        bg.paste(im, mask=im.split()[-1])
        im = bg
    else:
        im = im.convert("RGB")
    if im.width > max_width:
        h = round(im.height * max_width / im.width)
        im = im.resize((max_width, h), Image.LANCZOS)
    im.save(dst, "JPEG", quality=quality, optimize=True, progressive=True)
    print(f"{os.path.basename(dst):28s} {im.size[0]}x{im.size[1]}  {os.path.getsize(dst)/1024:.0f} KB")


save_jpg(os.path.join(SRC, "封面.jpg"), os.path.join(IMG_OUT, "badge-cover.jpg"), 1400, 86)
save_jpg(os.path.join(SRC, "海报666.jpg"), os.path.join(IMG_OUT, "art-therapy.jpg"), 1400, 82)
save_jpg(os.path.join(SRC, "TD", "1.png"), os.path.join(IMG_OUT, "td-mandala.jpg"), 1200, 88)
save_jpg(os.path.join(SRC, "f3e6cc135fba8653e145cd92d80f2ec5.jpg"), os.path.join(IMG_OUT, "portrait.jpg"), 900, 86)

videos = [
    ("游园惊梦.mp4", "youyuan-jingmeng.mp4"),
    ("效果演示.mp4", "demo.mp4"),
    (os.path.join("TD", "1.mp4"), "td-mandala.mp4"),
    (os.path.join("TD", "2.mp4"), "particles-flow.mp4"),
    (os.path.join("TD", "3.mp4"), "particles-glow.mp4"),
]
for src_name, dst_name in videos:
    src = os.path.join(SRC, src_name)
    dst = os.path.join(VID_OUT, dst_name)
    if os.path.exists(src):
        shutil.copy2(src, dst)
        print(f"{dst_name:28s} {os.path.getsize(dst)/1024/1024:.1f} MB")
    else:
        print("missing:", src)
