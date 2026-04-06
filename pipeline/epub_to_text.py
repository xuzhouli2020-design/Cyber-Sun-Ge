#!/usr/bin/env python3
"""Extract text from epub files into clean chapter-based text files."""

import sys
import os
import re
import ebooklib
from ebooklib import epub
from bs4 import BeautifulSoup

def epub_to_chapters(epub_path, output_dir):
    """Extract all chapters from an epub into individual text files + a combined file."""
    book = epub.read_epub(epub_path)

    os.makedirs(output_dir, exist_ok=True)

    all_text = []
    chapter_num = 0

    for item in book.get_items():
        if item.get_type() == ebooklib.ITEM_DOCUMENT:
            soup = BeautifulSoup(item.get_content(), 'html.parser')
            text = soup.get_text(separator='\n')

            # Clean up
            lines = [line.strip() for line in text.split('\n')]
            lines = [line for line in lines if line]  # remove empty lines
            text = '\n'.join(lines)

            if len(text.strip()) < 50:  # skip near-empty chapters (covers, etc.)
                continue

            chapter_num += 1
            chapter_file = os.path.join(output_dir, f"chapter_{chapter_num:02d}.txt")
            with open(chapter_file, 'w', encoding='utf-8') as f:
                f.write(text)

            all_text.append(f"=== 第{chapter_num}部分 ===\n\n{text}")
            print(f"Chapter {chapter_num}: {len(text)} chars - {lines[0][:60] if lines else '(empty)'}...")

    # Write combined file
    combined_file = os.path.join(output_dir, "full_text.txt")
    with open(combined_file, 'w', encoding='utf-8') as f:
        f.write('\n\n'.join(all_text))

    total_chars = sum(len(t) for t in all_text)
    print(f"\nDone: {chapter_num} chapters, {total_chars} total characters")
    print(f"Combined file: {combined_file}")
    return combined_file

if __name__ == '__main__':
    epub_path = sys.argv[1] if len(sys.argv) > 1 else None
    output_dir = sys.argv[2] if len(sys.argv) > 2 else None

    if not epub_path:
        print("Usage: python3 epub_to_text.py <epub_file> [output_dir]")
        sys.exit(1)

    if not output_dir:
        output_dir = os.path.splitext(epub_path)[0] + "_text"

    epub_to_chapters(epub_path, output_dir)
