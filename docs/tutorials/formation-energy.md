<!-- TODO by MH -->

We will calculate the formation energy of copper oxide (CuO2).

!!! Note "Pre-calculated pseudopotential values"
    Formation energy requires the subtraction of the constituent element total and zero point energies in their standard state.  We have pre-calculated these values at a converged k-point density for all supported pseudopotentials.  These values will automatically be read by the software to eliminate the recalculate them during this working

On the "Create a Job" from the sidebar on the home page Si will automatically be loaded as it is the default material.  The formation of elements is zero so for this test case we will need to import a CuO2 structure from Materials Project.  To import CuO2 go to the sidebar, and select the "Materials" page.  On that page click the cloud button on the upper right of that page for import.  In the search box, put CuO2 and after a few seconds, the entries for CuO2 from the database and Material Project will appear.  Choose the version of CuO2 with the lowest formation energy and click on it.  Then click on the right side of the entry to bring up the option to import the material

<img data-gifffer="/images/ImportCuO2.gif" />

Now that you have imported CuO2 we are ready to use that structure to submit the formation energy calculation.  Go to the "Create Job" page.  If you go to the "Choose A Material" section of the page, if you click on the dropdown menu, CuO2 should be one of your options to select as the material for the simulation.

<img data-gifffer="/images/CreateCuO2.gif" />

Next go to the workflow tab and select "Formation Energy" as the workflow type.  The units displayed as part of this workflow will look similar to a combination of the [kpt-convergence](kpt-convergence) and [relaxation tutorials](relaxation), but will include a couple of extra units after the vc_relax unit used to obtain the elements total and zero point energies and calculate the formation energy.

<img data-gifffer="/images/SetFormationEnergyWorkflow.gif" />

This calculation will take some time to complete due to both k-point convergence and relaxation being run on a supercell with more than just two atoms.  It's important to adjust the parameters for Compute accordingly.  Click on the "Compute" tab and increase the maximum run time limit to 30 minutes and the number of cores to 4.  Also click on your username in the box to turn on email notifications of the jobs status.

<img data-gifffer="/images/IncreaseComputeFormationE.gif" />

As each workflow is executing, you can monitor it's progress live by monitoring both the output of the executable as well as a graphical representation of the total energy convergence on the Status tab under each execution's sub-tab.

<img data-gifffer="/images/FormationEnergyTrackResults.gif" />

When all units are complete, switching to the Results tab and the sub-tab for the final execution unit will have an entry titled "Formation Energy" that will display to formation energy of the material.  The more negative the value, the more stable the material is.  This "Formation Energy" box will also show the constituent element total energy and zero point energies used to calculate the values.

<img data-gifffer="/images/FinalFormationEnergyDetails.gif" />

!!! Note "Formation energy only automated for 2-element compounds currently"
    Currently this workflow only supports formation energy calculation of 2 element compounds, but will be further developed to work for an arbitraty number of elements in the future

