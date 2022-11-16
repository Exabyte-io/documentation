# Calculate Valence Band Offset

This tutorial page explains how to calculate the [valence band offset](../../../properties-directory/scalar/valence-band-offset.md) (VBO)
based on the potential lineup method[^1][^2][^3] using [Density Functional Theory](../../../models-directory/dft/overview.md).
For this tutorial, we consider a 2D material interface MoS<sub>2</sub>/WS<sub>2</sub> and use
[Quantum Espresso](../../../software-directory/modeling/quantum-espresso/overview.md) as our main simulation engine.
The content of this tutorial was also part of our 2021 webinar *2D Materials and their Electronic Properties*[^4]

!!!note "Simulation engines considered in this tutorial"
    The workflow presented in this tutorial is currently only available for
[Quantum ESPRESSO](../../../software-directory/modeling/quantum-espresso/overview.md).

## Definitions

### Valence Band Offset

The [valence band offset](../../../properties-directory/scalar/valence-band-offset.md) is defined by the relative position
of the valence band on both sides of the interface. This tutorial employs the potential lineup method in order to
determine the valence band offset, which requires the calculation of the macroscopically averaged electrostatic potential
$ \overline{\overline{V}} $. The valence band offset can then be determined via:
$$ \Delta E_{\mathrm{VBO}} = \Delta E_{v} + \Delta V$$
, whereby $\Delta E_{v}$ is usually referred to as the *band structure* term and defined as the difference
of the two valence band maxima referenced to the macroscopically averaged electrostatic potential in each bulk material.
The second term, $\Delta V$, is determined from the lineup of the macroscopically averaged electrostatic potential.


## Choose Materials

When creating the job, the user needs to select **three materials** corresponding to the MoS<sub>2</sub>/WS<sub>2</sub> interface
and the isolated monolayers of both MoS<sub>2</sub> and WS<sub>2</sub>. Each of the structures is expected to be relaxed.

!!!note "Order of Materials"
    The VBO workflow assumes the interface structure to correspond to the first material. 

## Choose Workflow

The [workflow](../../../workflows/overview.md) for calculating the valence band offset can be
[imported](../../../workflows/actions/copy-bank.md) from the [Workflows Bank](../../../workflows/bank.md) into the account-owned
[collection](../../../accounts/collections.md).
This workflow can later be [selected](../../../jobs-designer/actions-header-menu/select-workflow.md) and added to the
[Job being created](../../../jobs-designer/workflow-tab.md).

The workflow contains two subworkflows per material calculating the valence band maximum (via band structure),
macroscopically averaged electrostatic potential, and its minima.
As the system in this tutorial is a heterostructure built of monolayers, determining the value of the macroscopically
averaged electrostatic potential in the region of the monolayer corresponds to finding the minima of $ \overline{\overline{V}} $.
For multilayered heterostructures the problem becomes equivalent of finding plateaus of $ \overline{\overline{V}} $.

The final subworkflow collects all the intermediate results and determines the value of the valence band offset.

## Workflow Settings

For the purpose of this tutorial, we set the size of the grid of k-points to 6 x 6 x 1 for each of the three PW-SCF units
and adjust the k-path to reflect the reduced dimensionality. In addition, one should also adjust the size of the window
for macroscopic averaging. For the present system we set the size to the distance between the sulfur atoms (ca. 5.7 bohr).

## Submit Job

Before [submitting](../../../jobs/actions/run.md) the [job](../../../jobs/overview.md), the user should click on the
["Compute" tab](../../../jobs-designer/compute-tab.md) of [Job Designer](../../../jobs-designer/overview.md) and inspect
the [compute parameters](../../../infrastructure/compute/parameters.md) included therein.

## Examine results

When all [unit](../../../workflows/components/units.md) computations are complete at the end of Job execution, switching
to the [Results tab](../../../jobs/ui/results-tab.md) of [Job Viewer](../../../jobs/ui/viewer.md) will show the results
of the simulation, including the valence band offset as well as the plots of the planar and macroscopic average of
the electrostatic potentials.

### Comparison with Experimental Value

The calculated value of ~0.27 eV for the valence band offset is below the experimental[^5] value of 0.55 eV,
but agrees with previous theoretical results[^6] of 0.32 eV and 0.22 eV, respectively.

## Animation

We demonstrate the above-mentioned steps involved in the creation and execution of a Valence Band Offset workflow in the following animation.

<div class="video-wrapper">
<iframe class="gifffer" width="100%" height="100%" src="https://www.youtube.com/embed/" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

## Links
    
[^1]: A. Baldereschi, S. Baroni, R. Resta, *Phys. Rev. Lett.* **61**, 734 (1988); DOI: [10.1103/PhysRevLett.61.734](https://www.doi.org/10.1103/PhysRevLett.61.734)
[^2]: L. Colombo, R. Resta, S. Baroni, *Phys. Rev. B* **44**, 5572 (1991); DOI: [10.1103/physrevb.44.5572](https://www.doi.org/10.1103/physrevb.44.5572)
[^3]: M. Peressi, N. Binggeli, A. Baldereschi, *J. Phys. D: Appl. Phys.* **31**, 1273-1299 (1998); DOI: [10.1088/0022-3727/31/11/002](https://www.doi.org/10.1088/0022-3727/31/11/002)
[^4]: [2D Materials and their Electronic Properties (Mat3ra YouTube)](https://youtu.be/5T9JMoj62P4)
[^5]: C. Lu, *et. al*, *Phys. Status Solidi A*, 1900544 (2009); DOI: [10.1002/pssa.201900544](https://www.doi.org/10.1002/pssa.201900544)
[^6]: E. Torun, H.P.C. Miranda, A. Molina-Sánchez, L. Wirtz, *Phys. Rev. B* **97**, 245427 (2018); DOI: [10.1103/PhysRevB.97.245427](https://www.doi.org/10.1103/PhysRevB.97.245427)

