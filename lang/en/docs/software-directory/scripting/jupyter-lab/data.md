# Jupyter Lab: Data

## Structured Representation

We present in what follows the [structured representation](../../../data-structured/overview.md) for the [Jupyter Lab Application](overview.md).

```json tab="Schema" 
{!schema/software_directory/scripting/jupyter-lab.json!}
```

```json tab="Example" 
{!example/software_directory/scripting/jupyter-lab.json!}
```

## Files/Storage Convention

1. Initially, the root of the Dropbox folder is passed to the application on the start, so the files at the root of the [Dropbox](../../../data-in-objectstorage/dropbox.md) directory can be accessed
2. Upon each "Save and Checkpoint" action invoked inside the notebook, the ipynb file is overwritten. A new version is stored in the file system, and a checkpoint is saved to the job inside its directory both in the [command-line](../../../jobs-cli/batch-scripts/directories.md#working-directory) and on the [web interface](../../../data-in-objectstorage/files.md).
3. All notebooks have access to the filesystem accessible to the user on the corresponding computational node, namely the [home](../../../infrastructure/clusters/directories.md) and [share](../../../infrastructure/clusters/directories.md) directories. For example, the following command will list the shared directory for the account "exabyte-io", when invoked inside the Jupyter Notebook running on "cluster-007":
 
    ```bash
    ls -lhta /cluster-007-share/groups/exabyte-io
    ```
