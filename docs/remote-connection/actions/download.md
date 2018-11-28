# Download Remote Files

Starting from the [Web Terminal](../web-terminal.md), the user can download any remotely stored file to his/her local disk with the `exadownload` command. Typing `exadownload <filepath/filename>` under the [Command Line Interface](../../cli/overview.md) downloads the file directly to the default location for saving Downloaded content for the web browser under consideration.

From [Remote Desktop](../remote-desktop.md) on the other hand, the user can download files (of limited size) by putting them in the [Dropbox](../../data-in-objectstorage/dropbox.md) folder first, which has an overall capacity of 1 Gb. Such files can later be downloaded from the [Web Interface](../../ui/overview.md) by clicking their corresponding entries listed under the [Files Explorer](../../data-in-objectstorage/ui/explorer.md) interface of the [Dropbox Page](../../data-in-objectstorage/ui/dropbox-page.md), as explained [here](../../data-in-objectstorage/actions/download.md).

## Animation for Remote Desktop

We demonstrate how to download a file called "remote-connection.yaml", present under the [Login Home](../../infrastructure/login/directories.md) directory, starting from the Remote Desktop interface and then retrieving the same file under the Dropbox contents listed within the Web Interface.

<img data-gifffer="/images/download-rd.gif" />

## Animation for Web Terminal

Here, we show the equivalent animation, but for the Web Terminal. We download the same "remote-connection.yaml" file as before by entering the corresponding `exadownload` command introduced previously.

<img data-gifffer="/images/download-wt.gif" />
