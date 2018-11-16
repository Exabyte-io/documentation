# Total Energy

The "Total Energy" refers to the total electronic ground state energy of a material with a fixed lattice (with no thermal vibrations of the atoms). It is an important example of a **[Scalar, Characteristic and Auxiliary](../../properties/classification/general.md) property** of [Materials](../../materials/overview.md), and is routinely calculated during the course of material science simulations. 

The total energy is constituted by the **cohesive (or binding) potential energy** stored internally within the crystal structure of the material, as a result of the chemical bonding interactions between its constituent atoms. A review of its significance in the general context of solid-state thermodynamics is offered in Ref. [^1].

## Computation

The total energy can be calculated by a basic "self-consistent field" (scf) [Workflow](../../workflows/overview.md) computation in [DFT](../../models/dft/overview.md). 

It is presented to the user, as part of the output of a [Job](../../jobs/overview.md), with the appearance displayed below, under the interface of the [Results Tab](../../jobs/ui/results-tab.md) of [Job Viewer](../../jobs/ui/viewer.md). Its final value is expressed in units of electronVolt (eV).

<div class="clearfix"><center><div class="chart"><i class="zmdi zmdi-battery-flash zmdi-hc-3x"></i></div><div class="count"><small><!-- react-text: 1660 -->Total energy<!-- /react-text --><!-- react-text: 1661 --><!-- /react-text --></small><h2>-8.922</h2></div></div>
 
## Links 

[^1]: [Cohesion (Bonding) in Solids, Website](https://www.itp.tu-berlin.de/fileadmin/a3233/upload/SS12/TheoFest2012/Kapitel/Chapter_6.pdf)
