<!-- TODO by MH -->
This page explains how to run a density of state calculation including partial density of states analysis based on density functional theory. We will be studying silicon in the standard diamond-centered cubic structure and use quantum espresso as our simulation engine during this tutorial.

!!! Note "Accuracy of DFT-GGA Density of States"
    Please note that this calculation is performed using standard [DFT-GGA](https://en.wikipedia.org/wiki/Density_functional_theory) and therefore underprediction of the energy of unoccupied electronic states expected.  Further modifications to the input files and settings to correctly predict the band gap are possible and will be explored in the future.

# Create new job
Si is the default material, so if you choose "Create a Job" from the sidebar on the home page Si will automatically be loaded.

<img data-gifffer="/images/BandStep1.gif" />

# Create workflow

Density of states is calculated in conjunction with band structure calculation so under workflow chose the "Bandstructure + DOS" for either Quantum Espresso.

<img data-gifffer="/images/DOSStep2.gif" />

## Adjust KPoints

In addition, for electronic properties with a non-self consistent step it is critical to have a high k-point density to give enough detail to calculate an accurate density of states.

In QuantumEspresso, the band structure + DOS workflow has 5 units.  The first unit specifies the settings for the self-consistent calculation of the eigenvalues and wave functions.  The second unit calculation is a non self-consitent calculation using the wave functions and charge density of the previous calculation. Subsequent calculations calculate the density of states and also the projection of those states for partial density of states analysis

We set the kpoint density to 11x11x11 in the first workflow unit to provide sufficient density for the second non-consistent calculation step of the band structure.
<img data-gifffer="/images/DOSStep3.gif" />

# Submit job

Before submitting the calculation, click on the "Go to Compute" button and examine the compute parameters.  This is a small structure so 1 core and 5 minutes are sufficient.  Click "No" when it asks if you want to save a duplicate material.

<img data-gifffer="/images/DOSStep4.gif" />

# Monitoring status

As each unit in the workflow is executing, you can monitor it's progress live by monitoring both the output of the executable as well as a graphical representation of the total energy convergence on the Status tab under each execution's sub-tab.

<img data-gifffer="/images/DOSStep5.gif" />

# Examining Results

When all 5 units are complete, switching to the Results tab and the sub-tab for the final execution unit will show the density of states as well as the partial density of states due to each atom in the structure as well as their s and p electron-like character.  By moving your cursor along each data series it will highlight which element electronic character that data series corresponds to.

<img data-gifffer="/images/DOSStep6.gif" />



