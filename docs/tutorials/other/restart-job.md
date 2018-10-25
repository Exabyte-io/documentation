<!-- by MH -->

This page explains how to restart a calculation from the results of a previous calculation.  We will use the "Recalculate Bands" workflow as an example to restart from a previous "Electronic Density Mesh" simulation. The tutorial for "Electronic Density Mesh" is [here](../dft/electronic-density-mesh.md)

# Choose restart

On the "Create Job" page, choose VASP as your simulation engine. Next expand the "Advanced" select and click on the dropdown for "Restart from".  Find the job that you previously ran an "Electronic Density Mesh" workflow on and select that job.  Next go to the dropdown workflow menu and select "Recalculate Bands"

<img data-gifffer="/images/RestartSelect.gif" />

# Compute parameters

Next we got to "Compute" tab, but no changes are necessary here so click the "Submit Job" button to run the job.

<img data-gifffer="/images/RestartSubmit.gif" />

# Monitor status + results

This type of job is a non self-consistent simulation that will not take as many steps to execute so the monitor window only shows two steps before completing.  If you click on the "Results" tab you will see that the band structure has been calculated using the previous charge density from an old Electronic Density Mesh simulation.

<img data-gifffer="/images/RestartResults.gif" />
