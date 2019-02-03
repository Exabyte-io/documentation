# Create Materials With VESTA

The present tutorial describes the steps necessary for connecting to our platform via a [Remote Desktop](../../remote-connection/remote-desktop.md) session, in order to create and manipulate a newly-created [material structure](../../materials/overview.md) through the pre-installed [VESTA](../../software-directory/analysis/vesta.md) graphical analysis and visualization software. 

We shall then demonstrate how this new crystal structure can later be retrieved within the account-owned [collection](../../accounts/collections.md) of materials accessible via our [Web Interface](../../ui/overview.md), through the help of the [Dropbox functionality](../../data-in-objectstorage/dropbox.md) of our platform.
 
Additional analysis software similar to VESTA can be retrieved under Remote Desktop, as introduced under the list presented [herein](../../software-directory/overview.md#analysis-tools). 

## Accessing Remote Desktop

One must open a [Remote Desktop Connection](../../remote-connection/remote-desktop.md) via our [Web Interface](../../ui/overview.md) in order to run [graphical interface programs](../../software-directory/overview.md#analysis-tools) for material analysis and visualization purposes. 

The instructions for opening and launching a Remote Desktop session can be found under [this page](../../remote-connection/actions/open-desktop.md).

## Launching VESTA Visualization Software

The user should now [follow this procedure](../../remote-connection/actions-rd/open-app.md) in order to start a session of the [VESTA](../../software-directory/analysis/vesta.md) graphical materials analysis software.

!!! warning "Avoid compute intensive visualization tasks"
    We kindly ask users to avoid running excessively intensive visualization tasks when interacting with analysis software such as VESTA, as it may interfere with other users' operations during the course of their execution.

## Use VESTA to Create a New Crystal Structure 

In the context of this tutorial, we shall make use of VESTA to create a new crystal structure consisting in Sodium Chloride (NaCl). We remind the reader about the basic features of such a crystal structure.

- Space Group: Fm-3m

- Bravais Lattice: face-centred cubic

- Lattice Constant: 5.604 Angstrom

- Atomic Positions of Na atoms: (0,0,0); (1/2,1/2,0); (1/2,0,1/2); (0,1/2,1/2)

- Atomic Positions of Cl atoms: (1/2,1/2,1/2); (0,0,1/2); (0,1/2,0); (1/2,0,0)

A visual representation of the NaCl crystal structure is portrayed below.

![NaCl Crystal Structure](../../images/tutorials/NaCl-crystal-structure.gif "NaCl Crystal Structure")

### Open New Structure Dialog

In order to create a new material structure through VESTA, the user should click the "New Structure" option at the top of the File Menu, accessible at the top-left corner of the VESTA graphical user interface. Doing this will open a "New Data" dialog, with which new crystal structures such as NaCl can be defined by entering the relevant crystallographic structural information.
 
### Insert Lattice Parameters and Atomic Positions
 
 The user should first enter the above-mentioned lattice parameters of the NaCl face-centred cubic unit cell under the "Unit Cell" tab of the dialog. Here, the relevant cubic space group (Fm-3m, number 225) can also be selected.
 
 Secondly, the atomic positions and chemical identity of both the Na and Cl atoms should be inserted within the "Structure Parameters" tab, by clicking on "New" every time a new atom is added to the central table in this tab.

At the end of entering the appropriate crystallographic data for NaCl, the "New Data" dialog should be closed and the changes recorded by clicking the `OK` button at the bottom of the dialog. The view will hence be returned to the main VESTA interface, with which the crystal structure of NaCl can be visualized and manipulated graphically at will by the user.

## Save Structure as POSCAR to Dropbox

Following the creation of the NaCl crystal structure within VESTA, the associated data can then be exported to the POSCAR file format directly to the [Dropbox Folder](../../data-in-objectstorage/dropbox.md) accessible to the user, affording for the simultaneous sharing of files between all [nodes of our platform](../../infrastructure/overview.md). This should be done by clicking the "Export Data" option under the top-left "File" menu of the VESTA interface.

Under the resulting "Export Data" dialog, the [dropbox folder](../../data-on-disk/directories.md#dropbox) accessible via the user's [home folder](../../infrastructure/login/directories.md) should be selected, and the appropriate POSCAR file format should be chosen under the bottom-right menu of the dialog. A suitable filename can also be entered at the top for later retrieval of the file. The interface will finally allow the user to choose between saving the crystallographic atomic position data in fractional or Cartesian coordinates, and whether to convert the crystal structure to its Niggli reduced cell representation. 

## Download Structure

The user can now exit the Remote Desktop session and return to the main [Web Interface](../../ui/overview.md) of our platform. The same crystallographic POSCAR file saved in the preceding step can now be retrieved again under the [Dropbox Page](../../data-in-objectstorage/ui/dropbox-page.md), accessible through the main [Left-hand Sidebar Menu](../../ui/left-sidebar.md) of the Web Interface.

## Upload Structure to Materials Collection

The POSCAR file should be downloaded to the local disk by following [these instructions](../../data-in-objectstorage/actions/download.md). After switching to the [Materials Explorer Page](../../materials/ui/explorer.md), this same POSCAR file can then be uploaded again into our platform, and thus added to the account-owned [collection](../../accounts/collections.md) of materials. Uploading a POSCAR structure file is achieved as explained under [this page](../../materials/actions/upload.md).

## Animation 

The above-mentioned steps involved in the creation and visualization of a new NaCl crystal structure through the [VESTA](../../software-directory/analysis/vesta.md) analysis software, incorporated into our [Remote Desktop Interface](../../remote-connection/remote-desktop.md), are illustrated in the below video.
 
We conclude this animation by saving the crystal structure data under the POSCAR format to the [Dropbox Folder](../../data-in-objectstorage/dropbox.md), and by later retrieving it under the Web Interface in order to upload it and inserting it into the account-owned [collection](../../accounts/collections.md) of materials, as narrated in the preceding paragraphs of the present tutorial page.
