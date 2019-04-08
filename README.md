# Exabyte public documentation

This repo holds public documentation for exabyte.io. Currently deployed version is available at [this link](http://docs.exabyte.io) (you will need to be logged in at platform.exabyte.io to try).

Uses [MkDocs](http://www.mkdocs.org/#getting-started) to convert Markdown files (*.md) in `docs/` directory into static html.

[Mkdocs-material](https://squidfunk.github.io/mkdocs-material/) theme is used, with additional css added in extra files.

> NOTE: tested and developed with mkdocs version 1.0.4. See "requirements.txt" for more info.

## Setup

For quick installation:

1. Install dependencies: python 2.7, `pip`, [`virtualenv`](https://virtualenv.pypa.io/en/latest/installation/), git, [git-lfs](https://git-lfs.github.com/).

2. Clone this repository: 

    ```bash
    git clone git@github.com:Exabyte-io/exabyte-public-documentation.git
    ```

3. Setup virtual environment

    ```bash
    cd exabyte-public-documentation
    virtualenv .virtualenv
    source .virtualenv/bin/activate
    pip install -r requirements.txt
    ```

4. Init git submodules:

    ```bash
    git submodule update --init
    ```

5. Download images:

    ```bash
    sh ./scripts/download_images.sh
    ```

6. Start mkdocs server (after sourcing virtual environment):

    ```bash
    mkdocs serve
    ```

You should have the documentation up and running at `http://localhost:8000`

## Development

### Including Images

Do NOT push images to this repository with git. 

(Some) Images (screenshots) are kept separately at http://files.exabyte.io:18/uploads/images/ and synchronized into `./docs/images` folder through running:

```bash
sh ./scripts/download_images.sh
```

or

```bash
sh ./scripts/upload_images.sh
```

Some images are included with git-lfs. This is an acceptable way to contribute images, as long as the size is kept small (below 1Mb each) in order to avoid exceeding Github LFS quota.

### Adjusting styles and sources

The default [mkdocs-material](https://squidfunk.github.io/mkdocs-material/) theme is extended, with additional css and javascript inside [docs/extra](docs/extra/) folder. Any new files shall go into the same folder and shall be added to the corresponding section of [mkdocs.yml](mkdocs.yml).


## Notes on Object-Oriented Design 

We embrace Object Oriented Design (OOD) principles when structuring the documentation. The rationale for adhering to the above OOP principles is mainly to avoid unnecessary repetitions of the same explanations in multiple different places, and thus to make the documentation easily expandable or modifiable in the future when new features will be added/changed.

### OOD Principles

- **Encapsulation**: each topic should be encapsulated in its own section, meaning that it should be **isolated** from the rest of the documentation content, with the latter linking to a single original source. See the folder structure and the explanation of [pseudopotential](docs/methods-directory/pseudopotential/overview.md) method, for example.

- **Abstraction**: general concepts shared by multiple specific implementations shall be explained separately from the implementations themselves. See [method](docs/methods/overview.md) and [pseudopotential](docs/methods-directory/pseudopotential/overview.md) method, explanation, for example.

- **Inheritance**: specific pages should inherit most of their contents from the general pages explained at the top level of a section. See example mentioned in the previous point.

> Example:
> 
> "All humans have two hands and two legs, which is a general and abstract property. However only a small fraction of these humans have blond hair, which is a special property. When you explain blond hair in its own specialized and encapsulated documentation page, you should not need to repeat that blond people have two legs and two hands, since such abstract concepts will be inherited from the top level page explaining the basic general physiology common to ALL humans, including blonds"

### Typical Structure of Documentation Sections

Some pages/sections appear recurrently in most documentation sections. Below is a list of the most common ones, with a brief explanation:

- **overview**: page with introduction to the contents of the present section (containing one *clickable/linked sub-header* for each main topic discussed in section). Should be present both at top level of each section, and within each of its main sub-sections.

- **ui**: section describing the user interface implementation of concepts (to should be explained separately).

- **data**: section containing JSON structured representations for the entities treated in the present section.

- **actions**: section describing the actions (such as open, edit, delete etc) related to the concepts under discussion.

### Directory Pattern

When there are multiple implementations of a particular concept, we apply a "Directory Pattern", where the concept is explained separately, and then the multiple implementations of the concept are organized into a directory. See [method](docs/methods/overview.md) and [pseudopotential](docs/methods-directory/pseudopotential/overview.md) method, explanation, for example.

## Basic Guidelines

### Formatting Styles

#### Headers

Write the main header (title) of the page as the first line, using top-level markdown notation (`#`). After adopting ["Material"](https://squidfunk.github.io/mkdocs-material/) mkdocs theme, the Table of contents (on the right, containing the current page structure) is not operational when more than one top-level header is present (h1). Therefore, we shall limit each and every page to only use **one** top-level header, and all the rest should be entered as sub-headers.
 
All other sub-headers contained throughout the remainder of the page should then be entered as second, third or even fourth degree headers, like in the following example:

```text
# Main Header (only one allowed, to be put in first line of page)
## Second-degree Sub-header
### Third-degree Sub-Header
#### Fourth-degree Sub-header
```

#### New Lines

Leave a newline after the heading elements:

```text
## Job

You can create a new job by clicking the appropriate icon.
```

#### Empty Spaces

Leave ONLY one empty line at the bottom of the page, and between paragraphs. Minimize the presence of unnecessary empty spaces within the main text of the page.

Leave more than one empty line (2-3) when "coming back" to higher-level header from nested level, as below:

```text
## Job

...

### Job Parameters

...

#### Job Sub-parameters

...


## Workflow

...
```


#### Admonition Styles

There are multiple [admonition](https://squidfunk.github.io/mkdocs-material/extensions/admonition/) classes available in MKDocs: tip (green), warning (orange), error (red), note (blue), and many others. To insert them in documentation pages, enter them with the following style:

```text
!!!tip "Unused credits"
    All unused credits automatically roll over into the next validity period.
```

is rendered into:

!!!tip "Unused credits"
    All unused credits automatically roll over into the next validity period.


#### Expandable Sections

Expandable section can be added using:

```text
<details markdown="1">
  <summary>**INCAR**</summary>
    ```
    ALGO = Normal
    EDIFF = 0.0001
    ...
    ```
</details>
```

is rendered into:

<details markdown="1">
  <summary>**INCAR**</summary>
    ```
    ALGO = Normal<br>
    EDIFF = 0.0001
    ...
    ```
</details>

Please note the `markdown=1` tag, without it the content of the `<details>` tag will not be processed appropriately. Also, the two spaces before `<summary>` seem mandatory for the same purpose.


#### ZMDI Icons

Use [zmdi](http://zavoloklom.github.io/material-design-iconic-font/cheatsheet.html) icons instead of saying "click" the button with 3 stripes:

```text
click the <i class="zmdi zmdi-check zmdi-hc-border"></i> icon
```

will be rendered as: "click the <i class="zmdi zmdi-check zmdi-hc-border"></i> icon".

We use the same ZMDI icon set for the main application. To find the correct ZMDI tag for an icon present on the Exabyte user interface, right click on it within your web browser and click on "Inspect Element". The ZMDI tag should be mentioned within the resulting HTML code describing the user interface.




### Links

#### External Links

Including an external link is best done via a dedicated "Links" footnote section at the bottom of the page, through the `[^1]`, `[^2]`, `[^3]` etc... linking notation (this feature is implemented via the Footnotes [pymdwown extension package](https://squidfunk.github.io/mkdocs-material/extensions/footnotes)). For example (note the different style of citation for Websites, PDF documents, Wikipedia articles etc....):

```text
Apple is the main competitor to Microsoft [^1].
    
Mac OS [^2] is the main Operating System developed by Apple.

Mac OS can run VASP, a type of ab-initio simulation code [^3].

Full instructions on how to use VASP can be found in Ref. [^4].
    
## Links
    
[^1]: [Microsoft, Official Website](www.microsoft.com)
[^2]: [Mac OS, Official Website](www.apple.com/mac-os.html)
[^3]: [Wikipedia Ab-initio, Website](www.wikipedia.org/ab-initio-simulations.html)
[^4]: [VASP manual, Document](www.vasp.com/user-manual.pdf)

///FOOTNOTES GO HERE///
```

By default, footnotes are included at the bottom of the page. `///FOOTNOTES GO HERE///` statement is necessary to include them elsewhere.

#### Links to Other Documentation Pages

Including a local link to another page in the documentation, or a specific sub-header section within that page, is done with the following notations respectively. 

```text
We explain service levels [in this page](../../pricing/service-levels.md)
```

```text
The particular information can be found [here](../../pricing/service-levels.md#pricing)
```

Use **ONLY RELATIVE** paths starting from the current page, not the absolute ones.




### Images and Animations

#### Including Images

Including an image/screenshot is done as follows, in MKDocs notation (don't use HTML tags).

```text
![Simulation Diagram](../../images/simulation-job-wokflow-unit-explained.png "Simulation Diagram")
```

Put images in separate folders within the main "images" directory, one for each top level section of the documentation. Also in this case it is essential to use **RELATIVE** and not absolute paths to the image, starting from the current page. 

#### Including GIFs

GIFs should be stored in the same image folders as normal images (see above). Including a GIF image is done as follows. 

```text
<img data-gifffer="/images/AddCredit.gif" />
```

In this case, absolute paths to the GIF need to be used, since we insert GIFs directly with HTML and relative paths don't work with HTML commands.

We use a third-party plugin, embedded into the source of this repository ("giffer") in order to make gif images clickable like videos.

#### Embedding Youtube Videos

Youtube videos can be embedded within documentation page through the following block of commands, linking to the video's identifier present in its URL:

```text
<div class="video-wrapper">
<iframe class="gifffer" width="100%" height="100%" src="https://www.youtube.com/embed/MBpd-yKUCM4" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>
```

#### Clickable Image Maps

Including a clickable image map is done as follows. Note that absolute paths to the image are required in this case, since we have to use HTML commands which don't work with relative paths.


```text
<img src="/images/workflow-designer-initial.png" usemap="#mapname">

<map name="mapname">
    <area shape="rect" coords="0,91,190,512" href="/workflow-designer/sidebar-items/">
    <area shape="rect" coords="190,91,754,512" href="/workflow-designer/source-editor-intro/">
    <area shape="rect" coords="0,28,754,91" href="/workflow-designer/header-menu-actions">
</map>

<!-- 
    coords="x1,y1,x2,y2"
    x1=top left X coordinate
    y1=top left Y coordinate
    x2=bottom right X coordinate
    y2=bottom right Y coordinate
-->
```



### Code Blocks

#### JSON Schemas and Examples

Including resolved JSON schemas and associated examples should be done within dedicated `data.md` pages for each concept being explained.
    
The [markdown_include](https://github.com/Exabyte-io/markdown-include) package is used to include JSON content into markdown documents, by putting direct links to pages inside the [ESSE repository](https://github.com/Exabyte-io/exabyte-esse) instead of copying their contents in the main documentation.

```text

    ```json tab="Schema" 
    {!schema/file_path/file_name.json!}
    ```
    ```json tab="Example" 
    {!example/file_path/file_name.json!}
    ```

```

#### Code Snippets 

Use the following conventions: "object" to quote object or concept, or `button` (between ` ticks as opposed to " quotes) to cite user interface icons or command-line statements in-line. 

Extended code blocks should be enclosed between pairs of triple ticks with name of interpreter for the language being shown, like so:

    ```bash
    exec something
    VARIABLE = "Example"
    print "Hello World"
    ```
    
#### Latex Math Equations

Math equations written in Latex can be inserted within documentation pages (after installing requirements - see instructions at the top of this page) both in-line and as separate blocks, using the dollar notation as shown in the following example:

```text
We define the Average Pressure $p_{avg}$ of a Material according to the following conventional formula.

$$
p_{avg}=-\frac{1}{3} \mathrm{Tr} \hspace{1pt} {\boldsymbol{\sigma}}
$$ 
```



### Writing Style

#### Formality

Some useful writing style rules are listed below:

- Language has to be simple, dry, and concise. Avoid use of superfluous, adorning or exaggerating adjectives, such as saying things like "the *complete* list of *all the many different* items". Just say "the list of items".

- Use third person when referring to reader/user. So, instead of saying "*you* can access", say it as "*the user* can access" or use the passive voice: "this functionality can be accessed".

- Allow for both genders when thinking about the reader, for example: "he/she is advised to do open the account page" or "his/her account balance should be consulted".

- Never start a sentence with short interjections like "To". Consider using more complex forms such as "In order to". Consider a similar approach with "By", "From" etc. 

- Give preference to present tense rather than future tense.

- It's better to say "click the button" than "click on the button".

- Introduce acronyms at first mention in every page, like: "Density Functional Theory (DFT) is used as a simulation tool....". Don't put acronyms in headers.

- For concepts that do not originate at Exabyte, put links to original source (or Wikipedia) instead of re-explaining them inside documentation.

#### Words to Avoid

The following list of words should be avoided:

- Simply
- Clearly
- Obviously
- In fact
- Furthermore
- Moreover
- Complete
- In particular
- Really
- Distinct
- Various 
- Automatically
- Finally


### Uploading/Updating Tutorial Videos

Follow the below instructions to upload/update a tutorial video:

1. Create a metadata file similar to the one in [here](docs/tutorials/dft/electronic/band-gap.json).

2. In metadata file, `descriptionLinks` is a list of links which are added to video description. See [description template](video-description.jinja) for more details.

3. Do not adjust the `youTubeId`. This field is automatically managed by the [video manager](video-manager.py) script.

4. Run the below command to upload/update the video once metadata is ready

```bash
source .virtualenv/bin/activate
python video-manager.py -f PATH_TO_VIDEO -m PATH_TO_METADATA
```

5. The video privacy status is set to `unlisted` by default. Pass privacy status as below to override it;

```bash
python video-manager.py -f PATH_TO_VIDEO -m PATH_TO_METADATA -p public
```
