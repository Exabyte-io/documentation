# Internal Energy of Materials

The **internal energy** is an important example of a Scalar [Characteristic](/data-structured/overview.md) property of [Materials](/materials/overview.md), and is routinely calculated during the course of material science computational simulations. 

## Cohesive (Chemical) Contribution

THe internal energy embodies primarily the **cohesive (or binding) potential energy** stored internally within the crystal structure of the material under consideration, as a result of the bonding interactions between its constituent atoms. A review of its significance in the general context of solid-state thermodynamics is offered in Ref. [[1](#links)]. 

## Thermal Vibrational Contribution

A second contribution to the internal energy, besides the cohesive chemical component, originates from the thermally-induced **lattice vibrations (phonons)**. These are particularly significant at high temperatures, but in the context of [DFT](/models/dft/overview.md) computations performed at zero temperature they are typically negligible in terms of their energetic contribution, although this contribution remains finite and positive in magnitude. 

This **"Zero-point Energy"** contribution to the internal energy of a zero-temperature solid can still be computed separately, as explained in the forthcoming sections of this page. A theoretical review of lattice vibrations in solid-state physics is available in Ref. [[2](#links)], whereas a description dedicated to the concept of Zero-point Energy can be found in Ref. [[3](#links)].

# Energy Types Computed with DFT

In the context of our platform, the following types of energies can be calculated as part of a [Workflow](/workflows/overview.md) computation, based on the [DFT theoretical framework](/models/dft/overview.md).

## Total Energy

The "Total Energy" refers to the total electronic ground state energy of a material with a fixed lattice (with no thermal vibrations of the atoms), such as can be calculated by a basic "self-consistent field" (scf) computation. 

It effectively corresponds to the aforementioned cohesive energy, stored exclusively inside the chemical bonds defining the crystal structure. 

The total energy is presented to the user, as part of the output of a [Job](/jobs/overview.md), with the appearance displayed below, under the interface of the [Results Tab](/jobs/ui/results-tab.md) of [Job Viewer](/jobs/ui/viewer.md). Its final value is expressed in units of electronVolt (eV).

![Total Energy](/images/total-energy.png "Total Energy")

<div class="clearfix text-center">
    <div class="chart"><i class="zmdi zmdi-square-down zmdi-hc-3x"></i></div>
    <div class="count"><small>kbar</small><h2>0</h2>
    </div>
</div>
 
## Zero Point Energy

The Zero-point Energy due to zero-temperature residual quantum effects on solid lattice vibrations has to be computed separately from a Total Energy job, by performing a [Phonon calculation](../dispersion/phonons.md) on the material under investigation using an appropriate [Workflow](/workflows/overview.md).

It is displayed under the [Results Tab](/jobs/ui/results-tab.md) of the corresponding [Job](/jobs/overview.md) in the following manner, also in units of eV. 

![Zero Point Energy](/images/zero-point-energy.png "Zero Point Energy")

## Fermi Energy

The Fermi Energy marks the highest occupied energy level in the electronic bandstructure of a solid [[4](#links)]. Its value can be estimated with any bandstructure [Workflow](/workflows/overview.md), and it is returned under the [Results Tab](/jobs/ui/results-tab.md) interface with the following appearance, in eV.

![Fermi Energy](/images/fermi-energy.png "Fermi Energy")

# Links 

1. [Cohesion (Bonding) in Solids, Website](https://www.itp.tu-berlin.de/fileadmin/a3233/upload/SS12/TheoFest2012/Kapitel/Chapter_6.pdf)

2. [Lattice Vibrations, Website](https://www.itp.tu-berlin.de/fileadmin/a3233/upload/SS12/TheoFest2012/Kapitel/Chapter7.pdf)

3. [Wikipedia Zero-point energy, Website](https://en.wikipedia.org/wiki/Zero-point_energy)

4. [Wikipedia Fermi Energy, Website](https://en.wikipedia.org/wiki/Fermi_energy)
