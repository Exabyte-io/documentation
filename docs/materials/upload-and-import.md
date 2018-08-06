# Upload structure

## Open upload dialog

Open left-hand sidebar and navigate to "Materials" page. Then choose upload tool <i class="zmdi zmdi-upload zmdi-hc-border"></i> in the top right corner.

## Select File

By clicking on the `Select Items` button at the top right end of the page, you can select one or multiple files from local filesystem on your machine. Two distinct crystallographic file formats, containing such data as the lattice geometry and the ionic positions of the crystal structure under investigation, are currently supported on the Exabyte platform: the CIF and POSCAR formats. The latter format in particular represents the standard way of defining and inputting crystal structure information to the VASP DFT code, one of the simulations engines incorporated into the Exabyte platform. 

More information on how to enter crystallographic data according to both CIF and POSCAR file format specifications can be found in Refs. [[1](#links)] and [[2](#links)] respectively.

## Load Material

After selecting the desired file(s), click the `Open` button to manually import the corresponding crystal structures into the Exabyte platform. The files will then be processed by our application and added as an entry to your "Materials" list. By default the name of the material will be attempted to be read from the file you imported. Chemical formula will be used as a failover option. 

The data contained in each imported crystal structure file can be further visualized by clicking on its corresponding entry, and then collapsed back again by clicking a second time (the same functionalities can be accessed through the `Expand` and `Collapse` buttons located at the top right corner of the page, upon selection of the relevant structure file).

In case large datasets of crystal structures need to be imported at a single time, and particular elements then need to be retrieved from the resulting list, an additional filtering and searching text bar is offered at the top of the screen. This search bar can be activated or hidden with the magnifying lense tool located on the toolbar at the top right end of the page. 

This toolbar furthermore offers the possibility to delete selected crystal structures from the list, or to tag them with a list of user-defined keywords for easier fetching while performing structure searches across the Exabyte platform. This is especially resourceful when large datasets of imported structures need to be retrieved, since they already have a common search label.  

## Upload Material

Upon selection of the desired crystal structures out of the list imported in the previous step, these can be uploaded to the user's personal materials repository by clicking on the `Upload` <i class="zmdi zmdi-upload zmdi-hc-border"></i> button towards the centre of the top right toolbar. For convenience, all structures in the list can be selected simulatenously by ticking the first checkbox at the top of the list rather than each entry separately.

All the afore-mentioned steps to first manually import and then upload user-defined crystal structure files to the Exabyte platform are summarized in the picture animation below.

<img data-gifffer="/images/upload.gif" />

# Select materials

You may select previously uploaded materials during job creation. Inside "Job Designer" use the actions dropdown <i class="zmdi zmdi-more-vert zmdi-hc-border"></i> in the header and select `Chose material`. A menu overlay where one can search for materials by name/formula will appear. Enter the name, click on material entry to select it and apply selection. Repeat for other materials as needed.

You may select multiple materials at once to be used during job creation from "Materials" page by selecting the corresponding entries in "Materials" list and then clicking <i class="zmdi zmdi-open-in-new"></i> "Create Job" icon. 

# Import structure

We support direct import of data from Materials Project [[3](#links)].

## Open import dialog

Open left-hand sidebar and navigate to "Materials" page. Then choose import tool <i class="zmdi zmdi-cloud-uplod zmdi-hc-border"></i> in the top right corner.

## Select Entries

Upload dialog will let you select one or multiple entries from cloud database.

You will be presented with a full screen overlay window with a search box.  Enter the element, formula or material name to search for. To see more details about the structure and source of each entry in the list structure click and expand it.

## Trigger Import

After selecting materials click "import" icon in the toolbar (top right). This will download the material and save it in your materials collection.

<img data-gifffer="/images/ImportMaterialsProjectMaterial.gif" />

!!! warning "Outdated visuals"
    The user experience details in the visualization above might be outdated.

To use the newly imported structure, go back to the `Create Job` page and you will now see the new material available for selection as explained above.

## Links

1. [Syntax of the CIF file format](https://www.iucr.org/resources/cif/spec/version1.1/cifsyntax)

2. [Syntax of the POSCAR file format](http://cms.mpi.univie.ac.at/vasp/guide/node59.html)

3. [Materials Project](https://materialsproject.org/)
