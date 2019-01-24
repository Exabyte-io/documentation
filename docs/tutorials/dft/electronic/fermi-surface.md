# Fermi Surface Calculation

This page explains how to calculate the [Fermi surface](../../../properties-directory/scalar/fermi-energy.md) for metallic copper (Cu) lying in its equilibrium face-centred cubic (fcc) [Bravais Lattice](../../../properties-directory/structural/lattice.md), through the use of [Density Functional Theory](../../../models-directory/dft/overview.md). We will use [Quantum ESPRESSO](../../../software-directory/modeling/quantum-espresso/overview.md) as our simulation engine for this tutorial.

## Create Job and Select Material

The user should start by creating a new [Job](../../../jobs/overview.md), through [opening](../../../jobs/actions/create.md) the [Job Designer Interface](../../../jobs-designer/overview.md). The fcc crystal structure of copper should then be [selected and added](../../../jobs-designer/actions-header-menu/select-materials.md) to the new Job being designed, assuming that this structure is already present among the entries listed in the account-owned [collection](../../../accounts/collections.md) of materials.

## Choose Workflow

[Workflows](../../../workflows/overview.md) for calculating the [band structure](../../../properties-directory/non-scalar/bandstructure.md) of [materials](../../../materials/overview.md) with [Quantum ESPRESSO](../../../software-directory/modeling/quantum-espresso/overview.md) can readily be [imported](../../../workflows/actions/copy-bank.md) from the [Workflows Bank](../../../workflows/bank.md) into the account-owned [collection](../../../accounts/collections.md). This workflow can later be [selected](../../../jobs-designer/actions-header-menu/select-workflow.md) and added to the [Job being created](../../../jobs-designer/workflow-tab.md).

## Set Sampling in Reciprocal Space

It is critical to have a high [k-point density](../../../models/auxiliary-concepts/reciprocal-space/sampling.md) in order to resolve enough details for the Fermi surface plot.

The band structure workflow is composed of two [units](../../../workflows/components/units.md). The first unit specifies the settings for the self-consistent calculation of the energy eigenvalues and wave functions.  The second unit calculation is a non self-consistent calculation using the wave functions and charge density of the previous calculation.

We set the size of the grid of k-points to 18 x 18 x 18 in the first workflow unit. This provides a dense enough k-point sampling in order to resolve the fine features present within the output of the band structure computation. The validity of this choice of k-grid size for yielding accurate results of order meV in the final energy can be verified by performing the relevant [convergence study](../../../models/auxiliary-concepts/reciprocal-space/convergence.md).

## Submit Job

Before [submitting](../../../jobs/actions/run.md) the [job](../../../jobs/overview.md), the user should click on the ["Compute" tab](../../../jobs-designer/compute-tab.md) of [Job Designer](../../../jobs-designer/overview.md) and examine the [compute parameters](../../../infrastructure/compute/parameters.md) included therein.  Copper is a small structure, so 4 CPUs and 1 minute of calculation runtime should be sufficient.

## Examine Final Results

When both [unit](../../../workflows/components/units.md) computations are complete at the end of Job execution, switching to the [Results tab](../../../jobs/ui/results-tab.md) of [Job Viewer](../../../jobs/ui/viewer.md) will show the final [total energy](../../../properties-directory/scalar/total-energy.md), the [Fermi energy](../../../properties-directory/scalar/fermi-energy.md), and more information about each execution unit.

The user can also browse the actual input and output files that are part of the calculation under the [Files Tab](../../../jobs/ui/files-tab.md) of [Job Viewer](../../../jobs/ui/viewer.md).

## Generate File with Fermi Surface Information

Once the simulation is complete, the user should [open](../../../remote-connection/actions/open-terminal.md) a [Web Terminal session](../../../remote-connection/web-terminal.md) in order to create a file that is essential for visualizing the Fermi surface. The calculation of Fermi surface can in general be performed using the `fs.x` code, part of the [Quantum ESPRESSO](../../../software-directory/modeling/quantum-espresso/overview.md) distribution. The resulting file in `.bxsf` format can be read and plotted using the [XCrySDen](../../../software-directory/analysis/xcrysden.md) analysis and visualization software.  

As below, navigate into the directory containing all your simulation results.  Once in the correct simulation directory run the commands in the window below to generate the post-processing bxsf file:

![Generate BXSF File](../../../images/tutorials/GenerateBXSFFile.png "Generate BXSF File")

Finally the user should close the Web Terminal session to return to the original [Web Interface](../../../ui/overview.md) of our platform.

# Start remote desktop

The next step is to open a Remote Desktop Connection to the terminal so that you can run graphical interface programs for visualization.  Underneath the "Terminal" option in the right sidebar you used earlier in the tutorial is a "Remote Desktop" option.

![Remote Desktop](../../../images/tutorials/ChooseRemoteDesktop.png "Remote Desktop")

Select this and a different overlay will appear in your web browser of a graphical user session.

![Start Remote Desktop](../../../images/tutorials/StartRemoteDesktop.png "Start Remote Desktop")

# Open XCrysden

Find and open XCrysden under the "Other" dropdown menu item.

![Other->XCrysden](../../../images/tutorials/RemoteDesktopApps.png "Other->XCrysden")

Within XCrysden, go to file->Open and navigate to the directory where you created the *.bxsf file to open a visualization of the Fermi Surface.

![Visualize Fermi Surface 1](../../../images/tutorials/FermiSurface1.png "Visualize Fermi Surface 1")
![Visualize Fermi Surface 2](../../../images/tutorials/FermiSurface2.png "Visualize Fermi Surface 2")
![Visualize Fermi Surface 3](../../../images/tutorials/FermiSurface3.png "Visualize Fermi Surface 3")
