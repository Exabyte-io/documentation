# JupyterLite Transformation Dialog

The JupyterLite Transformation Dialog enables the modification of materials within the JupyterLite environment, which is a lightweight implementation of JupyterLab that runs entirely in the browser. This dialog is accessible via the ["Advanced" menu](../advanced.md) within the Materials Designer interface.

<img src="/images/materials-designer/open-jupyterlite-dialog.png" alt="Open JupyterLite Transformation Dialog"/>

## JupyterLite Transformation

As depicted below, the JupyterLite Transformation Dialog facilitates the transfer of materials to the Python environment, allowing for transformations within Jupyter notebooks in the JupyterLite environment.

<img src="/images/materials-designer/jupyterlite-transformation.png" alt="JupyterLite Transformation Dialog"/>

## Select Input Materials

At the top of the dialog, a drop-down menu allows for the selection of materials to be transferred to the JupyterLite environment. These materials will then be available for further processing within JupyterLite.

<img src="/images/materials-designer/jupyterlite-transformation-input-materials.png" alt="Select Input Materials"/>

## Apply Transformation

To apply a transformation, open the notebook containing the desired transformation from the list provided in the Introduction.ipynb notebook. Follow the instructions within to apply the transformation to the selected materials. Typically, this process involves specifying settings for the transformation and clicking "Run All Cells."

<img src="/images/materials-designer/jupyterlite-transformation-apply-transformation.png" alt="Apply Transformation"/>

## Submit Results

In most cases the result of the transformation is a set of materials that can be passed back to the Materials Designer. They will appear in the "Materials Out" dropdown at the bottom of the dialog. Select the materials you want to pass back to the Materials Designer and click the "Submit" button to complete the transformation.

<img src="/images/materials-designer/jupyterlite-transformation-submit-results.png" alt="Submit Results"/>

## Animation

The following animation illustrates how to use the JupyterLite Transformation Dialog to create a matching interface between two surfaces using Zur and McGill's algorithm.

<img src="/images/materials-designer/jupyterlite-session-dialog.gif" alt="JupyterLite Transformation Dialog Animation"/>
