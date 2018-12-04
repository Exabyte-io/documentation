# Add New Software 

The user can compile new software on the [Command Line Interface](../overview.md) (CLI). This is helpful, for example, after introducing some changes or patches to the source code. In order to compile such new software a special permission is required to access the master nodes of our [computational clusters](../../infrastructure/clusters/overview.md), where the compilation shall be performed. This permission can be requested by following [these instructions](../../ui/support.md).

We also explain how to add python packages to the environment [in this page](create-python-env.md).

## Example: New Quantum ESPRESSO Version

The user might wish to compile a version of the [Quantum ESPRESSO](../../software/modeling/quantum-espresso.md) simulation package different from the ones offered [through environment modules](modules.md#list-available-modules). This new versions might also include modifications to the source code by the user. 

We refer to the official documentation [^1] for the instructions on how to compile Quantum ESPRESSO via CLI. Sample routines that allow for the compilation are demonstrated below:

```bash
# Create temporary directory
mkdir q-e-compilation && cd q-e-compilation

# Download and upack the archive
wget https://github.com/QEF/q-e/archive/qe-6.3MaX.tar.gz
tar -xvzf qe-6.3MaX.tar.gz
cd q-e-qe-6.3MaX/

# Load modules
module load mpi/ompi-110 openblas/218-g-540
./configure
make libfox
make pw
``` 

!!! warning "Compilation routines are given for demonstration only"
    The commands below are present to demonstrate the approach only and are limited in applicability. They do not include any consideration of the optimization of parallel performance, for example.

## Links

[^1]: [User’s Guide for Quantum ESPRESSO, Document](https://www.quantum-espresso.org/Doc/user_guide.pdf)
