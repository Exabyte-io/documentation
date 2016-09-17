<!-- TODO by MH -->

This tutorial shows you how to provide your own custom workflow for property calculation.  We have made our framework extenable to enable you to add, edit and delete any execution unit.

# Create job

To create a new job, click on the "Create Job" link located in the sidebar/menu on the left.

You will be taken to the "Job wizard" page where you can create a material or choose one that you created and saved before using Materials Designer tab.

<img data-gifffer="/images/FirstJobCreate.gif" />

# Choose workflow

By default when creating a job a workflow is chosen. With Quantum ESPRESSO that workflow in bandstructure and includes 3 units. The animation below shows how it is possible to delete those units and add your own custom empty execution units as well.

<img data-gifffer="/images/CustomAddDelete.gif" />

# Paste in custom input files

There are a wide variety of example simulation input files available on the web.  If we have not supported those workflows yet, we provide a method to run multiple step workflows.  For example, there is a [VASP Wiki](http://cms.mpi.univie.ac.at/wiki/index.php/VASP_example_calculations) with a large number of examples with all input files.  Below we show how to add a dielectric constant static and frequency calculation into our workflow units.  The simulations could then be executed automatically as normal by pressing the "Compute" tab and "Submit Job".  Exabyte will only display the standard output of each unit but all output files will be present at the end of the simulation accessible on the web or in the terminal window for further analysis.

<img data-gifffer="/images/AddIncar1.gif" />

<img data-gifffer="/images/AddIncar2.gif" />
