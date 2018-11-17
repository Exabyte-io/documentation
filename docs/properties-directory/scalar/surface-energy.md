# Surface Energy

In [Density Functional Theory](../../models/dft/overview.md), the surface energy $\gamma$ [^1] can be extracted as follows.

$$ 
\gamma = {\frac {E_{slab}-N\cdot E_{bulk}}{2A}}
$$

where $N$ is the number of atoms in the slab and $A$ is the surface area, with $E$ being the corresponding total energies. Thus one needs to have the total energy for the slab as well as the total energy for bulk material(s) in order to calculate the corresponding surface energy.

## Computation

The surface energy can be calculated by an appropriate [Workflow](../../workflows/overview.md) computation in [DFT](../../models/dft/overview.md). 

It is presented to the user with the appearance displayed below, under the interface of the [Results Tab](../../jobs/ui/results-tab.md) of [Job Viewer](../../jobs/ui/viewer.md). Its final value is expressed in units of eV/Angstroms^2.

<div class="clearfix">
    <center>
        <div class="chart"><i class="zmdi zmdi-battery-flash zmdi-hc-3x"></i></div>
        <div class="count">
        	<small>Surface energy</small>
            <h2>0.165</h2>
        </div>
     </center>
</div>

## Schema and Example 

The JSON schema and an example representation for this property can be found [here](../../properties/data/list.md#surface-energy).

## Links 

[^1]: [Wikipedia Surface Energy, Website](https://en.wikipedia.org/wiki/Surface_energy)
