# Introduction to JupyterLite

The **JupyterLite** environment is a lightweight implementation of JupyterLab that runs entirely in the web browser. It enables users to modify materials using Python and Jupyter notebooks with widely used packages such as `numpy`, `pymatgen`, and `ASE`.

## JupyterLite Environment

The JupyterLite environment facilitates access to Jupyter notebooks with data from the main application. 
## Access data from the Platform in JupyterLite

To access materials inside the JupyterLite environment launched from Materials Designer, use the following code snippet:

```python
from utils.jupyterlite import get_data

get_data("materials_in", globals())
```

## Send Materials Back to Materials Designer

To send the materials back to the Materials Designer, use the following code snippet:

```python
from utils.jupyterlite import send_data

materials = [material1, material2, ...]
send_data("materials", materials)
```
