# JupyterLite: File Storage and Synchronization

## Local File Storage

When Jupyter notebooks or files on the JupyterLite (JL) server opened via a provided URL, such as from the Materials Designer or Mat3ra Platform, these files are stored locally on your browser. This means:

- Local storage: Files and notebooks are saved to your local browser storage. They are not synced across different browsers or devices.
- No cross-device syncing: If the same URL is opened on another machine or browser, it will not carry over any changes made in the first environment.
- File restoration: If a distributed notebook or file is deleted by the user, it is restored to the original version upon deletion.

## Updating Notebooks and Files

When updates to JupyterLite or its API examples are released, it’s important to delete corresponding folder in JupyterLite or clear the local cache (for the `jupyterlite.mat3ra.com` URL) to ensure that the updated content is correctly loaded. Here's how to manage this:

- Clear local storage: You can either manually delete the files stored on your browser or clear the browser's local storage for JupyterLite to reload the updated versions.
- Cache refresh: After a JupyterLite update, you may need to delete the directory containing distributed notebooks and files to ensure the most up-to-date versions are loaded.

## Synchronization Behavior

JupyterLite instances opened via Materials Designer, Mat3ra Platform, or by a provided URL (e.g., `jupyterlite.mat3ra.com`) behave slightly differently:

- Per-machine sync: The files and notebooks opened in these instances are synced within the same browser and machine. Since they are loaded in an iframe (displaying the JupyterLite URL), they persist for that specific browser and device.
- Non-shared state: However, any changes or files are still specific to that browser instance, and they are not shared between devices or browsers unless explicitly copied or transferred.

