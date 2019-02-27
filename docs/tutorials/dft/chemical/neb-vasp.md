# Calculate Reaction Profile Using the Nudged Elastic Band (NEB) method

This tutorial page explains how to calculate the energy reaction profile and activation barrier for the multi-dimensional energy space of chemical reactions via the **Nudged Elastic Bands (NEB) method**, by making use of the [interpolated sets](../../../materials-designer/header-menu/advanced/interpolated-set.md) introduced in a [separate tutorial](../../materials/interpolated-sets.md). 

We consider the example of a one-dimensional, three-atom molecule of Hydrogen (H3) throughout the present tutorial, and shall be making use of [VASP](../../../software-directory/modeling/vasp/overview.md) as the main simulation engine. 

Only the aspects of NEB calculations which are specific to VASP will be reviewed here. For a more general introduction to how such calculations are performed and defined on our platform, the reader is referred to [this alternative tutorial page](neb-qe.md).

## Workflow Structure

VASP and Quantum ESPRESSO work differently with regards to NEB computations for generating an energy profile along a chemical reaction path, using equidistant image structures along the path constituting the interpolated set. General instructions on how NEB is implemented under VASP can be found in Ref. [^1].

In general, within VASP the input geometries of the images are interpolated automatically between the geometries of the initial and the final states. Hence there is no need to generate an interpolated set of images manually.

Most importantly, VASP expects there to be a group of pre-existing [set folders](../../../entities-general/sets.md) within the account-owned [collection](../../../accounts/collections.md) of materials named "00" (initial) to "0N" (final), each containing the POSCAR structure file for each of the N images constituting the interpolated set under consideration. These sets are generated automatically on our platform, as explained in what follows.
 
We describe now the overall structure of the [Workflow](../../../workflows/overview.md) used for executing NEB calculations on our platform via [VASP](../../../software-directory/modeling/vasp/overview.md), which is composed of three main [subworkflow](../../../workflows/components/subworkflows.md) operations.

### 1. Calculate Initial/Final Total Energies

The first subworkflow step consists in executing a pair of self-consistent field (SCF) ground-state energy computations with VASP, in order to extract the [total energies](../../../properties-directory/scalar/total-energy.md) for both the initial and final image structures within the interpolated set.

The total desired number of intermediate NEB images can be customized here, under the ["Important Settings" Tab](../../../workflow-designer/subworkflow-editor/important-settings.md) of the [Workflow Designer Interface](../../../workflow-designer/overview.md).
 
### 2. Prepare Directories 

The second subworkflow runs a [shell script](../../../software-directory/scripting/shell/overview.md) which prepares the aforementioned directories necessary to run a VASP NEB calculation. This script first puts the initial POSCAR structure file into a set directory named "00", the final one into "0N", and the remaining intermediate images in "01" to "0(N-1)". 

The outputs of the previous subworkflow on the SCF calculations applied to the initial and final images are here copied into the initial (00) and final (0N) directories respectively.

### 3. Nudged Elastic Band (NEB) Calculation

The third and final subworkflow executes the NEB computation itself through VASP. We note the following two important input parameters within the VASP "INCAR" input script:

- "IMAGES" defines the number of interpolated image geometries between the initial and final states within the interpolated set. This tag is documented in detail in Ref. [^2]. 

- "SPRING" defines the spring constant, in eV/Ang^2, between the images. A negative value turns on nudging.

Additional information on further possible input parameters available for VASP NEB calculations can be retrieved in Ref. [^3].

Under the ["Important Settings" Tab](../../../workflow-designer/subworkflow-editor/important-settings.md) of the [Workflow Designer Interface](../../../workflow-designer/overview.md), the number of intermediate NEB images should be set to the same value as the one selected previously in the first subworkflow. We also remind the reader that the size of the [grid of reciprocal k-points (kgrid)](../../../models/auxiliary-concepts/reciprocal-space/sampling.md) should be set to 1 x 1 x 1 for the case of chemical molecules such as those considered in the present tutorial.                                              

## Create and Submit Job

The same set of instructions as in the [alternative NEB tutorial](neb-qe.md#create-job-and-choose-workflow) should now be followed for [importing](../../../workflows/actions/copy-bank.md) the relevant VASP NEB workflow from the [bank](../../../workflows/bank.md) into the account-owned [collection](../../../accounts/collections.md), and for later [selecting](../../../jobs-designer/actions-header-menu/select-workflow.md) it into the new [Job](../../../jobs/overview.md) being [designed](../../../jobs-designer/overview.md).

!!!warning "Restrictions on number of computing cores"
    The number of cores on which VASP is run for NEB purposes has to be an integer multiple of the total number of images.

## Animation

We demonstrate the above-mentioned steps involved in the creation and execution of an NEB-based reaction energy profile computation on H3 molecules using the [VASP](../../../software-directory/modeling/vasp/overview.md) simulation engine in the following animation. 

Here, we have made use of 10 intermediate images. It can be deduced from the final results for the energy reaction profile, available under the [Results tab](../../../jobs/ui/results-tab.md) of [Job Viewer](../../../jobs/ui/viewer.md), that the size of the activation barrier in this case is of 0.2 eV, in agreement with the outcome of the [other NEB Tutorial](neb-qe.md).

<div class="video-wrapper">
<iframe class="gifffer" width="100%" height="100%" src="https://www.youtube.com/embed/CpFqp85v4cQ" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

## Links

[^1]: [TS search using the NEB Method, Official VASP Documentation](https://cms.mpi.univie.ac.at/wiki/index.php/TS_search_using_the_NEB_Method)

[^2]: [Instructions on how to generate Images, Official VASP Documentation](https://cms.mpi.univie.ac.at/wiki/index.php/IMAGES)

[^3]: [Transition State Theory: Nudged Elastic Band with VASP, University of Texas Website](http://theory.cm.utexas.edu/vtsttools/neb.html)
