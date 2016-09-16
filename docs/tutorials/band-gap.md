<!-- TODO by MH -->

This page explains how to run a band gap simulation based on density functional theory. We will be studying silicon in the standard diamond-centered cubic structure and use VASP as our simulation engine during this tutorial.

## Create a new job

To create a new job, click on the "Create Job" link located in the sidebar/menu on the left.

You will be taken to the "Job wizard" page where you can:

- Create a material (or choose one that you created and saved before) using the Materials Designer
- Choose and edit a simulation Workflow
- Setup the Compute Parameters.

<img data-gifffer="/images/FirstJobCreate.gif" />

## Workflow

Upon switching to the VASP simulation engine, the Total Energy workflow will become the default workflow.  Total Energy consists of only one execution unit and will also calculate the band gap.  We show below how to click on the execution unit and modify the k-point density to 11x11x11 to ensure a dense enough k-mesh for an accurate band gap prediction.

<img data-gifffer="/images/BandGapWorkflow.gif" />

## Compute parameters

This tab lets you set up the compute parameters of the number of processors and the maximum time limit for your calculation to be run. Increasing the number of processors allocated to the job may accelerate the calculation if you have a larger unit cell.  For smaller cells there is likely a certain number of cores at which it becomes inefficent to add anymore cores to the simulation. Since Si is a small supercell there is no need to increase the number of cores or the simulation runtime. We just need to click "Submit Job" as shown below. You will be asked if you want to keep a copy of the material since it is already save, but answer "No"

<img data-gifffer="/images/BandGapCompute.gif" />

## Monitoring Status and Results

Once the job is submitted it you will be taken to the Job Status page and can monitor the progress of the self-consitent calculation.  Once the calculation is complete the light on the Status tab will turn Green and the Results tab will become clickable.  You can scroll through the Results tab to see the results including the 0.649 eV indirect band gap found for Si.

<img data-gifffer="/images/BandGapResults.gif" />

!!! Note "DFT-GGA Band Gap error"
    Please note that this calculation is performed using standard [DFT-GGA](https://en.wikipedia.org/wiki/Density_functional_theory) and therefore underprediction of the band gap is to be expected.  Further modifications to the input files and settings to correctly predict the band gap are possible and will be explored in the future.

You will notice that we identify both the direct band gap and the indirect band gap.  This calculation is done during the self-consistent step of the calculation on the dense k-mesh.  As you can see the indirect band gap is significantly smaller than the smallest direct band gap.  The calculated value of 0.649 eV is significantly below the experimental band gap of Silicon of ~1.1 eV but this is expected with these types of potentials and algorithm as noted above.