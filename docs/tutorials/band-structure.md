<!-- TODO by MH -->

This page explains how to run a band structure simulation based on density functional theory. We will be studying silicon in the standard diamond-centered cubic structure and use VASP as our simulation engine during this tutorial.

!!! Note "Accuracy of DFT-GGA Band Structures"
    Please note that this calculation is performed using standard [DFT-GGA](https://en.wikipedia.org/wiki/Density_functional_theory) and therefore underprediction of the energy of unoccupied electronic states expected.  Further modifications to the input files and settings to correctly predict the band gap are possible and will be explored in the future.

# Create new job

Si is the default material, so if you choose "Create a Job" from the sidebar on the home page Si will automatically be loaded.

<img data-gifffer="/images/BandStep1.gif" />

# Create workflow

Under workflow chose VASP as your simulation energy and then "Bandstructure" for the workflow.

<img data-gifffer="/images/BandStep2.gif" />

## Adjust KPoints

In addition, for electronic properties with a non-self consistent step it is critical to have a high k-point density to give enough detail to calculate an accurate band structure.

In VASP, the band structure workflow has 2 units.  The first unit specifies the settings for the self-consistent calculation of the eigenvalues and wave functions.  The second unit calculation is a non self-consitent calculation using the wave functions and charge density of the previous calculation.

We set the kpoint density to 11x11x11 in the first workflow unit to provide sufficient density for the second non-consistent calculation step of the band structure.  In addition we also apply the recommended k-point path to effectively sample the electronic states based on the symmetry of the crystal.

<img data-gifffer="/images/BandStep3.gif" />

!!! Note: Future automatic high symmetry k-point paths
    Currently we only support the automatic generation of high symmetry k-points for FCC structures.  Support for high symmetry k-point path sampling for band structure calculations of all 14 lattice types will be supported in a future release.

# Submit job

Before submitting the calculation, click on the "Go to Compute" button and examine the compute parameters.  This is a small structure so 1 core and 5 minutes are sufficient.  Click "No" when it asks if you want to save a duplicate material.

<img data-gifffer="/images/BandStep4.gif" />

# Monitoring status

As each workflow is executing, you can monitor it's progress live by monitoring both the output of the executable as well as a graphical representation of the total energy convergence on the Status tab under each execution's sub-tab.

<img data-gifffer="/images/BandStep5.gif" />

# Examining Results

When both units are complete, switching to the Results tab and the sub-tab for the final execution unit will show the band structure of silicon as a function of the special k-point paths chosen.

<img data-gifffer="/images/BandStep6.gif" />