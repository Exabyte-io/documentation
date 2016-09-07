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

# Example elements

There are multiple [admonition](https://pythonhosted.org/Markdown/extensions/admonition.html) classes: tip (green), warning (orange), error (red), note (blue):

```txt
!!! tip "Unused credits"
    All unused credits automatically roll over into the next validity period.
```

is rendered into:

<div class="tip">
    <p class="first admonition-title">Unused credits</p>
    <p class="last">All unused credits automatically roll over into the next validity period.</p>
</div>

Expandable section can be added using:

```
<details>
    <summary>**INCAR**</summary>
    ```
    ALGO = Normal
    EDIFF = 0.0001
    ...
    ```
</details>
```

is rendered into:

<details>
    <summary>**INCAR**</summary>
    ```
    ALGO = Normal
    EDIFF = 0.0001
    ...
    ```
</details>

# Basic guidelines

1. Leave comment at the top about the original author:
    ```
    <!-- by MH -->
    ```

2. Do not duplicate the name of the page at the top, it will already be inside breadcrumbs, better add a short 1-paragraph description of the contents

3. Leave a newline after heading elements:
    ```
    ## Create a new job

    You can create a new job by clicking on the ...
    ```

4. Use [zmdi](http://zavoloklom.github.io/material-design-iconic-font/cheatsheet.html) icons instead of saying "click" on the button with 3 stripes:

    ```
    <i class="zmdi zmdi-plus-circle"></i>
    ```

    will be rendered as: a [zmdi-plus-circle](http://zavoloklom.github.io/material-design-iconic-font/cheatsheet.html) icon

    We use the same icon set for the main application.

5. Including an external link
6. Including a local link
7. Including a screenshot
8. Including a gif
