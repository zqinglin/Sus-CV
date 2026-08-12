#!/usr/bin/env python3
"""取公司 logo -> 矢量 PDF,进素材库。走 Simple Icons(带品牌色) + cairosvg。
用法: python3 fetch_logos.py "抖音=douyin,B站=bilibili,字节=bytedance"
     python3 fetch_logos.py douyin bilibili github wechat bytedance   # 直接给 slug
输出到 ../template/assets/logos/<slug>.pdf 和 ../template/assets/svg/<slug>.svg
slug 见 https://simpleicons.org 。抖音常取不到,用 tiktok 代(同音符 logo)。
依赖: python3 -m venv venv && venv/bin/pip install cairosvg  (需系统 libcairo)
"""
import sys, os, subprocess, urllib.request
HERE = os.path.dirname(os.path.abspath(__file__))
SVG = os.path.join(HERE, "..", "template", "assets", "svg")
PDF = os.path.join(HERE, "..", "template", "assets", "logos")
os.makedirs(SVG, exist_ok=True); os.makedirs(PDF, exist_ok=True)

def slugs_from_args(args):
    out = []
    for a in args:
        for part in a.split(","):
            part = part.strip()
            if not part: continue
            out.append(part.split("=")[-1])   # "抖音=douyin" -> douyin
    return out

def main(args):
    import cairosvg
    for slug in slugs_from_args(args):
        svg = os.path.join(SVG, slug + ".svg")
        try:
            urllib.request.urlretrieve(f"https://cdn.simpleicons.org/{slug}", svg)
            if b"<svg" not in open(svg, "rb").read(40):
                print("MISS", slug); os.remove(svg); continue
            cairosvg.svg2pdf(url=svg, write_to=os.path.join(PDF, slug + ".pdf"))
            print("OK  ", slug)
        except Exception as e:
            print("FAIL", slug, e)
if __name__ == "__main__":
    main(sys.argv[1:])
