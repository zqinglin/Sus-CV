#!/usr/bin/env python3
"""抽取简历文本供改造。docx 用 python-docx;PDF 建议直接用多模态 Read 看版式。
用法: python3 extract_resume.py 简历.docx
"""
import sys
def main(path):
    if path.lower().endswith(".docx"):
        from docx import Document           # pip install python-docx
        d = Document(path)
        for i, p in enumerate(d.paragraphs):
            t = p.text.strip()
            if t:
                print(f"[{i}] {t}")
    elif path.lower().endswith(".txt"):
        print(open(path, encoding="utf-8").read())
    else:
        print("PDF/图片: 请用多模态 Read 工具直接查看版式与内容(能看到配色/logo/布局),"
              "文本抽取会丢版式。", file=sys.stderr)
if __name__ == "__main__":
    main(sys.argv[1])
