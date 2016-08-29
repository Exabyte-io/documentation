# Overview

This repo holds public documentation for exabyte.io. Currently deployed version is available at [this link](http://docs.exabyte.io) (you will need to be logged in at platform.exabyte.io to try).

Uses [MkDocs](http://www.mkdocs.org/#getting-started) to convert Markdown files (*.md) in `docs/` directory into static html.

`exabyte_theme` holds a custom styled theme - a derived theme from the default mkdocs one.

# Setup

For quick installation run:

```bash
easy_install pip  # if pip is not installed yet
sudo pip install https://github.com/mkdocs/mkdocs/archive/master.zip
```

After that inside the repo directory run:

```bash
mkdocs build --clean  # to build new static pages from scratch
mkdocs serve
```

You should have the documentation available at `http://localhost:8000`

# Important

In order to make it easier to merge ongoing updates from mkdocs, do not change the content of:

    ./exabyte_theme/*

except for extra.css/extra.js files.
