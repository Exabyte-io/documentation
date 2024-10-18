---
# YAML header
render_macros: true
---

# Pyodide

JupyterLite uses [Pyodide](https://pyodide.org/en/stable/) as a kernel to run Python code in the browser.

## Overview

Pyodide is a Python distribution for the browser and Node.js based on port of CPython to WebAssembly/Emscripten, enabling Python code execution directly in the browser. 
It includes a comprehensive set of Python packages and allows additional package installations from PyPI.

## Dependencies installation

To install dependencies in Pyodide, the `micropip` package is used. 
Here's an example of how to install the `numpy` package:

```python
import micropip

await micropip.install("numpy")
```

> Note: Only pure Python packages are supported in Pyodide.

## Example Usage

To understand the basics of using Pyodide user can refer to the interactive documentation below.

{% with origin_url="https://jupyterlite.github.io/demo/notebooks/index.html?path=python.ipynb" %}
{% include 'jupyterlite_embed.html' %}
{% endwith %}