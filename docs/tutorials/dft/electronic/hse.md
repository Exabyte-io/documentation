# HSE Calculations

We discuss in the present tutorial those aspects of the calculation of [electronic structure properties](overview.md) which are specific to the implementation of the **HSE (Heyd-Scuseria-Ernzerhof)** [exchange-correlation functional](../../../models-directory/dft/parameters.md#functional), a special class of [Hybrid Functionals](../../../models-directory/dft/parameters.md#hybrid-functionals).

## Band Gap Calculations

Here, we will explain how to compute the [electronic band gap](../../../properties-directory/non-scalar/band-gaps.md) of crystalline silicon using the [VASP](../../../software-directory/modeling/vasp/overview.md) modeling engine. The increased [precision](../../../methods/precision.md) of Hybdrid Functionals in predicting [material properties](../../../properties/overview.md) of interest such as band gaps will hence be demonstrated. 
 
The instructions presented herein complement the general discussion introduced in a [separate tutorial](band-gap.md). The reader is referred to this latter page for an outline of the general procedure for band-gap computations using DFT, whereas only HSE-specific aspects will be reviewed throughout the remainder of the present page.

## Workflow for HSE Calculation with VASP

Advanced instructions on how to perform an HSE band structure calculation using [VASP](../../../software-directory/modeling/vasp/overview.md) can be retrieved under Refs. [^1],[^2]. 

For the sake of this brief introduction, it suffices to know that a VASP [Workflow](../../../workflows/overview.md) to compute the band-gap of semiconducting materials using HSE is composed of the following [subworkflow](../../../workflows/components/subworkflows.md) steps.

1. Standard self-consistent field (scf) calculation of the energy eigenvalues and wave functions, which includes the HSE [Refiner](../../../models-directory/dft/parameters.md#refiners) as set under the [Subworkflow Editor Interface](../../../workflow-designer/subworkflow-editor/overview-tab.md#refiners).

2. Self-consistent Hartree-Fock/HSE calculation, again with the HSE [Refiner](../../../models-directory/dft/parameters.md#refiners) activated.

3. Extraction of the [k-points](../../../models/auxiliary-concepts/reciprocal-space/sampling.md) in the Symmetry-irreducible wedge of the Brillouin Zone (IBZ) in [reciprocal space](../../../models/auxiliary-concepts/reciprocal-space.md).

4. Final HSE band structure computation, using the wave functions and charge density calculated in the previous steps.

## Copy HSE Workflow from Bank

[Workflows](../../../workflows/overview.md) for calculating the [band gap](../../../properties-directory/non-scalar/band-gaps.md) through HSE, as implemented under [VASP](../../../software-directory/modeling/vasp/overview.md), can readily be [imported](../../../workflows/actions/copy-bank.md) from the [Workflows Bank](../../../workflows/bank.md) into the account-owned [collection](../../../accounts/collections.md). The user should [search](../../../entities-general/actions/search.md) for the string "D7-HSR-BS-BG-DOS" under the Workflows Bank dialog when looking for the relevant HSE-based band-gap workflow.

This workflow can later be [selected](../../../jobs-designer/actions-header-menu/select-workflow.md) and added to the [Job being created](../../../jobs-designer/overview.md). The same procedure as in the [general band-gap computation tutorial](band-gap.md) can otherwise be followed.

!!!warning "Computational Cost"
    The computational cost of HSE calculations is significantly higher than for more basic methods in [DFT](../../../models-directory/dft/overview.md) such as the [Generalized Gradient Approximation](../../../models-directory/dft/parameters.md#subtype). We thus recommend to allow for more [CPU cores and/or walltime](../../../infrastructure/compute/parameters.md) as appropriate for the system under investigation.

## Examine results

When the computation is complete at the end of Job execution, switching to the [Results tab](../../../jobs/ui/results-tab.md) of [Job Viewer](../../../jobs/ui/viewer.md) will show the results of the simulation, including the indirect band gap found for silicon of around 1.14 eV.

### Comparison with Experimental Value

The calculated value of 1.14 eV for the indirect band gap of silicon is in much better agreement with the experimental value for this material (1.17 eV [^3]) than the alternative case of the [Generalized Gradient Approximation](../../../models-directory/dft/notes.md#accuracy-limits-of-the-generalized-gradient-approximation) (GGA), whose shortcomings are assessed in the [other tutorial page](band-gap.md). 

This provides an example of how HSE can result in improved precision in the estimation of important material properties than more traditional approaches within [DFT](../../../models-directory/dft/overview.md).

## Animation

We demonstrate the steps involved in the creation and execution of a HSE Band Gap computation workflow on silicon, using the [VASP](../../../software-directory/modeling/vasp/overview.md) simulation engine, in the following animation.

<div class="video-wrapper">
<iframe class="gifffer" width="100%" height="100%" src="https://www.youtube.com/embed/IXshoTGLJcE" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

## Links

[^1]: [Hartree-Fock (HF) type and hybrid functional calculations, Official VASP Manual](https://cms.mpi.univie.ac.at/vasp/vasp/Hartree_Fock_HF_type_hybrid_functional_calculations.html)
[^2]: [Si HSE bandstructure, VASP Wiki Tutorial](https://cms.mpi.univie.ac.at/wiki/index.php/Si_HSE_bandstructure)
[^3]: [Accessible computational materials design with high fidelity and high throughput, Article](https://arxiv.org/pdf/1807.05623.pdf)
