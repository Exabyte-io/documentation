# Overview

This repo holds public documentation for exabyte.io. Currently deployed version is available at [this link](http://docs.exabyte.io) (you will need to be logged in at platform.exabyte.io to try).

Uses [MkDocs](http://www.mkdocs.org/#getting-started) to convert Markdown files (*.md) in `docs/` directory into static html.

`exabyte_theme` holds a custom styled theme - a derived theme from the default mkdocs one.

# Setup

For quick installation run:

```bash
easy_install pip  # if pip is not installed yet
sudo pip install https://github.com/mkdocs/mkdocs/archive/master.zip
sh ./scripts/download_images.sh
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

# Development

Images (screenshots) are kept separately at http://files.exabyte.io:18/uploads/images/ and synchronized into `./docs/images` folder through running:

```bash
sh ./scripts/download_images.sh
```

or

```bash
sh ./scripts/upload_images.sh
```

Do not push images to this repository.

> **NOTE**: files named with verbs (eg. create-organization.md) are meant to contain step-by-step tutorials with visuals, files named with nouns (eg. advanced-characteristics.md) are meant to contain 'static' and more in-depth explanation of the terms with minimum visuals.
