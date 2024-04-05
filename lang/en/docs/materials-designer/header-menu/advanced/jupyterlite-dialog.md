# JupyterLite Transformation Dialog

The JupyterLite Transformation dialog allows you to change materials within the JupyterLite environment, which is a lightweight implementation of JupyterLab that runs entirely in the browser. This dialog is accessible via the ["Advanced" menu](../advanced.md) within the Materials Designer interface.

<img src="/images/materials-designer/open-jupyterlite-dialog.png" alt="Open JupyterLite Transformation Dialog"/>

## JupyterLite Transformation

The JupyterLite Transformation dialog is shown in the image below. It allows you to pass materials to the Python environment and apply transformation within Jupyter notebooks in the JupyterLite environment.

<img src="/images/materials-designer/jupyterlite-transformation.png" alt="JupyterLite Transformation Dialog"/>

## Select Input Materials

The dialog features a drop-down menu at the top, where you can select the materials you want to pass to the JupyterLite environment. The selected materials will be available in the JupyterLite environment for further processing.

<img src="/images/materials-designer/jupyterlite-transformation-input-materials.png" alt="Select Input Materials"/>

## Apply Transformation

Open the notebook with desired transformation from the list of available option in the Introduction.ipynb notebook. Follow the instructions in the notebook to apply the transformation to the selected materials. Most of the time user will need to specify settings for the transformation and click "Run All Cells".

<img src="/images/materials-designer/jupyterlite-transformation-apply-transformation.png" alt="Apply Transformation"/>

## Submit Results

In most cases the result of the transformation is a set of materials that can be passed back to the Materials Designer. They will appear in the Materials Out dropdown at the bottom of the dialog. Select the materials you want to pass back to the Materials Designer and click the "Submit" button to complete the transformation.

<img src="/images/materials-designer/jupyterlite-transformation-submit-results.png" alt="Submit Results"/>

## Animation

The animation below demonstrates usage of the JupyterLite Transformation dialog for creation of a coherent interface between two surfaces using Zur and McGill's algorithm.
<img src="/images/materials-designer/jupyterlite-session-dialog.gif" alt="JupyterLite Transformation Dialog Animation"/>
