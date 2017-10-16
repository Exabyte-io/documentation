<!-- TODO: come back and revise once more after the rest -->

This page helps users quickly get through the documentation.

# Login

We support 2 basics login types: through web-page and via secure shell terminal. You must have a valid username and password in order to login via web. Secure shell sessions use [key-based authentication](/cli/login/#upload-ssh-key). Users logged-in through the web can also access command-line terminal and remote desktop clients right inside the web browser without additional authentication. Read more in:

- [secure shell and in-browser terminals](/cli/overview/#in-browser-terminal-and-ssh-terminal)
- [remote desktop session example](/electronic-density-mesh/#preparing-for-visualization)
- [connection options explained](/connection-options/)
- <a href="http://platform.exabyte.io/login" target="_blank">login page</a>

# Creating materials

There are 3 basic ways to input material geometries:

- [construct new crystal geometries](/materials/creating-structures/) using our browser-based crystallographic design tools
- [upload structure](/materials/upload-and-import/#upload-structure)  in POSCAR/CIF format(s)
- [import structure](/materials/upload-and-import/#import-structure)  from a third-party database (eg. materialsproject.org)

!!! note "Combinatorial sets"
    [Combinatorial sets](/materials/combinatorial-sets/) make it possible to rapidly create a large number of material geometries.

# Running simulations

Next step after creating/choosing a material is to simulate it to extract [characteristic properties](/materials/properties/). In order to do so, one needs to construct a simulation workflow.

## Workflows

[Workflows](/models/simulation-workflows/) define the algorithm used during simulation. Each workflow has one or more characteristic properties associated with it. Workflows are dependent on simulation engine and model. For example, [Density Functional Theory](/models/density-functional-theory/) as implemented in Quantum ESPRESSO and VASP is supported at current.

More information about specific workflows, including tutorials and input date:

- [electronic band structure](/tutorials/band-structure)
- [electronic band gap](/tutorials/band-gap)
- [electronic density of states](/tutorials/density-of-states)
- [electronic density mesh](/tutorials/electronic-density-mesh)
- [zero point energy](/tutorials/zero-point-energy)
- [formation energy](/tutorials/formation-energy)
- [structural relaxation](/tutorials/relaxation)
- [automatic k-point convergence](/tutorials/kpt-convergence)
- [custom-input workflow](/tutorials/custom-input-workflow)
- [fermi surface](/tutorials/fermi-surface)
- [combinatorial screening](/tutorials/combinatorial-screening)
<!-- - [combinatorial screening of iii-v semiconductor band gaps](/tutorials/semiconductors/III-Vs-band-gap.md) -->

## Compute

Compute parameters ([submission queue](/compute/queues), number of nodes and processors per node, time limit, cloud provider/cluster) can be set before running simulations. Read on at:

- [setting compute parameters](/compute/setting-parameters/)
- [compute platform overview](/compute/overview/)
- [compute platform architecture](/compute/overview/#platform-architecture)
- [submission queues](/compute/queues/)
- [queue-based pricing](/billing/pricing-and-service-levels/#queue-based-pricing)
- [unified storage system](/cli/storage-system/)
- [linpack benchmark & scalability study](/compute/hpl-benchmark/)
- [simulation benchmarks](/compute/benchmarks-and-scalability/)

## Run simulations via command-line interface (CLI)

Advanced users connecting via command line terminal may use our queuing system supporting multiple clusters/cloud providers or, alternatively, directly use portable batch system (PBS/torque) underneath. Read more at:

- [job submission: tutorial](/tutorials/cli-job)
- [job submission examples](/cli/jobs/)
- [job script templates](/cli/jobs/#pre-configured-submit-scripts)
- [modules environment](/cli/modules-environment/)

## Extra simulation capabilities

- [restart from previous run](/tutorials/restart-job)
- [remote desktop visualization](/tutorials/remote-desktop)

# Exabyte Data Convention

We employ a proprietary JSON-based data convention that supports storing materials, simulations and compute properties in an organized and easy-to-navigate manner. It is designed with collaborative access to data in mind and have a flexible permission scheme allowing for complete privacy and wide publicity. More at:

We store all data about simulations and materials. Data originated from web application is automatically organized and searchable within the "Analytics" page (see below). Data originated on command line is accessible from within the web application and can also be further imported and organized for future search and potential use in advanced analytics / data mining / machine learning.

- [data conventions](/getting-started/data-conventions/)
- [analytics (comparing materials)](/materials/comparing-materials/)


# Other

- [service levels and pricing](/billing/pricing-and-service-levels/)
- [storage quotas](/billing/storage-quota/)
