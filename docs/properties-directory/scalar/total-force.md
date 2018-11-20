# Total Force

Similarly to the [average pressure](pressure.md), the **Total Force** is also treated as a [Scalar](../../properties/classification/general.md) property, defined as the norm (or magnitude) of the net vector sum of the individual [atomic forces](../structural/basis.md), summed across all atoms present in the crystal structure under consideration.

## Example

This material property is displayed under the [Results Tab](../../jobs/ui/results-tab.md) of [Job Viewer](../../jobs/ui/viewer.md) as follows, in units of eV/Angstroms. It it also routinely computed as part of any total energy self-consistent field (scf) calculation using [DFT](../../models/dft/overview.md).

<div class="clearfix">
    <center>
        <div class="chart"><i class="zmdi zmdi-arrows zmdi-hc-3x"></i></div>
        <div class="count">
        	<small>Total force</small>
            <h2>0.001999</h2>
        </div>
     </center>
</div>

## Schema 

The JSON schema and an example representation for this property can be found [here](../../properties/data/list.md#total-force).
