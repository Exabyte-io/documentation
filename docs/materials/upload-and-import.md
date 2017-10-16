# Upload structure

## Open upload dialog

Open left-hand sidebar and navigate to "Materials" page. Then choose upload tool <i class="zmdi zmdi-upload zmdi-hc-border"></i> in the top right corner.

## Select File

Upload dialog will let you select one or multiple files from local filesystem on your machine.

## Load Material

After selecting file(s) click the `Load` button. File will then be processed by our application and added as an entry to your "Materials" list. By default the name of the material will be attempted to be read from the file you imported. Chemical formula will be used as a failover option.

# Select materials

You may select previously uploaded materials during job creation. Inside "Job Designer" use the actions dropdown <i class="zmdi zmdi-more-vert zmdi-hc-border"></i> in the header and select `Chose material`. A menu overlay where one can search for materials by name/formula will appear. Enter the name, click on material entry to select it and apply selection. Repeat for other materials as needed.

You may select multiple materials at once to be used during job creation from "Materials" page by selecting the corresponding entries in "Materials" list and then clicking <i class="zmdi zmdi-open-in-new"></i> "Create Job" icon. 

# Import structure

We support direct import of data from Materials Project [[1](#links)].

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

1. [Materials Project](https://materialsproject.org/)
