# Edit Description

We demonstrate in the animation below how to add an example description to a Job inspected in [Viewer](../../jobs/ui/viewer.md). After toggling the description switch, we enter a series of headers in Markdown syntax [^1] and then add an equation from Wikipedia. Note that the editor also supports editing a document directly using the "what you see is what you get" approach [^2].

<img data-gifffer="/images/entities-general/metadata-workflow-description.gif" />

You can create headers by using `#` symbols, with the number of symbols indicating the level of the header (e.g., `# Header1`, `## Header2`). To create emphasis, use asterisks or underscores around your text: one for italics (`*italics*` or `_italics_`), two for bold (`**bold**` or `__bold__`). For lists, use dashes, asterisks, or plus signs. For links, use square brackets around the linked text and parentheses around the URL like so: `[link text](url)`.

The editor also supports the following formatting blocks:

- Math block (using [Katex](https://katex.org/docs/supported.html) syntax)
  ```
  $$math
    \alpha \beta \gamma
    ...
  $$
  ```
- Code block (e.g. Python)
  ````markdown
  ```python
    import numpy as np
    ...
  ```
  ````
- Table
  ```markdown
  | id  | name         | unit    |
  | --- | --- | --- |
  | 001 | total_energy | hartree |
  ...
  ```
- Checklist
  ```markdown
  1. [x] run structure relaxation
  2. [ ] analyze results
  ...
  ```

For more information on the Markdown and the Markdown editor, please visit this [documentation](https://ui.toast.com/tui-editor) or the summary linked below[^1].



## Edit Tags

In order to edit Tags, modify the content in the relevant text field pressing "Enter" key after each word or phrase. The corresponding tag is consequently included on the same line, with the option to delete it made available to its right through the "X" icon button. 

The aforementioned process is demonstrated in the animation below.

<img data-gifffer="/images/entities-general/tagging-workflow.gif" />

## Links

[^1]: [Markdown syntax summary, Website](https://daringfireball.net/projects/markdown/syntax)
[^2]: [WYSIWYG Wikipedia, Website](https://en.wikipedia.org/wiki/WYSIWYG) 
