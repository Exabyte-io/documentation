

# Overview

This repo holds public documentation for exabyte.io. Currently deployed version is available at [this link](http://docs.exabyte.io) (you will need to be logged in at platform.exabyte.io to try).

Uses [MkDocs](http://www.mkdocs.org/#getting-started) to convert Markdown files (*.md) in `docs/` directory into static html.

`exabyte_theme` holds a custom styled theme - a derived theme from the default mkdocs one.

> NOTE: tested and developed with mkdocs version 0.16.2.

# Setup

For quick installation run:

```bash
easy_install pip  # if pip is not installed yet
virtualenv .virtualenv
source ./virtualenv/bin/activate
pip install -r requirements.txt
```

In order to download images:

```
sh ./scripts/download_images.sh
```

After that inside the repo directory run, after sourcing virtual environment:

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

Do NOT push images to this repository.

> **NOTE**: files named with verbs (eg. create-organization.md) are meant to contain step-by-step tutorials with visuals, files named with nouns (eg. advanced-characteristics.md) are meant to contain 'static' and more in-depth explanation of the terms with minimum visuals.

# Examples elements

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
    ALGO = Normal<br>
    EDIFF = 0.0001
    ...
    ```
</details>


# Basic guidelines

1. Leave comment at the top about the original author (TB = Timur Bazhirov):
    ```
    <!-- by TB -->
    ```

2. Do not duplicate the name of the page at the top, it will already be inside breadcrumbs, better add a short 1-paragraph description of the contents

3. Leave a newline after the heading elements:
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

5. Including an external link:
    ```
    [zmdi-plus-circle](http://zavoloklom.github.io/material-design-iconic-font/cheatsheet.html)
    ```

6. Including a local link to a page or a place within a page:
    ```
    [subscription level](/billing/accounts-and-billing)
    ```

    ```
    [subscription level](/billing/accounts-and-billing#pricing)
    ```

7. Including an image/screenshot:
    ```
    ![Simulation Diagram](/images/simulation-job-wokflow-unit-explained.png "Simulation Diagram")
    ```

8. Including a gif image
    ```
    <img data-gifffer="/images/AddCredit.gif" />
    ```

    we use a third-party plugin, embedded into the source of this repository ("giffer") in order to make gif images clickable like videos.
