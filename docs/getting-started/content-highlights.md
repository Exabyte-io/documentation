# Content Highlights

This page helps users quickly get through the documentation.

## Login

We support two basics login connection methods: through our [Web Interface](../ui/overview.md), and [Command Line Interface (CLI)](../cli/overview.md). You must have a valid username and password in order to login via either option. Secure shell sessions use [key-based authentication](../remote-connection/ssh.md#generate-ssh-keys). Users logged-in through the web interface can, without additional authentication, also access the CLI via the [Web Terminal](../remote-connection/web-terminal.md), and have also a [Remote Desktop Environment](../remote-connection/remote-desktop.md) at their disposal. 

The user can find out more about such connection methods under the following links.

- [secure shell (ssh)](../remote-connection/ssh.md) 
- [web terminal](../remote-connection/web-terminal.md)
- [remote desktop](../remote-connection/remote-desktop.md)
- [connection options explained](../remote-connection/overview.md)
- <a href="http://platform.exabyte.io/login" target="_blank">login page</a>

## Creating Materials

There are three basic ways to input material geometries.

- [construct new crystal geometries](../materials-designer/overview.md), using our web-based crystallographic design tools
- [upload structure](../materials/actions/upload.md) in POSCAR/CIF format(s)
- [import structure](../materials/actions/import.md) from a third-party database (e.g. materialsproject.org)

!!! note "Combinatorial sets"
    [Combinatorial sets](../materials-designer/header-menu/advanced/combinatorial-set.md) make it possible to rapidly create a large number of material geometries.

## Running Simulations

Next step, after creating/choosing a material as described above, is to simulate it to extract its desired [characteristic properties](../properties/overview.md). In order to do so, one needs to [construct](../workflow-designer/overview.md) a simulation [workflow](../workflows/overview.md). 

Our [computational infrastructure](../infrastructure/overview.md) supports multiple [clusters/cloud providers](../infrastructure/clusters/overview.md), including [Amazon's AWS](../infrastructure/clusters/aws.md) or [Microsoft's Azure](../infrastructure/clusters/azure.md) services.

### Workflows

[Workflows](../workflows/overview.md) define the computational algorithms used during simulation. Each workflow has one or more characteristic properties associated with it. Workflows are dependent on the [simulation engine](../software/overview.md), on the choice for a [model](../models/overview.md), and on its computational implementation, or [method](../methods/overview.md). 

For example, [Density Functional Theory](../models-directory/dft/overview.md), as implemented in its [plane-wave pseudopotential formulation](../methods-directory/pseudopotential/overview.md) under the [Quantum ESPRESSO](../software-directory/modeling/quantum-espresso/overview.md) and [VASP](../software-directory/modeling/vasp/overview.md) codes, is supported at current.

More information about specific workflows can be found in the tutorial links below.

- [electronic band structure](../tutorials/band-structure)
- [electronic band gap](../tutorials/band-gap)
- [electronic density of states](../tutorials/density-of-states)
- [electronic density mesh](../tutorials/electronic-density-mesh)
- [zero point energy](../tutorials/zero-point-energy)
- [formation energy](../tutorials/formation-energy)
- [structural relaxation](../tutorials/relaxation)
- [automatic k-point convergence](../tutorials/kpt-convergence)
- [custom-input workflow](../tutorials/custom-input-workflow)
- [fermi surface](../tutorials/fermi-surface)
- [combinatorial screening](../tutorials/combinatorial-screening)
<!-- - [combinatorial screening of iii-v semiconductor band gaps](../tutorials/semiconductors/III-Vs-band-gap.md) -->

### Compute

Important [compute parameters](../infrastructure/compute/parameters.md) (such as submission queue, number of nodes and processors per node, time limit, cloud provider/cluster etc...) should be set before running simulations. The user can find out more about them under the following links.

- [setting compute parameters](../infrastructure/compute/parameters.md)
- [compute platform overview](../infrastructure/compute/overview.md)
- [compute platform architecture](../infrastructure/overview.md)
- [submission queues](../infrastructure/resource/queues.md)
- [queue-based pricing](../infrastructure/resource/category.md)
- [unified storage system](../infrastructure/storage.md)
- [linpack benchmark & scalability study](../benchmarks/hpl-benchmark.md)
- [simulation benchmarks](../benchmarks/high-throughput-screening.md)

### Run Simulations via Command Line Interface (CLI)

Advanced users connecting to our CLI may [submit jobs directly through it](../jobs-cli/overview.md), through the use of [Batch Scripts](../jobs-cli/batch-scripts/overview.md). The user can read more in the following pages.

- [job submission via cli: main explanation](../jobs-cli/overview.md)
- [job submission via cli: tutorial](../tutorials/cli-job)
- [batch script templates](../jobs-cli/batch-scripts/overview.md)
- [modules environment](../cli/modules.md)

<!-- TODO by GM: uncomment when tutorials are implemented

### Extra Simulation Capabilities

- [restart from previous run](../tutorials/restart-job)
- [remote desktop visualization](../tutorials/remote-desktop)

-->

## Exabyte Data Convention

We employ a [JSON-based data convention](../data-structured/overview.md) that supports storing materials, simulations and compute properties in an organized and easy-to-navigate manner. It is designed with collaborative access to data in mind, and has a flexible permission scheme allowing for complete privacy or wide publicity.

We store all data about simulations and materials. Data originated from web application is automatically organized and searchable within the "Analytics" page. Data originated on command line is [accessible from within the web application](../data-in-objectstorage/overview.md), and can also be further imported and organized for future search and potential use in advanced analytics / data mining / machine learning applications.

Find out more under the following pages.

- [data convention](../data-structured/overview.md)
- analytics (comparing materials)

## Other Account-related Features

- [service levels and pricing](../pricing/service-levels.md)
- [storage quotas](../accounts/quota.md)
- [account balance](../accounts/balance.md)
