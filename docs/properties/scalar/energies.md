# Internal Energy of Materials

The **internal energy** is an important example of a Scalar [Characteristic](/data-structured/overview.md) property of [Materials](/materials/overview.md), and is routinely calculated during the course of material science computational simulations. 

## Cohesive (Chemical) Contribution

THe internal energy embodies primarily the **cohesive (or binding) potential energy** stored internally within the crystal structure of the material under consideration, as a result of the bonding interactions between its constituent atoms. A review of its significance in the general context of solid-state thermodynamics is offered in Ref. [[1](#links)]. 

## Thermal Vibrational Contribution

A second contribution to the internal energy, besides the cohesive chemical component, originates from the thermally-induced **lattice vibrations (phonons)**. These are particularly significant at high temperatures, but in the context of [DFT](/models/dft/overview.md) computations performed at zero temperature they are typically negligible in terms of their energetic contribution, although this contribution remains finite and positive in magnitude. 

This **"Zero-point Energy"** contribution to the internal energy of a zero-temperature solid can still be computed separately, as explained in the forthcoming sections of this page. A theoretical review of lattice vibrations in solid-state physics is available in Ref. [[2](#links)], whereas a description dedicated to the concept of Zero-point Energy can be found in Ref. [[3](#links)].

# Energy Types

In the context of our platform, the following types of energies are available and can be calculated as part of a [Workflow](/workflows/overview.md) computation.

## Total Energy

The "Total Energy" refers to the total electronic ground state energy of a material with a fixed lattice (with no thermal vibrations of the atoms), such as can be calculated by a basic "self-consistent field" (scf) computation. 

It effectively corresponds to the aforementioned cohesive energy, stored exclusively inside the chemical bonds defining the crystal structure. 

The total energy is presented to the user, as part of the output of a [Job](/jobs/overview.md), with the appearance displayed below, under the interface of the [Results Tab](/jobs/ui/results-tab.md) of [Job Viewer](/jobs/ui/viewer.md). Its final value is expressed in units of electronVolt (eV).

![Total Energy](/images/total-energy.png "Total Energy")


<!---
<div class="clearfix text-center">
    <div class="chart"><i class="zmdi zmdi-square-down zmdi-hc-3x"></i></div>
    <div class="count"><small>kbar</small><h2>-8.222</h2>
    </div>
</div>
--->
 
## Zero Point Energy

The Zero-point Energy due to zero-temperature residual quantum effects on solid lattice vibrations has to be computed separately from a Total Energy job, by performing a [Phonon calculation](../non-scalar/phonons.md) on the material under investigation using an appropriate [Workflow](/workflows/overview.md).

It is displayed under the [Results Tab](/jobs/ui/results-tab.md) of the corresponding [Job](/jobs/overview.md) in the following manner, also in units of eV. 

![Zero Point Energy](/images/zero-point-energy.png "Zero Point Energy")

## Fermi Energy

The Fermi Energy marks the highest occupied energy level in the electronic bandstructure of a solid [[4](#links)]. Its value can be estimated with any bandstructure [Workflow](/workflows/overview.md), and it is returned under the [Results Tab](/jobs/ui/results-tab.md) interface with the following appearance, in eV.

![Fermi Energy](/images/fermi-energy.png "Fermi Energy")

## Band Gap Energy

The Bang Gap measures the finite energy difference between the highest occupied and lowest unoccupied energy levels in, respectively, the valence and conduction bands of a semiconducting or insulating material [[5](#links)]. It is also returned as part of a bandstructure [Workflow](/workflows/overview.md) computation.

### Direct vs Indirect Band Gaps

Two types of band gap are possible: **direct** and **indirect** [[6](#links)]. The former is always computed on our platform, and corresponds to the valence-conduction energy difference as measured at the "Gamma" origin point of the Brillouin Zone of the crystal. However, it is possible that an even smaller difference exists between a valence-conduction pair of states at different k-vectors (crystal momentum), in which case the material is referred to as an "indirect-gap semiconductor". 

Both types of band gaps are returned under the [Results Tab](/jobs/ui/results-tab.md) as portrayed in the below image. In case the material is of indirect-gap nature, the pair of k-vectors linking the corresponding minimal energy difference are indicated. Otherwise, for direct-gap semiconductors, the two types of gap are presented as being equivalent and being both located across the Gamma point.

![Band Gap Energy](/images/bang-gap-energy.png "Band Gap Energy")


# Links 

1. [Cohesion (Bonding) in Solids, Website](https://www.itp.tu-berlin.de/fileadmin/a3233/upload/SS12/TheoFest2012/Kapitel/Chapter_6.pdf)

2. [Lattice Vibrations, Website](https://www.itp.tu-berlin.de/fileadmin/a3233/upload/SS12/TheoFest2012/Kapitel/Chapter7.pdf)

3. [Wikipedia Zero-point energy, Website](https://en.wikipedia.org/wiki/Zero-point_energy)

4. [Wikipedia Fermi Energy, Website](https://en.wikipedia.org/wiki/Fermi_energy)

5. [Wikipedia Bang Gap, Website](https://en.wikipedia.org/wiki/Band_gap)

6. [Wikipedia Direct and indirect band gaps, Website](https://en.wikipedia.org/wiki/Direct_and_indirect_band_gaps)

