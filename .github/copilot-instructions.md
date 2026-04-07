# Copilot Instructions

## Project Overview

This is a Jekyll blog using the **Chirpy theme** (v7.4+ gem: `jekyll-theme-chirpy`), deployed to GitHub Pages at [HerrickSpencer.github.io](https://HerrickSpencer.github.io). The site covers tech/dev, DIY/woodworking, electronics, tips of the week, book reviews, and personal life.

## Build & Serve

```powershell
# Install dependencies
gem install bundler && bundle install

# Serve locally with drafts and live reload
bundle exec jekyll serve --drafts --livereload
# Site at http://localhost:4000

# Build for production
bundle exec jekyll b -d "_site"

# Validate HTML (used in CI)
bundle exec htmlproofer _site --disable-external --ignore-urls "/^http:\/\/127.0.0.1/,/^http:\/\/0.0.0.0/,/^http:\/\/localhost/"
```

There is also a VS Code task (`jekyll`) that runs `bundle exec jekyll serve --drafts --incremental`.

## Architecture

### Content Flow

- **Published posts** → `_posts/` with naming `YYYY-MM-DD-title.md`
- **Drafts** → `_drafts/` (no date prefix needed). Visible locally with `--drafts` flag.
- **Navigation tabs** → `_tabs/` (about, archives, books, career, categories, tags). Each has an `order` field controlling nav position.

### Custom Layouts (override Chirpy defaults)

- `_layouts/home.html` — Filters out posts in the `Cancer` category from the home page listing. Posts with `hidden: true` are also excluded. Uses Jekyll's paginator (only works on `index.html`).
- `_layouts/books.html` — Shows only posts with `categories: Books`. Uses **client-side JS pagination** with URL hash (`#page=N`) because `jekyll-paginate` only works on `index.html`.
- `_layouts/WPArchive.html` — Wraps old WordPress-migrated posts with a disclaimer note.

### Plugins

- `_plugins/posts-lastmod-hook.rb` — Automatically sets `last_modified_at` on posts from git history.

### Post Images

Post media goes in `assets/img/postMedia/`. The `postMedia` config value in `_config.yml` sets the base path. Book cover images go in `assets/img/postMedia/bookcovers/`.

## Post Conventions

### Front Matter

All posts use `layout: post`. Common fields:

```yaml
---
layout: post
title: 'Post Title'
categories:
- CategoryName
tags:
- tag1
- tag2
image: /assets/img/postMedia/subfolder/image.jpg
date: YYYY-MM-DD HH:MM +/-TZOFFSET
---
```

### Book Review Posts

Book reviews have additional front matter:

```yaml
---
categories:
- Books
tags:
- books
- reading
- fiction       # or nonfiction
author: herrick
stars: 8        # Rating out of 10, displayed on the books page
image: /assets/img/postMedia/bookcovers/book-name.jpg
---
```

Book reviews follow a structure starting with `## Overview` containing title, author, published date, genre, pages, and stars, followed by review sections. Draft book reviews live in `_drafts/` with filenames like `book-title-slug.md`.

### Category Conventions

Key categories in use: `Programming`, `Technology`, `DIY`, `Tips of the Week`, `Books`, `Life`, `Cancer`. The `Cancer` category is specifically filtered out of the home page.

### Tips of the Week

Prefixed with `ToW:` in the title (e.g., `"ToW: Quick QR Codes"`). Category: `Tips of the Week`.

## Global Defaults in `_config.yml`

All posts have these defaults (no need to repeat in front matter):
- `layout: post`
- `comments: true` (utterances, backed by GitHub Issues)
- `toc: true`
- `math: true` (MathJax 3.2.2 — can use LaTeX math in any post)

Drafts have `comments: false` by default.

## Post Templates

Front Matter CMS templates exist in `.frontmatter/templates/` for three post types: `diy-project.md`, `tech-post.md`, and `tip-of-the-week.md`. A VS Code snippet `draftfront` also scaffolds post front matter.

## CI/CD

GitHub Actions workflow (`.github/workflows/pages-deploy.yml`):
1. Builds with `bundle exec jekyll b` (Ruby 3.3)
2. Validates with `htmlproofer` (internal links only)
3. Deploys to GitHub Pages (main branch only)

The workflow also runs on a weekly schedule (Wednesdays at 07:00 UTC).
