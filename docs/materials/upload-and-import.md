If you have a structure that is not already present in the current Exabyte.io materials data bank we provide a couple of ways to import your structure.  Our search feature is automatically connected to Materials Project database of materials so any search you do of element combinations will show you results of structures also present in the Materials Project database meeting your criteria.  In addition, Exabyte.io currently reads a variety of input formats including VASP 4 and VASP 5 POSCAR and CIF formats.  The files should be named with a .poscar and .cif extension for reading.  We will be adding additional input format methods based on the needs of our users and also plan to implement all possible input methods in pymatgen.

# Reading in your own structure
## First save your input file
Save your VASP POSCAR or CIF file format with a .poscar or .cif extension.  For example if you have a POSCAR of a current vasp simulation, you will need to save it as POSCAR.poscar before loading the structure.
## Click Upload Material Button
On the create job page, you will see a blue button called `Upload Material`.  Click on this button and a new overlay window will appear on your screen.
## Click on Select File
This new overlay will contain another blue button called `Select File`.  Clicking on this button will bring up a system dependent window to browse your own directories on your machine that you are using to browse Exabyte.io.  Traverse your file system to find the file you would like to upload and select the file.  Selecting the file will require a double click in many cases or use of an "Open file" button, but this is highly system dependent.  The screen shot below shows what this looks like on a MacBook Pro OS.
## Click on Load Material
After selecting the file from your computer you should be able to click the `Load Material` button in the overlay back on the Exabyte.io website.  If successful this material load will then be read into the website and visualized.  You will have an opportunity to problem a material name to the structure as well.  By default the name of the material will be the first line of whatever file you imported

# Selecting a material from your personal materials data bank
On the create job page there is a box called `Chose a material`.  If you click on this box a searchable dropdown menu will appear displaying the name of every material in your personal materials data bank

# Importing a structure
Currently only Materials Project [[1](#links)] is supported.
From the Exabyte.io home page or the `Create Job` webpage move your cursor to the upper left hand corner of the webpage where the 3 small parallel lines are and click with your mouse.
This will bring up a menu with `Materials` as an option.  Click on `Materials`
You will go to the `Materials` page where in the upper right corner there is a cloud-like looking image with an arrow pointed up.  This is your `import` button.  Click on it
You will be presented with a full screen overlay window with a search box.  Enter the element, formula or material name you are interested into this box.  The search results from a live search of the Exabyte.io + Materials Project materials databases will be presented.
To see more details about the structure and source of each materials structure click on the material and a dropdown box will appear.
Once you decide which structure you want to use, move your cursor to the right side of the screen on the line before any materials details drop down menu appeared.  There 3 vertical dots will appear.  Click on those 3 dots and another menu will appear with the `import` option.  This will download the material and save it in your material bank.
To use the newly imported structure, go back to the `Create Job` page and you will now see the material as an option to `Chose a material`


## Links

1. [Materials Project, Website](https://materialsproject.org/)
