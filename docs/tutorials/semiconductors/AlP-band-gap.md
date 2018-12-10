<!-- by MH -->

This tutorial explain how to calculate an electronic band gap [[1](#links)] based on density functional theory. We study AlP and use VASP [[2](#links)] as our simulation engine using PAW pseudopotentials [[3](#links)], [[4](#links)]with Perdew-Burke-Ernzerhof functionals. [[5](#links)]

!!! Note "Accuracy of the results"
    Please note that this calculation is performed using Density Functional Theory and generalized gradient approximation [[6](#links)] and therefore a systematic under-estimate of the band gap is to be expected. Further modifications to the input files and settings to correctly predict the band gap are possible and explained elsewhere.  We follow-up with a second set of calculations using Hybrid Screened Exchange for more accurate prediction of the band gaps [[7](#links)].

# Import material

To import AlP go to the Materials webpage using the sidebar on the homepage.  Once on the homepage you can click on the cloud icon in the upper right with an embedded down arrow.  In the resulting overlay search enter AlP for Aluminum Phosphide.  After a few seconds the search results will appear.  The F-43m space group option is the lowest energy AlP.  Click on the right side on this line and choose "import".  This will load the material into your database.

<img data-gifffer="/images/tutorials/AlPImport.gif"/>

# Create job

To create a new job, click on the "Create Job" link located in left-hand sidebar menu.

You will be taken to the "Job wizard" page where you can create a material or choose one that you created and saved before using Materials Designer tab.

# Choose band gap workflow

Choose VASP simulation engine. You will see the Total Energy workflow as the default.  Click on the box saying "Total Energy" and select the "Band Gap" workflow to provide the band gap value estimate.  Below we demonstrate how to click on the execution unit and modify the k-point density to ensure a dense enough k-mesh for a band gap prediction.

# Compute parameters

Next we set up compute parameters for the number of processors and the maximum time limit (wall-time). Increasing the number of processors allocated to the job may accelerate the calculation, especially if you have a larger unit cell.  For smaller cells there is likely a certain number of cores at which it becomes inefficient to add more cores to the simulation.  We will use only 2 cores for this simulation.

<img data-gifffer="/images/tutorials/AlPCreate.gif"/>

# Submit job

Click "Save" as shown below. You will be asked if you want to keep a duplicate copy of the material since it has already been saved before. Answer "No" to proceed forward.  To submit the job to the queue click on the check box to the left of your job, then click the "play" button in the upper right corner of the page.  The status of the job will change from "Pre-submission" to "Submitted" to "Active".

<img data-gifffer="/images/tutorials/AlPSubmit.gif"/>

# Monitor status + results

Once the job is submitted it you will be taken to the Job Status page and can monitor the progress of the self-consistent calculation.  When the calculation is completed the color of the Status tab will turn Green and the Results tab will become click-able.  You can scroll through the Results tab to see the results including the indirect band gap found for AlP (1.75 eV).

<img data-gifffer="/images/tutorials/AlPResults.gif"/>

# Summary

You will notice that we identify both the direct band gap and the indirect band gap.  This calculation is done during the first, self-consistent step of the calculation on the dense k-point mesh.  As you can see the indirect band gap is significantly smaller than the smallest direct band gap.  The calculated value of 1.75 eV is significantly below the experimental band gap of Aluminum Phosphide of ~2.45 eV but this is expected with the model and method employed.

# Increasing accuracy with HSE

Hybrid Screened Exchange is a more computationally expensive model to be used within DFT that more accurately predicts the energy of excited state electrons.  To update your calculate the INCAR file below will use HSE based on the last 4 lines of the INCAR file.

```
LWAVE  = .FALSE.
ISMEAR =    0
SIGMA  = 0.05
LORBIT = 11
LHFCALC = .TRUE.
HFSCREEN = 0.2
ALGO = D
TIME = 0.4
```

For AlP if we use HSE with a 15 x 15 x 15 k-point density running for 12 hours on 18 cores, we obtain a predicted band gap of 2.36 eV within 4% error.

# Links

1. [Electronic Band gap, Wikipedia](https://en.wikipedia.org/wiki/Band_gap)
2. [Vienna ab-inito simulation package, Website](https://www.vasp.at/)
3. [PAW Potentials - Blochl](http://journals.aps.org/prb/abstract/10.1103/PhysRevB.50.17953)
4. [PAW Potentials - Kresse](http://journals.aps.org/prb/abstract/10.1103/PhysRevB.59.1758)
5. [PBE Functionals, PDF](http://journals.aps.org/prl/abstract/10.1103/PhysRevLett.77.3865)
6. [Density Functional Theory, Wikipedia](https://en.wikipedia.org/wiki/Density_functional_theory)
7. [Hybrid Screened Exchange, PDF](https://www.vasp.at/index.php/news/36-highlights/68-hse-hybrid-functional)


