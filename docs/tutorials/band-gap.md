<!-- TODO by MH -->

This page explains how to calculate an electronic band gap [[1](#links)] based on density functional theory. We study silicon in the standard diamond-centered cubic structure and use VASP [[2](#links)] as our simulation engine during this tutorial.

!!! Note "Accuracy of the results"
    Please note that this calculation is performed using Density Functional Theory and generalized gradient approximation [[3](#links)] and therefore a systematic under-estimate of the band gap is to be expected. Further modifications to the input files and settings to correctly predict the band gap are possible and explained elsewhere.

# Create job

To create a new job, click on the "Create Job" link located in left-hand sidebar menu.

You will be taken to the "Job wizard" page where you can create a material or choose one that you created and saved before using Materials Designer tab.

<img data-gifffer="/images/FirstJobCreate.gif" />

# Choose band gap workflow

Choose VASP simulation engine. You will see the Total Energy workflow as the default.  Total Energy workflow has one execution unit and provides the band gap value estimate.  Below we demonstrate how to click on the execution unit and modify the k-point density to 11 x 11 x 11 to ensure a dense enough k-mesh for a precise prediction.

<img data-gifffer="/images/BandGapWorkflow.gif" />

# Compute parameters

Next we set up compute parameters for the number of processors and the maximum time limit (walltime). Increasing the number of processors allocated to the job may accelerate the calculation, especially if you have a larger unit cell.  For smaller cells there is likely a certain number of cores at which it becomes inefficient to add more cores to the simulation. Since Si is a small supercell there is no need to increase the number of cores or the walltime.

# Submit job

Click "Submit Job" as shown below. You will be asked if you want to keep a duplicate copy of the material since it has already been saved before. Answer "No" to proceed forward.

<img data-gifffer="/images/BandGapCompute.gif" />

# Monitor status + results

Once the job is submitted it you will be taken to the Job Status page and can monitor the progress of the self-consistent calculation.  When the calculation is completed the color of the Status tab will turn Green and the Results tab will become clickable.  You can scroll through the Results tab to see the results including the indirect band gap found for Si (~0.6 eV).

<img data-gifffer="/images/BandGapResults.gif" />

# Summary

You will notice that we identify both the direct band gap and the indirect band gap.  This calculation is done during the first, self-consistent step of the calculation on the dense k-point mesh.  As you can see the indirect band gap is significantly smaller than the smallest direct band gap.  The calculated value of ~0.6 eV is significantly below the experimental band gap of Silicon of ~1.1 eV but this is expected with the model and method employed.

# Links

1. [Electronic Band gap, Wikipedia](https://en.wikipedia.org/wiki/Band_gap)
2. [Vienna ab-inito simulation package, Website](https://www.vasp.at/)
3. [Density Functional Theory, Wikipedia](https://en.wikipedia.org/wiki/Density_functional_theory)
