# Bandstructure

Electronic bandstructure calculations [[1](#links)] can be performed with any appropriate [Workflow](../../workflows/overview.md). The results are portrayed in the [Results Tab](../../jobs/ui/results-tab.md) of [Job Viewer](../../jobs/ui/viewer.md) in the form of a dispersion curve, as portrayed in the graphic below.

![4 jobs results](/images/4_jobs_results.png "4 jobs results")

This dispersion plot covers the [desired path](/workflow-designer/subworkflow-editor/important-settings.md) in the reciprocal space of the Brillouin Zone, with its corresponding Greek letter labels indicating special symmetry points. The energy vertical axis is scaled relative to the [Fermi energy](../scalar/energies.md#fermi-energy) of the material (red dashed line), marking the highest occupied energy level.

The possibility to print or download the dispersion graph in different image formats is offered, under the button labelled with three horizontal bars at the top-right corner of the panel shown above.

## Band gap section

Numerical data about the size of the [energy band-gap](../scalar/energies.md#band-gap-energy), for the case of a semiconducting solid, is also displayed below the graph, in the "Band gap" section. This information is available for both the direct band-gap at the Gamma origin point, and for the indirect band-gap between the indicated valence and conduction k-points.

## Eigenvalues section

Finally, the list of energy eigenvalue solutions, corresponding to each k-point eigenvector in the reciprocal path under investigation, can be inspected by expanding the "Eigenvalues" section, using the three-dotted button at the bottom of the panel. Information about the weight, net electron spin, and electron occupation numbers for each solution is also included here.

# Links

1. [Wikipedia Electronic band structure, Website](https://en.wikipedia.org/wiki/Electronic_band_structure)
