# Band Gap 

The Bang Gap measures the finite energy difference between the highest occupied and lowest unoccupied energy levels in, respectively, the valence and conduction bands of a semiconducting or insulating material [^1]. 

## Direct and Indirect Band Gaps

Two types of band gap are possible: **direct** and **indirect** [^2]. The former is always computed on our platform, and corresponds to the valence-conduction energy difference as measured at the "Gamma" origin point of the Brillouin Zone of the crystal.
 
However, it is possible that an even smaller difference exists between a valence-conduction pair of states at different k-vectors (crystal momentum), in which case the material is referred to as an "indirect-gap semiconductor". 

## Computation

Both types of band gaps are returned under the [Results Tab](../../jobs/ui/results-tab.md) as portrayed in the following image, immediately below the main [bandstructure dispersion](bandstructure.md) plot. 

In case the material is of indirect-gap nature, the pair of k-vectors linking the corresponding minimal energy difference is indicated. Otherwise, for direct-gap semiconductors, the two types of gap are presented as being equivalent and being both located across the Gamma point.

![Band Gap Energy](/images/Properties/bang-gap-energy.png "Band Gap Energy")

## Schema and Example 

The JSON schema and an example representation for this property can be found [here](../../properties/data/list.md#band-gaps).

## Links

[^1]: [Wikipedia Bang Gap, Website](https://en.wikipedia.org/wiki/Band_gap)

[^2]: [Wikipedia Direct and indirect band gaps, Website](https://en.wikipedia.org/wiki/Direct_and_indirect_band_gaps)
