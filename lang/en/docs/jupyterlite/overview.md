# Introduction to JupyterLite

The [**JupyterLite**](https://jupyterlite.readthedocs.io/en/stable/) environment is a lightweight implementation of JupyterLab that runs entirely in the web browser. Without the need for setup and installation, user can open, edit and run Jupyter notebooks.

## JupyterLite Environment

The JupyterLite environment facilitates access to Jupyter notebooks with data from the main application. 
It enables users to modify materials using Python and Jupyter notebooks with widely used packages such as `mat3ra-made`, `numpy`, `pymatgen`, and `ASE`.

## Accessing JupyterLite

### 1. Materials Designer
To access JupyterLite, select "Advanced > JupyterLite Transformation" from the main menu in Materials Designer.

![JupyterLite Transformation](../images/jupyterlite/md-advanced-jl.png)

### 2. Mat3ra Platform

To access JupyterLite from the Mat3ra Platform, click on the "Remote Access" icon in the top right corner of the platform and choose "JupyterLite".

![JupyterLite Button](../images/jupyterlite/platform-remote-access-jl.png)

### 3. Direct Access

To access [JupyterLite](https://jupyterlite.mat3ra.com/lab/index.html) directly, navigate to the following URL:

```
https://jupyterlite.mat3ra.com/lab/index.html
```

## Access data from the Platform in JupyterLite

To access materials inside the JupyterLite environment launched from Materials Designer, use the following code snippet:

```python
from utils.jupyterlite import get_data

get_data("materials_in", globals())
```

Parameters:

The first parameter specifies the name of the global variable (`"materials_in"`) where the received data will be stored.
The second parameter, `globals()`, ensures that the function operates correctly across both Pyodide and Python environments. It allows `get_data` to dynamically interact with the global namespace of the script.

Data Handling:

The materials data is initially stored in a global variable named `data_from_host`, which is updated in response to changes in material selection or the materials themselves.
In the context of the Pyodide environment, `data_from_host` becomes available after the Pyodide kernel has loaded and the extension set the data.

### Send Materials Back to Materials Designer

To send the materials back to the Materials Designer, use the following code snippet:

```python
from utils.jupyterlite import send_data

materials = [material1, material2, ...]
send_data("materials", materials)
```

Parameters:

The first parameter specifies the data that is being sent, which is "materials" in case for materials, this shouldn't be changed. The second parameter is the list of materials in ESSE format.

## Actions

The set of actions available in the context of the JupyterLite environment includes:

- **Open**: Open an existing notebook or file within the JupyterLite environment.
- **Run**: Execute code cells interactively within the notebook.
- **Upload File**: Upload a file from your local system to the JupyterLite environment.
- **Copy Notebook**: Create a copy of an existing notebook within the JupyterLite environment.

### Open

To open an existing notebook or file, navigate to the file browser within JupyterLite and double-click on the desired file.


### Run

To run code cells, click on the cell you want to execute and press `Shift + Enter` or click the "Run" button in the toolbar.

In most of the notebooks in the Materials Designer, the required action is to Run All Cells. To do this, click on the "Run" button in the toolbar and select "Run All Cells".

![Run All Cells](../images/jupyterlite/run-all.png)

### Upload File

To upload a file, click on the "Upload" button in the file browser, select the file from your local system, and click "Open".

![Upload File](../images/jupyterlite/upload-file.png)

### Copy Notebook

To edit an existing notebook without modifying the original, user can create a copy of the notebook.
To copy a notebook, right-click on the notebook file in the file browser, select "Copy", and then paste it in the desired location.

![Copy Notebook](../images/jupyterlite/copy-notebook.png)