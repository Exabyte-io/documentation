# Effective Screening Medium (ESM) Calculation

In the present tutorial, we demonstrate how to create a [Job](../../../jobs/overview.md) in order to extract **potential/charge profiles**, via the [Effective Screening Medium (ESM)](../../../models/auxiliary-concepts/esm.md) approach for simulating **surfaces** and **interfaces** based on [Density Functional Theory](../../../models-directory/dft/overview.md).

We consider a water (H2O) molecule in the present example, and use [Quantum ESPRESSO](../../../software-directory/modeling/quantum-espresso/overview.md) as our main simulation engine during this tutorial.

!!!note "Quantum ESPRESSO version considered in this tutorial"
    The present tutorial is written for Quantum ESPRESSO at versions 5.2.1, 5.4.0, 6.0.0 or 6.3.
    
## Workflow for ESM Calculation with Quantum ESPRESSO

The [Workflow](../../../workflows/overview.md) implementing ESM calculations on our platform through [Quantum ESPRESSO](../../../software-directory/modeling/quantum-espresso/overview.md) is composed of a single main computational [unit](../../../workflows/components/units.md). 

Examples on how ESM is enabled and supported in Quantum ESPRESSO are offered in Ref. [^1]. Here, we will offer a brief review of the most important input keywords, that are required to be included in Quantum ESPRESSO input scripts in the context of ESM calculations.

### Quantum ESPRESSO ESM Input Parameters

#### assume_isolated = 'esm'
 
This parameter is used to perform the calculation assuming the system to be isolated, such as in the cases of a molecule or a cluster, as opposed to regular periodic boundary conditions. 

For polarized or charged slab calculation, the 'esm' option embeds the simulation cell within an effective semi-
infinite medium in the perpendicular direction (along z). Embedding regions can be vacuum or semi-infinite metal electrodes.If between two electrodes, an optional electric field may be applied via the 'esm_efield' keyword described in what follows.

This requires a simulation cell with the $c$ lattice vector along z, normal to the xy plane, with the slab centered around z=0. 

#### esm_bc

This option determines the boundary conditions used for either side of the slab. The available possibilities are listed in [this page](../../../materials-designer/header-menu/advanced/boundary-conditions.md).

#### esm_w

This keyword determines the [position offset](../../../materials-designer/header-menu/advanced/boundary-conditions.md#offset) of the start of the effective screening region, measured relative to the edge of the simulation cell (of total vertical thickness $L_z$). The ESM region begins at (with the slab centered around z=0):

$$
 z = +/- [L_z/2 + esm_w]
$$

#### esm_efield

This other option gives the magnitude of the electric field to be applied between semi-infinite ESM electrodes.

#### fcp_mu

Finally, the `fcp_mu` tag in the Quantum ESPRESSO input script sets the target Fermi energy for the simulation.

### SCF vs Relax ESM Calculations

Two different flavors of ESM workflow calculations are offered on our platform, the first one performing a basic ground state energy self-consistent field (SCF) calculation, whereas the second affording also for the [relaxation](../../../workflows/addons/structural-relaxation.md) of the inter-atomic forces, within the structure under consideration, during the course of the ESM computation. The latter option is enabled via the  `calculation = 'relax'` Quantum ESPRESSO input tag.

## Prepare Water Molecule

The structure of a water molecule (H2O) can readily be [imported](../../../materials/actions/copy-bank.md) from the [Materials Bank](../../../materials/bank.md) into the account-owned [collection](../../../accounts/collections.md) of materials, if it is not already present there.  

This water structure should then be [imported](../../../materials-designer/header-menu/input-output/import.md) into the [Materials Designer](../../../materials-designer/overview.md) interface, in order to edit its [boundary conditions](../../../materials-designer/header-menu/advanced/boundary-conditions.md) via the corresponding option in the ["Advanced" menu](../../../materials-designer/header-menu/advanced.md). 

In the present example, we shall opt for the "Vacuum-Slab-Vacuum" (bc1) boundary condition option. The vacuum boundaries should be shifted by half of the lattice $c$ constant via the "Offset" option of the ["Set Boundary Conditions" dialog](../../../materials-designer/header-menu/advanced/boundary-conditions.md).

After finishing setting up the boundary conditions for our water molecule structure, the user should [Save](../../../materials-designer/header-menu/input-output/save.md) the changes to the structure within the account-owned materials collection, and then exit Materials Designer.

## Create Job

The user should then open an instance of the [Job Designer interface](../../../jobs-designer/overview.md) in order to create a new simulation [Job](../../../jobs/overview.md), via the corresponding option in the main [left-hand sidebar](../../../ui/left-sidebar.md#create-job) of our [Web interface](../../../ui/overview.md).

## Import Water Molecule in Job Designer

The previously-created water structure should now be [selected and imported](../../../jobs-designer/actions-header-menu/select-materials.md) via the ["Materials" tab](../../../jobs-designer/materials-tab.md) of [Job Designer](../../../jobs-designer/overview.md), to be made the main simulation sample structure.

## Copy ESM Workflow from Bank

[Workflows](../../../workflows/overview.md) for performing [Effective Screening Medium (ESM)](../../../models/auxiliary-concepts/esm.md) computations with [Quantum ESPRESSO](../../../software-directory/modeling/quantum-espresso/overview.md) can readily be [imported](../../../workflows/actions/copy-bank.md) from the [Workflows Bank](../../../workflows/bank.md) into the account-owned [collection](../../../accounts/collections.md). 

This workflow can later be [selected](../../../jobs-designer/actions-header-menu/select-workflow.md) and added to the [Job being created](../../../jobs-designer/overview.md). 

## Change Important Settings

Opening ["Important Settings"](../../../workflow-designer/subworkflow-editor/important-settings.md) within the [Workflow Tab](../../../jobs-designer/workflow-tab.md) allows the user to customize the following Boundary Conditions-related settings:

- Type of boundary conditions
- Offset
- Electric Field
- Target Fermi Energy 

In the present example, we shall keep the previously-defined 'bc1' boundary conditions, and leave the remaining three options to their default zero values.

In addition, the user should set the size of the grid of [k-points](../../../models/auxiliary-concepts/reciprocal-space/sampling.md) to 2x2x2 in this case, also under "Important Settings".

## Submit Job

Before [submitting](../../../jobs/actions/run.md) the [job](../../../jobs/overview.md), the user should click on the ["Compute" tab](../../../jobs-designer/compute-tab.md) of [Job Designer](../../../jobs-designer/overview.md) and examine the [compute parameters](../../../infrastructure/compute/parameters.md) included therein.  Water is a small structure, so 4 CPUs and 1 minute of calculation runtime should be sufficient.

## Examine Final Results

### Potential Energy Profile

When the ESM computation is complete at the end of Job execution, switching to the [Results tab](../../../jobs/ui/results-tab.md) of [Job Viewer](../../../jobs/ui/viewer.md) will show the **Potential Energy profile** of our water-vacuum system, plotted as an energy curve (in eV) as a function of the distance along the vertical perpendicular direction (the "z" coordinate), away from the central water slab. The "local" and "Hartree" contributions to the Potential energy are also given separately.

### Charge Density Profile

Similarly, the Charge Density profile is also displayed under the [Results tab](../../../jobs/ui/results-tab.md), showing the evolution of the charge density (in electron charge units/Angstrom) as a function of the same vertical "z" coordinate mentioned previously.

## Animation

We demonstrate the above-mentioned steps involved in the creation and execution of an ESM computation on a water molecule using the [Quantum ESPRESSO](../../../software-directory/modeling/quantum-espresso/overview.md) simulation engine in the following animation. Here, we shall make use of the "Relax" variant of the Quantum ESPRESSO ESM workflow.

<div class="video-wrapper">
<iframe class="gifffer" width="100%" height="100%" src="https://www.youtube.com/embed/7VskTArfynU" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

## Links

[^1]: [Quantum ESPRESSO ESM Examples, Official GitHub repository](https://github.com/QEF/q-e/tree/master/PW/examples/ESM_example)
