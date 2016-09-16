<!-- TODO by MH -->

This page explains how to run a zero point energy simulation based on density functional theory. We will calculate the zero point energy of silicon.

# Background

The zero point energy is a purely quantum mechanical property that is related to the uncertainty of the electrons position and momentum at 0K.  It is sometimes referred to as a vibration due to the uncertainty principle of the inability to define an exact location for each atom.  It is critical that a well-relaxed structure with converged k-point density is used for zero point energy calculations.

# Create new job

On the "Create a Job" from the sidebar on the home page Si will automatically be loaded as it is the default material.  We will use the default material for this tutorial

<img data-gifffer="/images/CreateZPEStructure.gif" />

# Create Workflow

Next go to the workflow tab and select "Zero Point Energy" as the workflow type.  As mentioned above, k-point convergence, and relaxing the structure is critical for this property, so we will add them by expanding the "Advanced" section and adding them both to the workflow units.  Each individual workflow is described in detail in their own tutorials on [kpt-convergence](kpt-convergence) and [relaxation](relaxation).

<img data-gifffer="/images/CreateZPEWorkflow.gif" />

# Examine Input file

The unique unit for this tutorial is the vasp_zpe unit.  Clicking on that unit will show the input files for that calculation.  The "IBRION=5" is the key for VASP to run the displacements for the zero point energy calculation.

<img data-gifffer="/images/ShowZPEUnit.gif"  />

# Monitor Status

As each workflow is executing, you can monitor it's progress live by monitoring both the output of the executable as well as a graphical representation of the total energy convergence on the Status tab under each execution's sub-tab.  The animated GIF below shows the zero point calculation unit of calculations of the total energy of various atom displacements

<img data-gifffer="/images/TrackZPEResults.gif" />

# Check Results

When all units are complete, switching to the Results tab and the sub-tab for the final execution unit will have a card titled "Zero Point Energy" that will display to zero point energy of the material.  The larger the energy the more critical it is to incldue the zero point energy in your thermodynamic calculations.

<img data-gifffer="/images/ShowZPEResults.gif" />