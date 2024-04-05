# Import Materials from Files

This tutorial explains how to import materials from files in various formats into the Materials Designer interface. With the help of notebook that uses ASE python package to extract structural information from files in multiple formats (CIF, POSCAR, etc., as supported by ASE). Some formats, like espresso-in and espresso-out can be inferred from the file content.

## Step 0: Open Materials Designer

Start by opening an instance of the [Materials Designer Interface](../../materials-designer/overview.md) for creating and designing new [Materials structures](../../materials/overview.md) on our platform.

## Step 1: Open JupyterLite Environment

Open the [JupyterLite Environment](../../materials-designer/header-menu/advanced/jupyterlite-dialog.md) by navigating to "Advanced" > "JupyterLite Transformation" menu item in the Materials Designer interface.

## Step 2: Open the Notebook

Open the "Materials import from files in ASE-supported formats" in the Introduction.ipynb notebook.

![JupyterLite session with Introduction notebook](/images/tutorials/import_from_files/open_notebook.webp "Open Notebook")

## Step 3: Upload files

Double-click the `uploads` folder in the File Browser tab on the left to open it. Drag and drop the files you want to import into the field.

![JupyterLite session with uploaded files in the files browser](/images/tutorials/import_from_files/upload_files.webp "Upload Files")

## Step 4: Run the Notebook

Run the notebook by clicking the "Run All Cells" button in the toolbar or execute each cell by pressing "Shift + Enter" if you want to review results or change the code in the process.

![JupyterLite session with Run menu open](/images/tutorials/import_from_files/run_notebook.webp "Run Notebook")

## Step 5: Review the Results and Submit

Materials should appear in the "Materials Out" dropdown at the bottom of the dialog. Select the material you want to work with and click "Submit" to load it into the Materials Designer.

In case ASE is unable to read the file, an error message will be printed stating the unreadable files and a table of available formats. The information about ASE IO can be found [here](https://wiki.fysik.dtu.dk/ase/ase/io/io.html).
In this case, you can try to fix the issue and re-run the notebook. The error with some files does not prevent other files from being read.

![JupyterLite Transformation dialog with materials_out dropdown populated](/images/tutorials/import_from_files/submit_results.webp "Review Results and Submit")
