<!-- TODO by MH -->

This page explains how to calculate electronic band structure [[1](#links)] based on density functional theory. We will be studying Silicon in the standard diamond-like face-centered cubic structure and will use VASP [[2](#links)] as our simulation engine.

!!! Note "Accuracy of the results"
    Please note that this calculation is performed using standard Density Functional Theory [[3](#links)] and therefore underprediction of the energy of unoccupied electronic states is expected. Further modifications to the input files and settings to correctly predict the band gap are possible and will be explored later.

# Create job

Silicon in face-centered cubic structure is the default material that is shown on new job initialization. Therefore, if you select "Create a Job" from left-hand sidebar, it will automatically be loaded.

<img data-gifffer="/images/BandStep1.gif"/>

# Choose workflow

Under workflow chose VASP as simulation engine and then "Bandstructure" for the workflow.

<img data-gifffer="/images/BandStep2.gif"/>

## Adjust kpoints

It is critical to have a high k-point density in order to resolve enough details for the band structure plot.

The band structure workflow has 2 units.  The first unit specifies the settings for the self-consistent calculation of the eigenvalues and wave functions.  The second unit calculation is a non self-consitent calculation using the wave functions and charge density of the previous calculation.

We set the kpoint density to 11 x 11 x 11 in the first workflow unit to provide sufficient density for the second non-consistent calculation step of the band structure.  In addition we also apply the recommended k-point path to effectively sample the electronic states based on the symmetry of the crystal.

<img data-gifffer="/images/BandStep3.gif"/>

# Submit job

Before submitting the job, click on the "Compute" tab and examine compute parameters.  This is a small structure so 1 CPU and 5 minutes are sufficient.  Click "No" when asked if you want to save a duplicate material.

<img data-gifffer="/images/BandStep4.gif"/>

# Monitor status

As each unit is being executed, you can monitor progress in real-time by viewing both standard output and the graph of the total energy convergence on the "Status" tab.

<img data-gifffer="/images/BandStep5.gif"/>

# Examine Results

When both units are complete, switching to the Results tab and the sub-tab for the final execution unit will show the band structure of silicon as a function of the special k-point paths chosen.

<img data-gifffer="/images/BandStep6.gif"/>

# Links

1. [Electronic Bandstructure, Wikipedia](https://en.wikipedia.org/wiki/Electronic_band_structure)
2. [Vienna ab-inito simulation package, Website](https://www.vasp.at/)
3. [Density Functional Theory, Wikipedia](https://en.wikipedia.org/wiki/Density_functional_theory)
