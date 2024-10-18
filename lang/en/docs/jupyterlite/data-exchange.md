# Data Exchange with JupyterLite

## Overview

JupyterLite environment can exchange data (1) either directly with the platform or (2) with its sub-parts, such as the [Materials Designer](../materials-designer/overview.md).

## Get data inside JupyterLite

`get_data` is used to init a local variable and make it available inside the session.

For example, to work with materials data inside the JupyterLite environment inside [Materials Designer](../materials-designer/overview.md), use the following code snippet:

```python
from utils.jupyterlite import get_data

get_data("materials_in", globals())
```

The first parameter specifies the name of the global variable (`"materials_in"`) where the received data will be stored. The second parameter, `globals()`, ensures the function operates correctly across both Pyodide and Python environments. It allows `get_data` to dynamically interact with the global namespace of the script.

Data Handling:

The materials data is initially stored in a global variable named `data_from_host`, which is updated in response to changes in material selection or the materials themselves.
In the context of the Pyodide environment, `data_from_host` becomes available after the Pyodide kernel has loaded and the extension set the data.

## Send data outside

To send the materials back to the Materials Designer, use the following code snippet:

```python
from utils.jupyterlite import send_data

materials = [material1, material2, ...]
send_data("materials", materials)
```

Parameters:

The first parameter specifies the data that is being sent, which is "materials" in case for materials, this shouldn't be changed. The second parameter is the list of materials in ESSE format.
