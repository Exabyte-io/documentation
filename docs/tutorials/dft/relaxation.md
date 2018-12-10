<!-- by MH -->

This page explains how to run an structural relaxation using density functional theory [[1](#links)]. Relaxation can be run either as a stand-alone workflow or can be prepended to any property calculation.

# Background

The motivation behind using relaxation is explained in detail [here](/models/structural-relaxation). This page focuses on the practical steps and usage.

# Create job

Relaxation prior to property calculations is critical and we will demonstrate its use for a simple Total Energy calculation in this tutorial

To create a new project, click on the "Project" link located in the sidebar/menu on the left. After that, click <i class="zmdi zmdi-plus-circle zmdi-hc-border"></i> button in the top right corner, as shown in the animation below. Every user has a default project and we will use during this tutorial.

Chose the Si structure provided by default for every user. The exact list of materials in your personal database will differ, so you may need to search for the Si structure and select it as shown below:

<img data-gifffer="/images/tutorials/RelaxStep1.gif" />

# Create workflow

Next, choose VASP [[2](#links)] as the simulation engine to be used and choose the "Total Energy" workflow:

Then, to add relaxation as a pre-processor to total energy calculation, expand the <i class="zmdi zmdi-plus-circle zmdi-hc-border"></i> Advanced section to show un-highlighted buttons for Relaxation and k-point convergence. Click on the Relaxation and you will see the relaxation unit added to the workflow.

<img data-gifffer="/images/tutorials/RelaxStep2.gif" />

# Edit input file

To obtain reasonable results for this simulation we, of course, need a k-point density higher than 1x1x1, so click on the "K-points" section of the workflow page and edit the first three entries of the form to be 11 and click "Apply Changes"

<img data-gifffer="/images/tutorials/RelaxStep3.gif" />

Clicking on the "vasp" unit will also show you the input files for the final total energy calculation. Please note that the POSCAR file displayed in this section is just a placeholder and will be overwritten by a CONTCAR file from the VASP relaxation in the earlier part of the workflow.

If you click on the vc-relax, you can see the content of the input files used for the relaxation VASP calculation. The relaxation used is by default always a variable cell shape and size relaxation allowing the atom positions to relax.

<img data-gifffer="/images/tutorials/RelaxStep4.gif" />

# Compute parameters

Before submitting the calculation, click on the "Go to Compute" button and examine the compute parameters. The example below shows how to increase the total run time to 15 minutes, the number of cores to 2 cores, and how to turn on email notifications of when the job starts and ends. Click "No" when it asks if you want to save a duplicate material.

<img data-gifffer="/images/tutorials/RelaxStep5.gif" />

# Monitor status

Finally, while the calculation is running you will see a tab for each execution unit in the workflow. You will notice the vc-relax will update in real time as the simulations progress. The graphical interface will show the delta energy between successive self-consistent steps in the DFT calculation for all SCF steps and all ionic displacements of the atoms. The text based output of VASP also updates in real-time.

<img data-gifffer="/images/tutorials/RelaxStep6.gif" />

# Examine results

When both calculation units are complete, the yellow buttons will have turned green and the "Results" tab will become clickable. You can open "Results" tab to see the final total energy, Fermi energy, and more information about each execution unit.

<img data-gifffer="/images/tutorials/RelaxStep7.gif" />

!!! tip "Tip"
    You can also browse standard output and input files for each unit of the calculation.

# Links

1. [Density Functional Theory, Wikipedia](https://en.wikipedia.org/wiki/Density_functional_theory)
2. [Vienna ab-inito simulation package, Website](https://www.vasp.at/)
