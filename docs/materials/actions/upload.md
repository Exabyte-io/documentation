# Upload structures

At present we support uploading structural data in two file formats: CIF and POSCAR. Both contain the lattice geometry and the ionic positions of the crystal structure under investigation. The latter format represents the standard way of defining and inputting crystal structure information to the VASP DFT code, one of the simulations engines incorporated into our platform. More information on how to enter crystallographic data according to both CIF and POSCAR file format specifications can be found in Refs. [[1](#links)] and [[2](#links)] respectively.

# Open upload dialog

Open left-hand sidebar and navigate to "Materials" page. Then choose upload tool <i class="zmdi zmdi-upload zmdi-hc-border"></i> in the top right corner.

# Select Files

By clicking on the `Select Items` tool <i class="zmdi zmdi-collection-plus zmdi-hc-border"></i> at the top right end of the page and following the file upload dialog, you can select one or multiple files from the local filesystem on your machine.  When you are done, the files are processed by the web browser and arranged in a list prepared to be uploaded to our platform. The list will also contain information about whether a certain file has already been used for uploading structural information before.

## Expand Content

The data contained in each crystal structure file can be further visualized by clicking on its corresponding entry, and then collapsed back again by clicking a second time (the same functionalities can be accessed through the `Expand` and `Collapse` tools located at the top right corner of the page, upon selection of the relevant structure file).

## Search

In case large datasets of crystal structures need to be imported at a single time, and particular elements then need to be retrieved from the resulting list, an additional filtering and searching text bar is offered at the top of the screen. This search bar can be activated or hidden with the `Search` tool <i class="zmdi zmdi-search zmdi-hc-border"></i> located on the toolbar at the top right end of the page. 

## Tag

Users may tag structures with a list of keywords. This is especially resourceful when large datasets of imported structures need to be retrieved or filtered later. The general guidelines for entering descriptive tags and attach them to entities are presented [here](/entities-general/actions/metadata.md).

## Upload Files

Upon selection of the desired crystal structures can be uploaded to the platform by clicking on the `Upload` <i class="zmdi zmdi-upload zmdi-hc-border"></i> tool. For convenience, all structures in the list can be selected simultaneously by ticking the "Select All" checkbox at the top of the list.

# View Materials

Once the crystal structure files have been imported into the platform, they will be added as an entries to "Materials" list. By default the name of the material will be attempted to be read from the file imported. Chemical formula will be used as a backup option.  


# Animation

All the aforementioned steps are demonstrated in the animation below.

<img data-gifffer="/images/upload.gif" />


# Links

1. [Syntax of the CIF file format](https://www.iucr.org/resources/cif/spec/version1.1/cifsyntax)

2. [Syntax of the POSCAR file format](http://cms.mpi.univie.ac.at/vasp/guide/node59.html)
