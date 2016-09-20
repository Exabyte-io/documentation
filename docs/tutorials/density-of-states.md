<!-- by MH -->

This page explains how to calculate electronic density of states [[1](#links)] using density functional theory. We study silicon in the standard diamond-centered cubic structure and use Quantum ESPRESSO [[2](#links)] as our simulation engine during this tutorial.

!!! Note "Accuracy of the results"
    Please note that this calculation is performed using Density Functional Theory and generalized gradient approximation [[3](#links)] which is known to under-estimate the energy of unoccupied electronic states.

# Create job

Si is the default material, so if you choose "Create a Job" from the sidebar on the home page Si will automatically be loaded.

<img data-gifffer="/images/BandStep1.gif" />

# Choose workflow

Density of states is calculated in conjunction with band structure calculation so under workflow chose the "Bandstructure + DOS" for either Quantum Espresso.

Click on the animation below to view:

<img data-gifffer="/images/DOSStep2.gif" />

## Adjust kpoints

It is critical to have a high sampling in reciprocal cell (high k-point density) to give enough detail to calculate an accurate density of states.

In QuantumEspresso, the band structure + DOS workflow has 5 units.  The first unit specifies the settings for the self-consistent calculation of the eigenvalues and wave functions.  The second unit calculation is a non self-consitent calculation using the wave functions and charge density of the previous calculation. Subsequent calculations calculate the density of states and also the projection of those states for partial density of states analysis

We set the kpoint density to 11x11x11 in the first workflow unit to provide sufficient density for the second non-consistent calculation step of the band structure. <!-- TODO: set kpoint grid for the 4rth, non-self-consistent calculation, explain why it is beneficial -->

<img data-gifffer="/images/DOSStep3.gif" />

# Submit job

Before submitting the calculation, click on the "Go to Compute" button and examine the compute parameters.  This is a small structure so 1 core and 5 minutes are sufficient.  Click "No" when it asks if you want to save a duplicate material.

<img data-gifffer="/images/DOSStep4.gif" />

# Monitor status

As each unit in the workflow is executing, you can monitor its progress live by viewing both the output of the executable as well as a graphical representation of the total energy convergence on the Status tab under each execution's sub-tab.

<img data-gifffer="/images/DOSStep5.gif" />

# Examine results

When all 5 units are complete, switching to the Results tab and the sub-tab for the final execution unit will show the density of states as well as the partial density of states due to each atom in the structure as well as their s and p electron-like character.  By moving your cursor along each data series it will highlight which element electronic character that data series corresponds to.

<img data-gifffer="/images/DOSStep6.gif" />

# Links

1. [Electronic Density of States, Wikipedia](https://en.wikipedia.org/wiki/Density_of_states)
2. [Quantum ESPRESSO, Website](http://www.quantum-espresso.org/)
3. [Density Functional Theory, Wikipedia](https://en.wikipedia.org/wiki/Density_functional_theory)
