# Contributing

## Prerequisites

You need **Ruby** installed with the MSYS2 devkit (required for compiling native gem extensions on Windows).

### Install Ruby (Windows)

```powershell
winget install RubyInstallerTeam.RubyWithDevKit.3.3
```

After installation, **restart your terminal** so the PATH updates take effect.

### Install Dependencies

From the repository root, install Bundler and the project gems:

```powershell
gem install bundler
bundle install
```

## Running the Site Locally

```powershell
bundle exec jekyll serve --drafts --livereload
```

This will:

- **`--drafts`** — Include posts from the `_drafts/` folder
- **`--livereload`** — Automatically refresh the browser when files change

The site will be available at **http://localhost:4000**.

Alternatively, you can use the VS Code task from the Command Palette: **Tasks: Run Task** → **jekyll** (this runs with `--drafts --incremental` instead of `--livereload`).

## Writing Posts

- Published posts go in `_posts/` with the naming convention `YYYY-MM-DD-title.md`.
- Work-in-progress posts go in `_drafts/` (no date prefix needed).

## Project Structure

| Path | Description |
|------|-------------|
| `_posts/` | Published blog posts |
| `_drafts/` | Draft posts (visible locally with `--drafts`) |
| `_config.yml` | Site configuration |
| `_layouts/` | Page layout templates |
| `_includes/` | Reusable template partials |
| `_tabs/` | Top-level navigation pages |
| `_data/` | Site data files (authors, contact, etc.) |
| `assets/` | Images, CSS, and other static files |
| `Docs/` | Project documentation |
