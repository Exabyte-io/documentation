# Average Pressure

We define the **Average Pressure** $p_{avg}$ of a Material as a Scalar [Characteristic](/data-structured/overview.md) property obtained from the following conventional formula.

$$
p_{avg}=-\frac{1}{3} \mathrm{Tr} \hspace{1pt} {\boldsymbol{\sigma}}
$$ 

where ${\boldsymbol{\sigma}}$ is the [internal stress tensor](../array/stress-tensor.md) of the solid, and $\mathrm{Tr}$ indicates the Trace operator in linear algebra [[1](#links)]. 

The average pressure can be computed as part of any [Workflow](/workflows/overview.md) involving at least one basic "self-consistent field" (scf) total energy calculation. It is then presented to the user, as part of the output of a [Job](/jobs/overview.md), with the following appearance under the interface of the [Results Tab](/jobs/ui/results-tab.md) of [Job Viewer](/jobs/ui/viewer.md). Its final value is expressed in units of kilo bars (kbar).

![Average Pressure](/images/average-pressure.png "Average Pressure")

# Total Force

The **Total Force** is also treated as a scalar, defined as the norm (or magnitude) of the net vector sum of the individual [atomic forces](../array/atomic-forces.md), summed across all atoms present in the crystal structure under consideration.

This material property is displayed under the [Results Tab](/jobs/ui/results-tab.md) as follows, in units of eV/Angstroms. It it also routinely computed as part of any total energy scf calculation.

![Total Force](/images/total-force.png "Total Force")

# Links

1. [Wikipedia Trace (linear algebra), Website](https://en.wikipedia.org/wiki/Trace_(linear_algebra))
