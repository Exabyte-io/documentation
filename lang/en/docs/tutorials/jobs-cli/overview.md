# Tutorials on Jobs via Command Line Interface

The tutorials below explain how to submit jobs via the [Command Line Interface (CLI)](../../jobs-cli/overview.md), and how to make the job results available for post-processing with other tools in our platform.

Follow these tutorials if you are accustomed to command line and are still transitioning to the Mat3ra workflows, or if you are an advanced user trying to implement a workflow not yet natively supported by the web interface (in which case, please also [let us know](other/support.md) what functionality is desirable!)


## Tutorial: [Creating, Running, and Inspecting Jobs](job-cli-example.md)

[This first tutorial](job-cli-example.md) explains how to create the input scripts for running a materials science computation (in this case using the [Quantum ESPRESSO](../../software-directory/modeling/quantum-espresso/overview.md) modeling application.) We also explain how to submit the corresponding [simulation job](../../jobs/overview.md) to the [Resource Manager](../../infrastructure/resource/overview.md) of our computational [infrastructure](../../infrastructure/overview.md) via the [Command Line Interface](../../cli/overview.md), how to control whether the results are automatically imported to the main [Web Interface](../../ui/overview.md) of our platform, and how to inspect the status of the job and the job results.

## Tutorial: [QE GPU Job](jobs-cli/qe-gpu.md)
[This tutorial](jobs-cli/qe-gpu.md) explains how to run jobs utilizing GPUs via [command-line interface](../../cli/overview.md), using a [Quantum ESPRESSO](../../software-directory/modeling/quantum-espresso/overview.md) job as an example, and presents an example of a computational speed-up achieved.
