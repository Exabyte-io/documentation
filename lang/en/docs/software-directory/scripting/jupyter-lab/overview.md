# Jupyter Lab


JupyterLab [^1] is the next-generation user interface for Project Jupyter [^2] offering all the familiar building blocks of the classic Jupyter Notebook [^3] in a flexible and powerful user interface. JupyterLab will eventually replace the classic Jupyter Notebook.

We include support for **Jupyter Lab** within our platform, using the operating system default interpreter version 2.7.5 for Python.

## Files/Storage Convention

1. Initially, the root of the Dropbox folder is passed to the application on the start, so the files at the root of the [Dropbox](../../../data-in-objectstorage/dropbox.md) directory can be accessed
2. Upon each "Save and Checkpoint" action invoked inside the notebook, the ipynb file is overwritten. A new version is stored in the file system, and a checkpoint is saved to the job inside its directory both in the [command-line](../../../jobs-cli/batch-scripts/directories.md#working-directory) and on the [web interface](../../../data-in-objectstorage/files.md).
3. All notebooks have access to the filesystem accessible to the user on the corresponding computational node, namely the [home](../../../infrastructure/clusters/directories.md) and [share](../../../infrastructure/clusters/directories.md) directories. For example, the following command will list the shared directory for the account "exabyte-io", when invoked inside the Jupyter Notebook running on "cluster-007":
 
    ```bash
    ls -lhta /cluster-007-share/groups/exabyte-io
    ```

## Data

We introduce the [structured representation](../../../data-structured/overview.md) for Jupyter Lab application [here](data.md).

## Links

[^1]: [Jupyter Lab, Official Documentation](https://jupyterlab.readthedocs.io/en/stable/#)
[^2]: [Project Jupyter, Official Website](https://jupyter.org/)
[^3]: [Jupyter Notebook, Official Documentation](https://jupyter-notebook.readthedocs.io/en/stable/#)
