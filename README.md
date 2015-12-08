# Overview

This repo holds public documentation for exabyte.io. Currently deployed version is available at [this link](http://docs.exabyte.io:81)

Uses [MkDocs](http://www.mkdocs.org/#getting-started) to convert Markdown files (*.md) in `docs/` directory into static html.

`exabyte_theme` holds a custom styled theme - a derived theme from the default mkdocs one.

# Setup

For quick installation run:

```bash
easy_install pip  # if pip is not installed yet
sudo pip install mkdocs
```

After that inside the repo directory run:

```bash
mkdocs build --clean  # to build new static pages from scratch
mkdocs serve
```

You should have the documentation available at `http://localhost:8000`
