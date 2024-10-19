# JupyterLite: File Storage and Synchronization

## Main Concepts

When Jupyter notebooks or files inside the JupyterLite (JL) environment are opened, these files are stored locally inside a browser.

### Local storage

Files and notebooks are saved to your local browser storage and persist in it until the local storage cache is reset.

### No cross-device syncing

If the same URL is opened on another machine or browser, it will not carry over any changes made in the first environment.

### "Default" and custom notebooks

Our JupyterLite environment provides a set of "default" notebooks that are available in the sidebar. If a user creates a new notebook or uploads a file, it will be stored in the browser's local storage only. 

### File restoration

If the user deletes a "default" notebook present or file, it is restored to the original version upon deletion. Note that this does not apply to custom notebooks or files.

## Updating Notebooks/Files

When updates to JupyterLite or its API examples are released, it’s important to delete the corresponding folder in JupyterLite or clear the local cache (for the `jupyterlite.mat3ra.com` URL) to ensure that the updated content is correctly loaded. Here's how to manage this:

- Clear local storage: You can manually delete the files stored on your browser or clear the browser's local storage so JupyterLite can reload the updated versions.
- Cache refresh: After a JupyterLite update, you may need to delete the directory containing distributed notebooks and files to ensure the most up-to-date versions are loaded.

### Reset a "default" notebook

Select one of the "default" notebooks in the sidebar, right-click, and select "Delete" in the context menu. It will be restored to the original version.

<img data-gifffer="/images/jupyterlite/jl-delete-reset-notebook.gif" />

## Synchronizing Files between sessions

To share changes between devices or browser sessions, including within different parts of the platform, one needs to explicitly copy and transfer/reupload the file.

Download and upload the notebook to move between Chrome and Safari sessions:

<img data-gifffer="/images/jupyterlite/jl-download-upload.gif" />
