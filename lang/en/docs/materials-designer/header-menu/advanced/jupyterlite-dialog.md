# JupyterLite Transformation Dialog

The JupyterLite Transformation dialog allows you to interact with the JupyterLite environment, which is a lightweight implementation of JupyterLab that runs entirely in the browser. This dialog is accessible via the ["Advanced" menu](../advanced.md) > JupyterLite Transformation within the Materials Designer interface.

![JupyterLite Session Dialog](../../../images/materials-designer/open-jupyterlite-dialog.png "JupyterLite Session Dialog")

## JupyterLite Transformation

The JupyterLite Transformation dialog is shown in the image below. It allows you to pass materials to the Python environment and apply transformation within Jupyter notebooks in the JupyterLite environment.

![JupyterLite Transformation Dialog](../../../images/materials-designer/jupyterlite-transformation.png "JupyterLite Transformation Dialog")

## Select Input Materials

The dialog features a drop-down menu at the top, where you can select the materials you want to pass to the JupyterLite environment. The selected materials will be available in the JupyterLite environment for further processing.

![Select Input Materials](../../../images/materials-designer/jupyterlite-transformation-input-materials.png "Select Input Materials")

## Apply Transformation

Open the notebook with desired transformation from the list of available option in the Introduction.ipynb notebook. Follow the instructions in the notebook to apply the transformation to the selected materials.

![Apply Transformation](../../../images/materials-designer/jupyterlite-transformation-apply-transformation.png "Apply Transformation")

## Submit Results

In most cases the result of the transformation is a set of materials that can be passed back to the Materials Designer. They will appear in the Materials Out dropdown at the bottom of the dialog. Select the materials you want to pass back to the Materials Designer and click the "Submit" button to complete the transformation.

![Submit Results](../../../images/materials-designer/jupyterlite-transformation-submit-results.png "Submit Results")

