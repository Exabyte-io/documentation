# Electronic Charge Density Mesh Calculation

This tutorial page explains how to calculate and visualize the electronic charge density mesh based on [Density Functional Theory](../../../models-directory/dft/overview.md). We consider crystalline silicon in its standard equilibrium cubic-diamond crystal structure, and use [Quantum ESPRESSO](../../../software-directory/modeling/quantum-espresso/overview.md) as our main simulation engine during this tutorial.

## Create job

Silicon in its cubic-diamond crystal structure is the [default material](../../../materials/default.md) that is shown on [new job creation](../../../jobs-designer/overview.md), unless this default was [changed](../../../entities-general/actions/set-default.md) by the user following [account](../../../accounts/overview.md) creation. If silicon is still the default choice, it will as such be automatically loaded at the moment of the [opening](../../../jobs/actions/create.md) of [Job Designer](../../../jobs-designer/overview.md).

## Choose Workflow

[Workflows](../../../workflows/overview.md) for calculating the electronic density mesh through [Quantum ESPRESSO](../../../software-directory/modeling/quantum-espresso/overview.md) can readily be [imported](../../../workflows/actions/copy-bank.md) from the [Workflows Bank](../../../workflows/bank.md) into the account-owned [collection](../../../accounts/collections.md). This workflow can later be [selected](../../../jobs-designer/actions-header-menu/select-workflow.md) and added to the [Job being created](../../../jobs-designer/workflow-tab.md).

## Set Sampling in Reciprocal Space

It is critical to have a high [k-point density](../../../models/auxiliary-concepts/reciprocal-space/sampling.md) in order to calculate the electronic density with sufficient accuracy and to properly visualize the resulting charge density iso-surfaces.

For Quantum ESPRESSO, the workflow for "Electronic Density Mesh" contains only one [unit](../../../workflows/components/units.md) that produces an output file called **density.xsf**.

We set the size of the grid of k-points to 18 x 18 x 18 in the first workflow unit. This provides a dense enough k-point sampling in order to resolve the fine features present within the electron charge density mesh. The validity of this choice of k-grid size for yielding accurate results of order meV in the final energy can be verified by performing the relevant [convergence study](../../../models/auxiliary-concepts/reciprocal-space/convergence.md).

## Submit Job

Before [submitting](../../../jobs/actions/run.md) the [job](../../../jobs/overview.md), the user should click on the ["Compute" tab](../../../jobs-designer/compute-tab.md) of [Job Designer](../../../jobs-designer/overview.md) and inspect the [compute parameters](../../../infrastructure/compute/parameters.md) included therein.  Silicon is a small structure, so 4 CPUs and 1 minute of calculation runtime should be sufficient.

## Examine Results

Once the computation is complete at the end of Job execution, switching to the [Files tab](../../../jobs/ui/files-tab.md) of [Job Viewer](../../../jobs/ui/viewer.md) will show a listing of the files and directories on the system associated with the electronic density job under consideration.
 
The file that is of interest to us in this case is the aforementioned "density.xsf" output file, containing the results for the electronic charge density computation. 

## Preparing for Visualization

### Open remote Desktop

Following Job execution, we are now ready to visualize graphically the electron density mesh. The next step is to open a [Remote Desktop Connection](../../../remote-connection/remote-desktop.md) so that graphical interface programs for [visualization](../../../software-directory/overview.md#analysis-tools) purposes can be run. Instructions on how to open the [Remote Desktop Interface](../../../remote-connection/remote-desktop.md) starting from our [Web Interface](../../../ui/overview.md) can be found [here](../../../remote-connection/actions/open-desktop.md).

### Open visualization software

The next steps depend on the [analysis and visualization software](../../../software-directory/overview.md#analysis-tools) preferred by the user. We provide below two examples supported on our platform, for the cases of [XCrysden](../../../software-directory/analysis/xcrysden.md) and [VESTA](../../../software-directory/analysis/vesta.md) respectively. Instructions on how to open Applications in the Remote Desktop Environment can be retrieved [in this page](../../../remote-connection/actions-rd/open-app.md).

> If the [default project](../../../jobs/projects.md) was used for the electron charge density calculation, then the location of the "density.xsf" output file referenced in what follows will be: `/home/<username>/data/<username>/<job name>/`. Otherwise, the full path to the file is shown underneath the filename among the list of entries in the [Files tab](../../../jobs/ui/files-tab.md) of [Job Viewer](../../../jobs/ui/viewer.md).

## Visualize Charge Density with XCrysden

The user should first open the [XCrysden](../../../software-directory/analysis/xcrysden.md) analysis and visualization software suite.

Within XCrysden, the user should first go to "File" > "Open", and then navigate to the [directory](../../../data-on-disk/directories.md) where the "density.xsf" electron density file was saved by the previously-executed Job. This opens the file for a visualization of the electron density.

At this stage, the user can adjust the value of charge density to be shown, and toggle the isosurface buttons to display the corresponding data.

## Visualize Charge Density with Vesta

The user can alternatively open the [VESTA](../../../software-directory/analysis/vesta.md) analysis and visualization software package, for achieving the same objective and purpose as with [XCrysden](../../../software-directory/analysis/xcrysden.md) described above.

Within VESTA, first go to file->Open and then browse to the directory where the electron density file (density.xsf) is located. This file should be opened in order to visualize the electron density of the material under investigation.

## Animation

We demonstrate the above-mentioned steps involved in the creation and execution of an electronic charge density mesh computation workflow on silicon, using the [Quantum ESPRESSO](../../../software-directory/modeling/quantum-espresso/overview.md) simulation engine, in the following animation. 

In this particular example, we consider the usage of [VESTA](../../../software-directory/analysis/vesta.md) for visualizing the output contents of the electron charge density file. In the final part of the animation, we adjust the iso-surface value to have the electronic density more visible as yellow iso-surfaces, demonstrating how the electron density within the dimensions of the unit cell is highly concentrated around the second atom in the two-atom [basis](../../../properties-directory/structural/basis.md) of crystalline silicon. The electron densities around the other atoms do not fully show up in this visualization, since their iso-surfaces are truncated by the sides of the unit cell (this truncation shows up as blue planes on the edges of the unit cell).

<div class="video-wrapper">
<iframe class="gifffer" width="100%" height="100%" src="https://www.youtube.com/embed/DXxe6CkTRS4" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>
