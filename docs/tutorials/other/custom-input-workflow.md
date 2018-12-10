<!-- TODO by MH -->

This tutorial shows you how to set up a custom workflow for characteristic property calculation.  We have made our framework customizable to enable you to add, edit and delete any execution unit.

# Create job

To create a new job, click on the "Create Job" link located in the sidebar/menu on the left.

You will be taken to the "Job wizard" page where you can create a material or choose one that you created and saved before using Materials Designer tab.

<img data-gifffer="/images/tutorials/tutorials/FirstJobCreate.gif" />

# Choose workflow

By default when creating a job a workflow is chosen. With Quantum ESPRESSO that workflow in bandstructure and includes 3 units. The animation below shows how it is possible to delete those units and add your own custom empty execution units as well.

<img data-gifffer="/images/tutorials/tutorials/CustomAddDelete.gif" />

!!! Warning "Custom workflows REQUIRE user input"
    A custom workflow will not work if a unit is added without the user adjusting the input file text. Once the unit is added the user will need to open the unit and enter text into the input files to enable the simulation to run. As shown above, the control sections of a Quantum ESPRESSO file will be empty.  Below, we show adding a custom VASP unit leads to empty INCAR and KPOINTS files that must be edited to enable the workflow to run.


# Paste input files text

There are a wide variety of example simulation input files available on the web.  If we have not supported those workflows yet, we provide a method to run multiple step workflows.  For example, there is a [VASP Wiki](http://cms.mpi.univie.ac.at/wiki/index.php/VASP_example_calculations) with a large number of example input files.

Below we show how to add a dielectric constant and frequency calculation into our workflow units.  The simulations could then be executed by pressing the "Compute" tab and then "Submit Job". Exabyte will only display the standard output of each unit but all output files will be present at the end of the simulation accessible on the web.

<img data-gifffer="/images/tutorials/tutorials/AddIncar1.gif" />

<img data-gifffer="/images/tutorials/tutorials/AddIncar2.gif" />
