# Thermal Vibrations and Zero Point Energy

A further contribution to the internal energy of a material structure originates from the thermally-induced **lattice vibrations (phonons)**. These are particularly significant at high temperatures, but in the context of [DFT](../../models/dft/overview.md) computations performed at zero temperature they are typically negligible in terms of their energetic contribution. This contribution however remains finite and positive in magnitude due to quantum residual effects. This **"Zero-point Energy"** [^1] contribution to the internal energy of a zero-temperature solid can thus be computed separately. 

## Example

The Zero-point Energy  has to be computed by performing a [Phonon calculation](../non-scalar/phonon-dispersions.md) on the material under investigation using an appropriate [Workflow](../../workflows/overview.md).

It is displayed under the [Results Tab](../../jobs/ui/results-tab.md) of the corresponding [Job](../../jobs/overview.md) in the following manner, also in units of eV. 

<div class="clearfix">
    <center>
        <div class="chart"><i class="zmdi zmdi-battery-flash zmdi-hc-3x"></i></div>
        <div class="count">
        	<small>Zero point energy</small>
            <h2>0.075</h2>
        </div>
     </center>
</div>

## Schema 

The JSON schema and an example representation for this property can be found [here](../../properties/data/list.md#zero-point-energy).

## Links 

[^1]: [Wikipedia Zero-point energy, Website](https://en.wikipedia.org/wiki/Zero-point_energy)
