We provide multiple ways to import material structures.  Our "import" feature automatically connects to and sources materials from [materialsproject.org](https://materialsproject.org) database. In addition, we currently reads a variety of input formats including VASP 4 and VASP 5 POSCAR and CIF formats.

!!! note "POSCAR and CIF file formats"
    Files should be named with .poscar or .cif extension in order to be recognized for reading.

# Upload structure

## Prepare input file

Save your VASP POSCAR or CIF file format with a .poscar or .cif extension.  For example if you have a POSCAR of a current vasp simulation, you will need to save it as POSCAR.poscar before loading the structure.

## Click Upload Material Button

On the create job page, you will see a blue button called `Upload Material`.  Click on this button and a new overlay window will appear on your screen.

## Click on Select File

This new overlay will contain another blue button called `Select File`.  Clicking on this button will bring up to browse your own directories on your machine that you are using to browse Exabyte.io.  Traverse your file system to find the file you would like to upload and select the file.  Selecting the file will require a double click in many cases or use of an "Open file" button.

## Click on Load Material

After selecting the file from your computer you should be able to click the `Load Material` button in the overlay back on the Exabyte.io website.  If successful this material load will then be read into the website and visualized.  You will have an opportunity to problem a material name to the structure as well.  By default the name of the material will be the first line of whatever file you imported.

<img data-gifffer="/images/UploadPOSCAR.gif" />


# Selecting a material from previously saved

On the create job page there is a box called `Chose a material`.  If you click on this box a searchable dropdown menu will appear displaying the name of every material in your personal materials data bank

<img data-gifffer="/images/ChooseSavedMaterial.gif" />

# Importing a structure

We support direct import of structures from Materials Project [[1](#links)]
Open the left-hand sidebar to bring up a menu with `Materials` as an option.  Click on `Materials`. You will go to the `Materials` page where in the upper right corner there is a cloud-like looking image with an arrow pointed up.  This is your `import` button.  Click on it. You will be presented with a full screen overlay window with a search box.  Enter the element, formula or material name you are interested into this box.  The search results from a live search of the Exabyte.io + Materials Project materials databases will be presented. To see more details about the structure and source of each materials structure click on the material and a dropdown box will appear.
Once you decide which structure you want to use, move your cursor to the right side of the screen on the line before any materials details drop down menu appeared.  There 3 vertical dots will appear.  Click on those 3 dots and another menu will appear with the `import` option.  This will download the material and save it in your materials collection.

<img data-gifffer="/images/ImportMaterialsProjectMaterial.gif" />

To use the newly imported structure, go back to the `Create Job` page and you will now see the material as an option to `Chose a material` as explained above.

## Links

1. [Materials Project, Website](https://materialsproject.org/)
