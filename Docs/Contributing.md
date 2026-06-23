# Contributing

## Prerequisites

You need **Ruby 3.3+** installed. Choose the appropriate section below for your operating system.

### Install Ruby (Windows)

```powershell
winget install RubyInstallerTeam.RubyWithDevKit.3.3
```

After installation, **restart your terminal** so the PATH updates take effect.

### Install Ruby (Ubuntu Linux)

Use `apt` to install Ruby and the build tools needed for compiling native gem extensions:

```bash
sudo apt update
sudo apt install ruby-full build-essential zlib1g-dev
```

Verify the installation:

```bash
ruby --version
gem --version
```

**Optional:** If you prefer to manage multiple Ruby versions, consider using [asdf](https://asdf-vm.com/):

```bash
# Install asdf
git clone https://github.com/asdf-vm/asdf.git ~/.asdf
cd ~/.asdf && git checkout $(git describe --abbrev=0 --tags)

# Add asdf to your shell (add to ~/.bashrc or ~/.zshrc)
. "$HOME/.asdf/asdf.sh"
. "$HOME/.asdf/asdf.sh.bash"

# Install the Ruby plugin
asdf plugin add ruby

# Install Ruby 3.3
asdf install ruby 3.3.0
asdf global ruby 3.3.0
```

### Install Dependencies

From the repository root, install Bundler and the project gems:

**Windows:**
```powershell
gem install bundler
bundle install
```

**Linux:**
```bash
gem install bundler
bundle install
```

## Running the Site Locally

### Using the Command Line

**Windows:**
```powershell
bundle exec jekyll serve --drafts --livereload
```

**Linux:**
```bash
bundle exec jekyll serve --drafts --livereload
```

This will:

- **`--drafts`** — Include posts from the `_drafts/` folder
- **`--livereload`** — Automatically refresh the browser when files change

The site will be available at **http://localhost:4000**.

### Using VS Code Task

Alternatively, you can use the VS Code task from the Command Palette:

1. Press **Ctrl+Shift+P** (or **Cmd+Shift+P** on macOS)
2. Type **Tasks: Run Task**
3. Select **jekyll**

This runs with `--drafts --incremental` for faster incremental builds.

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
