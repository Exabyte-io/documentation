# Upload structure

## Open upload dialog

Open left-hand sidebar and navigate to "Materials" page. Then choose upload tool <i class="zmdi zmdi-upload zmdi-hc-border"></i> in the top right corner.

## Select Files

By clicking on the `Select Items` button <i class="zmdi zmdi-collection-plus zmdi-hc-border"></i> at the top right end of the page, you can select one or multiple files from local filesystem on your machine. Two distinct crystallographic file formats, containing such data as the lattice geometry and the ionic positions of the crystal structure under investigation, are currently supported on the Exabyte platform: the CIF and POSCAR formats. The latter format in particular represents the standard way of defining and inputting crystal structure information to the VASP DFT code, one of the simulations engines incorporated into the Exabyte platform. 

More information on how to enter crystallographic data according to both CIF and POSCAR file format specifications can be found in Refs. [[1](#links)] and [[2](#links)] respectively.

### Expand Content

The data contained in each imported crystal structure file can be further visualized by clicking on its corresponding entry, and then collapsed back again by clicking a second time (the same functionalities can be accessed through the `Expand` and `Collapse` buttons located at the top right corner of the page, upon selection of the relevant structure file).

### Search

In case large datasets of crystal structures need to be imported at a single time, and particular elements then need to be retrieved from the resulting list, an additional filtering and searching text bar is offered at the top of the screen. This search bar can be activated or hidden with the magnifying lense tool located on the toolbar at the top right end of the page. 

### Tag

This toolbar furthermore offers the possibility to delete selected crystal structures from the list, or to tag them with a list of user-defined keywords for easier fetching while performing structure searches across the Exabyte platform. This is especially resourceful when large datasets of imported structures need to be retrieved, since they already have a common search label. 

## Upload Files

Once the crystal structure files have been manually imported into the Exabyte platform, they will then be processed by our application and added as an entry to your "Materials" list. By default the name of the material will be attempted to be read from the file you imported. Chemical formula will be used as a failover option.  

Upon selection of the desired crystal structures out of the list imported in the previous step, these can be uploaded to the user's personal materials repository by clicking on the `Upload` <i class="zmdi zmdi-upload zmdi-hc-border"></i> button towards the centre of the top right toolbar. For convenience, all structures in the list can be selected simulatenously by ticking the first checkbox at the top of the list rather than each entry separately.

All the afore-mentioned steps to first manually import and then upload user-defined crystal structure files to the Exabyte platform are summarized in the picture animation below.

<img data-gifffer="/images/upload.gif" />


## Links

1. [Syntax of the CIF file format](https://www.iucr.org/resources/cif/spec/version1.1/cifsyntax)

2. [Syntax of the POSCAR file format](http://cms.mpi.univie.ac.at/vasp/guide/node59.html)
