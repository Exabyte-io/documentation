# Thermal Vibrational Energy

A second contribution to the internal energy, besides the cohesive chemical component, originates from the thermally-induced **lattice vibrations (phonons)**. These are particularly significant at high temperatures, but in the context of [DFT](../../models/dft/overview.md) computations performed at zero temperature they are typically negligible in terms of their energetic contribution. This contribution remains however finite and positive in magnitude due to quantum effects. 

## Zero Point Energy

This **"Zero-point Energy"** contribution to the internal energy of a zero-temperature solid can still be computed separately, as explained in the forthcoming sections of this page. A theoretical review of lattice vibrations in solid-state physics is available in Ref. [^1], whereas a description dedicated to the concept of Zero-point Energy can be found in Ref. [^2].

## Computation 

The Zero-point Energy  has to be computed by performing a [Phonon calculation](../non-scalar/phonon-dispersions.md) on the material under investigation using an appropriate [Workflow](../../workflows/overview.md).

It is displayed under the [Results Tab](../../jobs/ui/results-tab.md) of the corresponding [Job](../../jobs/overview.md) in the following manner, also in units of eV. 

<div class="clearfix"><center><div class="chart"><i class="zmdi zmdi-battery-flash zmdi-hc-3x"></i></div><div class="count"><small><!-- react-text: 1660 -->
Zero point energy<!-- /react-text --><!-- react-text: 1661 --><!-- /react-text --></small><h2>0.075</h2></div></div>

## Links 

[^1]: [Lattice Vibrations, Website](https://www.itp.tu-berlin.de/fileadmin/a3233/upload/SS12/TheoFest2012/Kapitel/Chapter7.pdf)

[^2]: [Wikipedia Zero-point energy, Website](https://en.wikipedia.org/wiki/Zero-point_energy)
