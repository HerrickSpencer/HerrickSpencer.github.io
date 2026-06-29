#!/usr/bin/env python3
"""
create-book-draft.py — Scaffold a new book review draft post.

Fetches metadata and cover from Open Library, creates the draft file,
and saves a 1200x630 banner image. Description and My Notes are left
as TODO placeholders for you (or Copilot) to fill in.

Usage (run from repo root):
  python3 .github/skills/create-book-draft/create-book-draft.py
  python3 .github/skills/create-book-draft/create-book-draft.py "Book Title"
  python3 .github/skills/create-book-draft/create-book-draft.py "Book Title" "Author Name"
"""

import sys
import os
import json
import re
import subprocess
import urllib.request
import urllib.parse
from datetime import date
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]
SKILL_DIR = Path(__file__).resolve().parent
DRAFTS_DIR = REPO_ROOT / "_drafts"
COVERS_DIR = REPO_ROOT / "assets" / "img" / "postMedia" / "bookcovers"
TODAY = date.today().isoformat()


# ── helpers ──────────────────────────────────────────────────────────────────

def slugify(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[''']", "", text)       # drop apostrophes
    text = re.sub(r"[^a-z0-9]+", "-", text) # non-alphanumeric → hyphen
    return text.strip("-")


def fetch_json(url: str) -> dict:
    req = urllib.request.Request(url, headers={"User-Agent": "HerrickSpencer-blog/1.0"})
    with urllib.request.urlopen(req, timeout=10) as resp:
        return json.loads(resp.read())


def download_file(url: str, dest: Path) -> bool:
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "HerrickSpencer-blog/1.0"})
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = resp.read()
        # Reject tiny placeholder images (Open Library returns a 1-byte GIF when no cover exists)
        if len(data) < 5000:
            return False
        dest.write_bytes(data)
        return True
    except Exception:
        return False


# ── Open Library search ───────────────────────────────────────────────────────

def search_books(title: str, author: str = "") -> list[dict]:
    query = title
    if author:
        query += f" {author}"
    encoded = urllib.parse.quote(query)
    url = f"https://openlibrary.org/search.json?q={encoded}&limit=5&fields=key,title,author_name,first_publish_year,isbn,number_of_pages_median,subject,cover_i,cover_edition_key"
    data = fetch_json(url)
    return data.get("docs", [])


def pick_book(results: list[dict]) -> dict | None:
    if not results:
        return None
    print("\nSearch results:")
    for i, book in enumerate(results):
        author = ", ".join(book.get("author_name", ["Unknown"]))
        year = book.get("first_publish_year", "?")
        print(f"  [{i+1}] {book['title']} — {author} ({year})")
    print("  [0] None of these / enter details manually")

    while True:
        choice = input("\nPick a result [1]: ").strip() or "1"
        if choice == "0":
            return None
        if choice.isdigit() and 1 <= int(choice) <= len(results):
            return results[int(choice) - 1]
        print("  Invalid choice, try again.")


def get_pages(book: dict) -> str:
    pages = book.get("number_of_pages_median")
    return str(pages) if pages else "?"


def get_genres(book: dict) -> list[str]:
    """Pick the most useful subjects as tags."""
    subjects = book.get("subject", [])
    # Keep short, clean subjects and normalise to lowercase kebab
    keep = []
    for s in subjects[:30]:
        s = s.lower().strip()
        # Skip overly generic or long subjects
        if len(s) > 40 or s in ("fiction", "nonfiction", "accessible book", "large type books",
                                  "protected daisy", "open library staff picks", "in library"):
            continue
        keep.append(s)
        if len(keep) >= 5:
            break
    return keep


def find_cover(book: dict, slug: str) -> tuple[str | None, str]:
    """Return (local_banner_path, source_url_or_note)."""
    tmp = Path(f"/tmp/bookcover-{slug}.jpg")
    banner = COVERS_DIR / f"{slug}.jpg"

    # Try cover by Open Library cover_i (numeric ID)
    cover_id = book.get("cover_i")
    if cover_id:
        url = f"https://covers.openlibrary.org/b/id/{cover_id}-L.jpg"
        if download_file(url, tmp):
            return str(tmp), url

    # Try by cover_edition_key (OLID)
    olid = book.get("cover_edition_key")
    if olid:
        url = f"https://covers.openlibrary.org/b/olid/{olid}-L.jpg"
        if download_file(url, tmp):
            return str(tmp), url

    # Try by ISBN
    for isbn in (book.get("isbn") or [])[:5]:
        url = f"https://covers.openlibrary.org/b/isbn/{isbn}-L.jpg"
        if download_file(url, tmp):
            return str(tmp), url

    return None, "not found"


def make_banner(input_path: str, output_path: str) -> bool:
    result = subprocess.run(
        [sys.executable, str(SKILL_DIR / "make-banner.py"), input_path, output_path],
        capture_output=True, text=True
    )
    if result.returncode != 0:
        print(f"  ⚠  Banner script error: {result.stderr.strip()}")
        return False
    return True


# ── manual fallback ──────────────────────────────────────────────────────────

def ask(prompt: str, default: str = "") -> str:
    suffix = f" [{default}]" if default else ""
    val = input(f"{prompt}{suffix}: ").strip()
    return val or default


def manual_book_details(title: str, author: str) -> dict:
    print("\nEnter details manually:")
    title  = ask("Full title", title)
    author = ask("Author", author)
    year   = ask("Published year")
    pages  = ask("Pages (approx)")
    fiction = ask("Fiction or nonfiction?", "nonfiction").lower()
    return {"_manual": True, "title": title, "author": author,
            "year": year, "pages": pages, "fiction": fiction}


# ── draft template ───────────────────────────────────────────────────────────

TEMPLATE = """\
---
layout: post
title: "Book: {title}"
categories:
  - Books
tags:
  - books
  - reading
  - {fiction_tag}
{extra_tags}\
stars: 0
image: /assets/img/postMedia/bookcovers/{slug}.jpg
date: {today} 00:00 +0000
date_read: {today}
---

## Overview

**Title:** {title}  
**Author:** {author}  
**Published:** {year}  
**Genre:** {genre}  
**Pages:** ~{pages}  
**Date Read:** {{{{page.date_read}}}}  
**Rating:** {{{{page.stars}}}} / 10

---

## Description

<!-- TODO: Add a 2-3 paragraph summary of the book — what it's about, why it's notable, any context. -->

**Source:** <!-- TODO: Add publisher or Wikipedia link -->

---

## My Notes

*[Your thoughts here — some prompts to get you started:]*

<!-- TODO: Add 4-5 personalized questions specific to this book's themes. Ask Copilot: "Generate My Notes prompts for my book draft @_drafts/book-{slug}.md" -->

---

## Quotes

*[Add any favourite quotes or passages here.]*
"""


# ── main ─────────────────────────────────────────────────────────────────────

def main():
    args = sys.argv[1:]
    input_title  = args[0] if len(args) > 0 else input("Book title: ").strip()
    input_author = args[1] if len(args) > 1 else input("Author (optional, press Enter to skip): ").strip()

    if not input_title:
        print("No title provided. Exiting.")
        sys.exit(1)

    print(f"\nSearching Open Library for: {input_title!r}...")
    try:
        results = search_books(input_title, input_author)
        book = pick_book(results)
    except Exception as e:
        print(f"  ⚠  Search failed ({e}), switching to manual entry.")
        book = None

    if book is None:
        details = manual_book_details(input_title, input_author)
        title  = details["title"]
        author = details["author"]
        year   = details["year"]
        pages  = details["pages"]
        genre  = details.get("fiction", "nonfiction").capitalize()
        fiction_tag = details.get("fiction", "nonfiction")
        extra_tags = []
    else:
        title  = book["title"]
        author = ", ".join(book.get("author_name", ["Unknown"]))
        year   = str(book.get("first_publish_year", "?"))
        pages  = get_pages(book)
        tags   = get_genres(book)
        fiction_tag = "nonfiction"  # default; user can update
        genre  = tags[0].title() if tags else "Nonfiction"
        extra_tags = [t for t in tags[1:] if t not in ("fiction", "nonfiction")][:3]

    slug = slugify(title)
    draft_path = DRAFTS_DIR / f"book-{slug}.md"
    banner_path = COVERS_DIR / f"{slug}.jpg"

    # ── cover image ──
    COVERS_DIR.mkdir(parents=True, exist_ok=True)
    image_note = ""
    if book and not book.get("_manual"):
        print("\nLooking for cover image...")
        tmp_path, source = find_cover(book, slug)
        if tmp_path:
            print(f"  ✓  Downloaded cover from {source}")
            if make_banner(tmp_path, str(banner_path)):
                print(f"  ✓  Banner saved → {banner_path.relative_to(REPO_ROOT)}")
                image_note = "✓ Banner image saved."
            else:
                image_note = f"⚠  Banner script failed. Cover downloaded to {tmp_path} — resize manually."
        else:
            print("  ⚠  No cover found on Open Library.")
            image_note = f"⚠  No cover found. Add one manually to assets/img/postMedia/bookcovers/{slug}.jpg"
    else:
        image_note = f"⚠  No cover fetched. Add one manually to assets/img/postMedia/bookcovers/{slug}.jpg"

    # ── draft file ──
    DRAFTS_DIR.mkdir(exist_ok=True)
    if draft_path.exists():
        overwrite = input(f"\n{draft_path.name} already exists. Overwrite? [y/N]: ").strip().lower()
        if overwrite != "y":
            print("Skipped.")
            sys.exit(0)

    extra_tag_lines = "".join(f"  - {t}\n" for t in extra_tags)
    content = TEMPLATE.format(
        title=title, slug=slug, author=author, year=year,
        pages=pages, genre=genre, fiction_tag=fiction_tag,
        extra_tags=extra_tag_lines, today=TODAY,
    )
    draft_path.write_text(content)

    print(f"\n✓  Draft created → {draft_path.relative_to(REPO_ROOT)}")
    print(f"   {image_note}")
    print(f"\nNext steps:")
    print(f"  1. Fill in the Description and My Notes sections (or ask Copilot to do it)")
    print(f"  2. Set 'stars' (1–10) and update 'date_read' after finishing the book")
    print(f"  3. Move to _posts/YYYY-MM-DD-book-{slug}.md when ready to publish")


if __name__ == "__main__":
    main()
