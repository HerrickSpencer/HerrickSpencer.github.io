---
name: create-book-draft
description: Creates a new book review draft post for the HerrickSpencer blog, including downloading and resizing the book cover image. Use this skill when asked to create a book draft, add a book, or start a book review post.
allowed-tools: shell
---

# Create Book Draft Post

When asked to create a book draft post, follow these steps:

## 1. Gather Book Information

If the user hasn't provided a book title, ask for one. Then research the book to find:
- Full title
- Author name(s)
- Publication year
- Genre (be specific, e.g. "Memoir / Narrative nonfiction", "Literary fiction", "Science fiction")
- Approximate page count
- A 2–3 paragraph description/summary of the book (what it's about, why it's notable)
- Any noteworthy context (awards, controversies, cultural significance)

Use web search tools if available to find accurate details.

## 2. Determine Metadata

- **Slug**: Create a kebab-case filename slug from the title (e.g. "The Midnight Library" → `midnight-library`). Prefix the filename with `book-` (e.g. `book-midnight-library.md`).
- **Tags**: Include `books` and `reading` always. Add `fiction` or `nonfiction` as appropriate. Add 1–3 more tags relevant to genre or topic (e.g. `memoir`, `tech`, `history`, `sci-fi`, `politics`, `biography`).
- **Stars**: Leave as a placeholder `0` — the user will fill this in after reading.
- **Date**: Use today's date as the `date` and `date_read` fields (YYYY-MM-DD format). The user can update after reading.
- **Image path**: Use `/assets/img/postMedia/bookcovers/[slug].jpg` where `[slug]` matches the filename slug.

## 3. Generate Thoughtful Prompt Questions

In the **My Notes** section, generate 4–5 personalized prompt questions tailored to the specific book's themes, the author's perspective, or content that would resonate with a tech professional and lifelong learner. Make them specific to this book — not generic.

## 4. Find and Save the Book Cover Banner Image

The blog uses **1200×630 JPEG** banners. A `make-banner.py` script is included in this skill's directory to handle resizing.

Steps:
1. **Find the cover image URL.** Look for a high-quality cover image (at least 400px wide) from one of these sources (in order of preference):
   - Open Library: `https://covers.openlibrary.org/b/isbn/[ISBN]-L.jpg`
   - The publisher's website
   - A book database like Google Books or Goodreads
   - Use a web search for "[Book Title] [Author] book cover high resolution"

2. **Download the image** to a temp file:
   ```bash
   curl -L -o /tmp/bookcover-[slug].jpg "[IMAGE_URL]"
   ```

3. **Run `make-banner.py`** from this skill's base directory to resize to 1200×630:
   ```bash
   python3 [SKILL_DIR]/make-banner.py /tmp/bookcover-[slug].jpg assets/img/postMedia/bookcovers/[slug].jpg
   ```
   The script centers the cover on a padded canvas sampled from the cover's edge colors, matching the style of existing book banners. It auto-installs Pillow if needed.

4. **Verify** the output file exists and looks correct.

If image download fails (e.g. 404 or redirect to a placeholder), try alternative sources. If no good image can be found, skip and tell the user — they can add it manually later.

## 5. Create the Draft File

Create the file at `_drafts/book-[slug].md` using this exact template:

```markdown
---
layout: post
title: "Book: [Full Title]"
categories:
  - Books
tags:
  - books
  - reading
  - [fiction OR nonfiction]
  - [additional tags]
author: herrick
stars: 0
image: /assets/img/postMedia/bookcovers/[slug].jpg
date: [YYYY-MM-DD] 00:00 +0000
date_read: [YYYY-MM-DD]
---

## Overview

**Title:** [Full Title]  
**Author:** [Author Name]  
**Published:** [Year]  
**Genre:** [Genre]  
**Pages:** ~[Pages]  
**Date Read:** {{page.date_read}}  
**Rating:** {{page.stars}} / 10

---

## Description

[2–3 paragraph description of the book — what it's about, notable context, why it matters]

**Source:** [Link to publisher or Wikipedia page for the book] | [Second source if available]

---

## My Notes

*[Your thoughts here — some prompts to get you started:]*

- [Personalized question 1]
- [Personalized question 2]
- [Personalized question 3]
- [Personalized question 4]
- [Personalized question 5]

---

## Quotes

*[Add any favourite quotes or passages here.]*
```

## 6. Confirm Creation

After creating the file, tell the user:
- The path to the new draft file
- Whether the book cover banner was saved successfully, or if they need to add one manually to `/assets/img/postMedia/bookcovers/[slug].jpg`
- That they should update `stars` (1–10) and `date_read` after finishing the book
