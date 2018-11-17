# Electronic Bandstructure

In solid-state physics, the electronic band structure of a material describes the range of energies that an electron within the crystal structure may have (called energy bands) [^1].

## Computation

Electronic bandstructure calculations can be performed with an appropriate [Workflow](../../workflows/overview.md). The results are portrayed in the [Results Tab](../../jobs/ui/results-tab.md) of [Job Viewer](../../jobs/ui/viewer.md) in the form of a **dispersion curve**, as illustrated in the graphic below.

![Bandstructure](/images/Properties/bandstructure.png "Bandstructure")

This dispersion plot covers the [desired path](../../workflow-designer/subworkflow-editor/important-settings.md) in the reciprocal space of the Brillouin Zone, with its corresponding Greek letter labels indicating special symmetry points. The energy along the vertical axis is scaled relative to the [Fermi energy](../scalar/fermi-energy.md) of the material (red dashed line), marking the highest occupied energy level.

The possibility to print or download the dispersion graph in different image formats is offered, under the button labelled with three horizontal bars at the top-right corner of the panel shown above.

## Energy Eigenvalues 

The list of energy eigenvalue solutions, corresponding to each k-point eigenvector in the reciprocal path under investigation, can be inspected by expanding the "Eigenvalues" section, using the three-dotted button at the bottom of the panel. Information about the weight, net electron spin, and electron occupation numbers for each solution is also included here.

## Schema and Example 

The JSON schema and an example representation for this property can be found [here](../../properties/data/list.md#bandstructure).

## Links

[^1]: [Wikipedia Electronic band structure, Website](https://en.wikipedia.org/wiki/Electronic_band_structure)
