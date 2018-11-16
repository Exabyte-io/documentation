# Bandstructure

Electronic bandstructure calculations [^1] can be performed with any appropriate [Workflow](../../workflows/overview.md). The results are portrayed in the [Results Tab](../../jobs/ui/results-tab.md) of [Job Viewer](../../jobs/ui/viewer.md) in the form of a dispersion curve, as illustrated in the graphic below.

![Bandstructure](/images/Properties/bandstructure.png "Bandstructure")

This dispersion plot covers the [desired path](../../workflow-designer/subworkflow-editor/important-settings.md) in the reciprocal space of the Brillouin Zone, with its corresponding Greek letter labels indicating special symmetry points. The energy vertical axis is scaled relative to the [Fermi energy](../scalar/energies.md#fermi-energy) of the material (red dashed line), marking the highest occupied energy level.

The possibility to print or download the dispersion graph in different image formats is offered, under the button labelled with three horizontal bars at the top-right corner of the panel shown above.

## Band Gap Section

Numerical data about the size of the energy **band-gap**, for the case of a semiconducting solid, is also displayed below the graph, in the "Band gap" section. 

The Bang Gap measures the finite energy difference between the highest occupied and lowest unoccupied energy levels in, respectively, the valence and conduction bands of a semiconducting or insulating material [^2]. 

### Direct and Indirect Bang Gaps

Two types of band gap are possible: **direct** and **indirect** [^3]. The former is always computed on our platform, and corresponds to the valence-conduction energy difference as measured at the "Gamma" origin point of the Brillouin Zone of the crystal. However, it is possible that an even smaller difference exists between a valence-conduction pair of states at different k-vectors (crystal momentum), in which case the material is referred to as an "indirect-gap semiconductor". 

Both types of band gaps are returned under the [Results Tab](../../jobs/ui/results-tab.md) as portrayed in the below image. In case the material is of indirect-gap nature, the pair of k-vectors linking the corresponding minimal energy difference is indicated. Otherwise, for direct-gap semiconductors, the two types of gap are presented as being equivalent and being both located across the Gamma point.

![Band Gap Energy](/images/Properties/bang-gap-energy.png "Band Gap Energy")

## Eigenvalues Section

Finally, the list of energy eigenvalue solutions, corresponding to each k-point eigenvector in the reciprocal path under investigation, can be inspected by expanding the "Eigenvalues" section, using the three-dotted button at the bottom of the panel. Information about the weight, net electron spin, and electron occupation numbers for each solution is also included here.

## Links

[^1]: [Wikipedia Electronic band structure, Website](https://en.wikipedia.org/wiki/Electronic_band_structure)

[^2]: [Wikipedia Bang Gap, Website](https://en.wikipedia.org/wiki/Band_gap)

[^3]: [Wikipedia Direct and indirect band gaps, Website](https://en.wikipedia.org/wiki/Direct_and_indirect_band_gaps)
