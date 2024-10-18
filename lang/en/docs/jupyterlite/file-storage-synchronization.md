# JupyterLite: File Storage and Synchronization

## Main Concepts

When Jupyter notebooks or files inside the JupyterLite (JL) environment are opened, these files are stored locally inside a browser.

### Local storage

Files and notebooks are saved to your local browser storage and persist in it until the local storage cache is reset.

### No cross-device syncing

If the same URL is opened on another machine or browser, it will not carry over any changes made in the first environment.

### File restoration: 

If a distributed notebook or file is deleted by the user, it is restored to the original version upon deletion.

## Updating Notebooks/Files

When updates to JupyterLite or its API examples are released, it’s important to delete corresponding folder in JupyterLite or clear the local cache (for the `jupyterlite.mat3ra.com` URL) to ensure that the updated content is correctly loaded. Here's how to manage this:

- Clear local storage: You can either manually delete the files stored on your browser or clear the browser's local storage for JupyterLite to reload the updated versions.
- Cache refresh: After a JupyterLite update, you may need to delete the directory containing distributed notebooks and files to ensure the most up-to-date versions are loaded.

Reset one notebook:

<img data-gifffer="/images/jupyterlite/jl-delete-reset-notebook.gif" />

Reset multiple notebooks:

<img data-gifffer="/images/jupyterlite/jl-delete-reset-multiple.gif" />


## Synchronizing Files between sessions

To share changes between devices or browser sessions, including within different parts of the platform, one needs to explicitly copy and transfer/reupload the file.

<!-- TODO: add visual -->
