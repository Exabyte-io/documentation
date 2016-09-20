<!-- by MH -->

This page explains how to run a zero point energy calculation [[1](#links)] based on density functional theory [[2](#links)]. We will calculate zero point energy for silicon in face-centered cubic structure. We will be studying Silicon in the standard diamond-like face-centered cubic structure and will use VASP [[3](#links)] as our simulation engine.

# Background

The zero point energy is a quantum mechanical property that is related to the uncertainty of the electronic position and momentum at 0K. It is sometimes referred to as a vibration due to the uncertainty principle. It is critical that a well-relaxed structure with converged k-point density is used for zero point energy calculations.

# Create job

Click "Create a Job" in left-hand sidebar on the home page. FCC Si will automatically be loaded as it is the default material.

<img data-gifffer="/images/CreateZPEStructure.gif" />

# Choose workflow

Next go to the workflow tab and select "Zero Point Energy" as the workflow type. As mentioned before, k-point convergence, and structural relaxation are or critical importance for this property, so we add them by expanding the "Advanced" section and adding them both to the workflow. Each individual workflow from within "Advanced Options" is described in detail in their own tutorials. See [kpt-convergence](kpt-convergence) and [relaxation](relaxation).

<img data-gifffer="/images/CreateZPEWorkflow.gif" />

# Examine input file

The unique unit for this tutorial is the vasp_zpe unit. Clicking on it will show the corresponding input files. `IBRION = 5` flag within INCAR enables VASP to run the displacements for the zero point energy calculation.

<img data-gifffer="/images/ShowZPEUnit.gif" />

# Monitor status

As each unit in the workflow is executed, you can monitor progress live by viewing both the output of the executable as well as a graphical representation of the total energy convergence on the "Status" tab under each execution's sub-tab. The animation below shows zero point calculation output for various atom displacements.

<img data-gifffer="/images/TrackZPEResults.gif" />

# Check results

When the execution of all units finished, switching to the "Results" tab and the sub-tab for the final execution unit will have a card titled "Zero Point Energy" that will display the value of zero point energy for the material in question. The larger its value - the more critical it is to include zero point energy in thermodynamic calculations.

<img data-gifffer="/images/ShowZPEResults.gif" />

# Links

1. [Zero-point Energy, Wikipedia](https://en.wikipedia.org/wiki/Zero-point_energy)
2. [Density Functional Theory, Wikipedia](https://en.wikipedia.org/wiki/Density_functional_theory)
3. [Vienna ab-inito simulation package, Website](https://www.vasp.at/)
