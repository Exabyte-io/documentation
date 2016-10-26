<!-- by TB -->

This page helps users quickly get through the documentation.

# Login

We support 2 basics login types: through web-page and via secure shell terminal. You must have a valid username and password in order to login via web. Secure shell sessions use [key-based authentication](/cli/login/#upload-ssh-key). Users logged-in through the web can also access command-line terminal and remote desktop clients right inside the web browser without additional authentication. Read more at:

- [secure shell and in-browser terminals](/cli/overview/#in-browser-terminal-and-ssh-terminal)
- [remote desktop session example](/electronic-density-mesh/#preparing-for-visualization)
- [connection options explained](/connection-options/)
- <a href="http://platform.exabyte.io/login" target="_blank">login page</a>

# Data conventions

We support collaborative access to data and have a flexible permission scheme that supports complete privacy as well as wide publicity. More at:

- [data conventions](/getting-started/data-conventions/)

# Creating materials

There are 3 basic ways to input material geometries:

- [construct new crystal geometries using in-browser crystallographic design tools](/materials/creating-structures/)
- [upload structure in POSCAR/CIF format(s)](/materials/upload-and-import/#upload-structure)
- [import structure from a third-party database](/materials/upload-and-import/#import-structure) (materialsproject.org is supported at current)

!!! note "Combinatorial sets"
    [Combinatorial sets](/materials/combinatorial-sets/) make it possible to create a large number of material geometries at once.

# Running simulations

Next step after setting up material geometry is to simulate it and extract [characteristic properties](/materials/characteristic-properties/). In order to do so, users have to construct a simulation workflow and set up compute parameters.

## Workflows

[Workflows](/models/simulation-workflows/) define the algorithm used during the simulation. Each characteristic property has a workflow associated with itself. Workflows are dependent on the simulation engine and model. [Density Functional Theory](/models/density-functional-theory/) as implemented in Quantum ESPRESSO and VASP is supported at current.

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
- [combinatorial screening general](/tutorials/combinatorial-screening)
- [combinatorial screening of iii-v semiconductor band gaps](/tutorials/semiconductors/III-Vs-band-gap.md)
- [default simulation input files](/models/example-simulations/)

## Compute parameters

Compute parameters ([submission queue](/compute/queues), number of nodes and processors per node, time limit, cloud provider/cluster) can be set before running simulation. By default "Debug" queue with 1 node, 1 CPU and 1h walltime are used. Read on at:

- [setting compute parameters](/compute/setting-parameters/)
- [compute platform architecture](/compute/overview/#platform-architecture)
- [compute platform overview](/compute/overview/)
- [submission queues](/compute/queues/)
- [queue-based pricing](/billing/pricing-and-service-levels/#queue-based-pricing)
- [unified storage system](/cli/storage-system/)
- [linpack benchmark & scalability study](/compute/hpl-benchmark/)
- [simulation benchmarks](/compute/benchmarks-and-scalability/)

## Run simulations via command-line interface (CLI)

Advanced users connecting via command line terminal may use our unified queuing system (UQS) supporting multiple clusters/cloud providers or, alternatively, directly use portable batch system (PBS/torque) underneath UQS. Read more at:

- [job submission: tutorial](/tutorials/cli-job)
- [job submission examples](/cli/jobs/)
- [job script templates](/cli/jobs/#pre-configured-submit-scripts)
- [modules environment](/cli/modules-environment/)

## Extra simulation capabilities

- [restart from previous run](/tutorials/restart-job)
- [remote desktop visualization](/tutorials/remote-desktop)

# Analyzing the data

We store all data about simulations and materials. Data originated from web application is automatically organized and searchable within the "Analytics" page (see below). Data originated on command line is accessible from within the web application and can also be further imported and organized for future search and potential use in advanced analytics / data mining / machine learning.

- [analytics (comparing materials)](/materials/comparing-materials/)
- [CLI data import](/tutorials/cli-job-import)

!!! note "Data formats"
    We developed proprietary modular JSON-based data formats that support storing materials, simulations and compute properties in an organized and easy-to-navigate manner.

# Other

- [service levels and pricing](/billing/pricing-and-service-levels/)
- [storage quotas](/billing/storage-quota/)
