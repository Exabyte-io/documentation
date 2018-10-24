# Upload Structures

At present, we support uploading structural data in two file formats: CIF and POSCAR. Both contain the lattice geometry and the ionic positions of the crystal structure under investigation. The latter format represents the standard way of defining and inputting crystal structure information to the [VASP DFT code](/applications/vasp.md), one of the simulations engines incorporated into our platform. 

More information on how to enter crystallographic data according to both CIF and POSCAR file format specifications can be found in Refs. [[1](#links)] and [[2](#links)] respectively.

# Open Upload Dialog

Under the [Account Profile](/accounts/ui/profile-page.md) page, first [navigate](/ui/specific/tabs-navigator.md) to the "Materials" tab. Then choose upload tool <i class="zmdi zmdi-upload zmdi-hc-border"></i> in the top right [actions toolbar](/entities-general/ui/explorer.md#actions-toolbar).

# Select Files

Click the `Select Items` tool <i class="zmdi zmdi-collection-plus zmdi-hc-border"></i> in the top right [actions toolbar](/entities-general/ui/explorer.md#actions-toolbar) of this new page, to open a file upload dialog.
 
 Through this dialog, the user can select one or multiple files from the local filesystem on his/her machine. The files are then processed by the web browser and arranged in a list prepared to be uploaded to our platform. This list also contains information about whether a certain file has already been used for uploading structural information before.

## Expand Content

The data contained in each crystal structure file can be further visualized by clicking its corresponding entry, and then collapsed back again by clicking a second time. 

The same functionality can be accessed through the `Expand` and `Collapse` tools located in the top-right [actions toolbar](/entities-general/ui/explorer.md#actions-toolbar) of the page, upon selection of the relevant structure file.

## Search

In case large datasets of crystal structures need to be imported at a single time, and particular elements then need to be retrieved from the resulting list, an additional [filtering and searching](/entities-general/actions/search.md) text bar is offered at the top of the screen. 

This search bar can be activated or hidden with the `Search` tool <i class="zmdi zmdi-search zmdi-hc-border"></i> located in the top-right [actions toolbar](/entities-general/ui/explorer.md#actions-toolbar) of the page. 

## Tag

Users may tag structures with a list of keywords. This is especially resourceful when large datasets of imported structures need to be retrieved or filtered later. The general guidelines for entering descriptive tags and attach them to entities are presented [here](/entities-general/actions/metadata.md).

## Upload Files

Upon selection of the desired crystal structures, they can be uploaded to the platform by clicking `Upload` <i class="zmdi zmdi-upload zmdi-hc-border"></i> in the top-right [actions toolbar](/entities-general/ui/explorer.md#actions-toolbar). 

For convenience, all structures in the list can be selected simultaneously by ticking the "Select All" checkbox at the top of the list.

# View Materials

Once the crystal structure files have been imported into the platform, they are added as entries to the Account-owned Materials collection. By default, the name of the material is read from the imported file, if possible. Chemical formula is otherwise used as a backup option.  


# Animation

The aforementioned steps are demonstrated in the animation below.

<img data-gifffer="/images/upload.gif" />


# Links

1. [Syntax of the CIF file format](https://www.iucr.org/resources/cif/spec/version1.1/cifsyntax)

2. [Syntax of the POSCAR file format](http://cms.mpi.univie.ac.at/vasp/guide/node59.html)
