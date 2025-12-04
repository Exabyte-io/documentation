# Add New Software

Users can compile their own software on the [Command Line Interface](
../overview.md) (CLI). This is helpful, for example, after introducing some
changes or patches to the source code. Most of our applications are currently
distributed as Apptainer[^1] (Singularity[^2]) containers, bundled with all
required dependencies. This ensures that each application is isolated and avoids
dependency conflicts. If you plan to run an application that is not installed in
our cluster, we encourage you to package your code and its dependencies as an
Apptainer/<wbr/>Singularity container. If you already have a Docker image, it
can be converted into an Apptainer/<wbr/>Singularity image.

Below is an example of Apptainer/<wbr/>Singularity definition to build Quantum
ESPRESSO container along with its dependencies.


```singularity title="espresso.def"
Bootstrap: docker  # (1)!
From: almalinux:9  # (2)!

%labels  # (3)!
    Maintainer Mat3ra.com
    Version QE-7.5-gcc-openmpi-openblas

%environment  # (4)!
    export PATH=/usr/lib64/openmpi/bin:/opt/qe-7.5/bin:$PATH

%post  # (5)!
    # enable additional repos
    dnf install -y epel-release
    dnf config-manager --set-enabled crb

    # install dependencies
    dnf install -y autoconf \
        gcc \
        gcc-c++ \
        gcc-gfortran \
        git \
        make \
        fftw-devel \
        openblas \
        openblas-devel \
        openmpi-devel \
        scalapack-openmpi-devel \
        wget

    # download QE and compile
    VERSION=7.5
    INSTALL_PREFIX="/opt/qe-$VERSION"
    BUILD_DIR=~/tmp
    mkdir $BUILD_DIR

    cd $BUILD_DIR
    wget https://gitlab.com/QEF/q-e/-/archive/qe-${VERSION}/q-e-qe-${VERSION}.tar.gz
    tar -xf q-e-qe-${VERSION}.tar.gz
    cd q-e-qe-${VERSION}

    export PATH=/usr/lib64/openmpi/bin:$PATH
    export FFLAGS="-O2 -fallow-argument-mismatch"
    export FCFLAGS="-O2 -fallow-argument-mismatch"

    ./configure --prefix=${INSTALL_PREFIX} MPIF90=mpif90 CC=mpicc F90=gfortran F77=gfortran \
      --with-scalapack=yes \
      BLAS_LIBS="-lopenblas" LAPACK_LIBS="-lopenblas" \
      LDFLAGS="-Wl,-rpath,/usr/lib64/openmpi/lib -Wl,-rpath,/usr/lib64"

    make all -j$(nproc)
    make install

    # cleanup
    rm -rf $BUILD_DIR
    dnf clean all && rm -rf /var/lib/dnf /var/cache/dnf /var/cache/yum
```

1. Bootstrap from a Docker image
2. Select base image
3. Metadata such as version, maintainer details, etc.
4. Set runtime environment variables
5. Build routine goes under the `post` section

!!! info
    Large libraries such as Intel OneAPI suite, NVIDIA HPC SDK, which are
    several Gigabyte in size, can be mapped from our custer host instead of
    bundling together with the application.

To build a container on Mat3ra clusters, please submit a [PBS batch script](
../../jobs-cli/batch-scripts/overview.md). This ensures the resource-intensive
build process runs on a compute node rather than the login node.

```bash title="build-qe.pbs"
#!/bin/bash
#PBS -N Build_QE
#PBS -j oe
#PBS -l nodes=1
#PBS -l ppn=4
#PBS -l walltime=00:01:00:00
#PBS -q OR
#PBS -m abe
#PBS -M info@mat3ra.com

cd $PBS_O_WORKDIR
apptainer build espresso.sif espresso.def
```

Once the container is built, we are ready to run applications packaged in it.
Please follow [this documentation page](../../jobs-cli/batch-scripts/apptainer.md)
to find more about how to submit jobs and use apptainer. For practical
templates, please visit [CLI job examples](
https://github.com/Exabyte-io/cli-job-examples).


### Transfer external images

You can build containers on your local machine or pull pre-built ones from
sources like the such as [NVIDIA GPU Cloud](
https://catalog.ngc.nvidia.com/orgs/hpc/containers/quantum_espresso). If
Apptainer is installed locally, build the container using:

```bash
apptainer build espresso.sif espresso.def
```

Once built, you can push the image to a container registry such as the
[GitHub Container Registry](
https://docs.github.com/en/packages/working-with-a-github-packages-registry/working-with-the-container-registry).

```bash
apptainer push espresso.sif oras://ghcr.io/<user-or-org-name>/<namespace>/<container-name>:<tag>
```

Then, pull the image from the Mat3ra login node::
```bash
apptainer pull oras://ghcr.io/<user-or-org-name>/<namespace>/<container-name>:<tag>
```

!!! tip
    - You may use GitHub workflow to build images and push to GHCR.
    - When pulled a docker image, apptainer will automatically convert and save as
    SIF file.

Alternatively, you can copy the local image file directly to the Mat3ra cluster
via SCP:
```bash
scp espresso.sif <username>@login.mat3ra.com:/cluster-001-home/<username>/
```

## Compiling software in Mat3ra cluster
In order to compile such new software a special permission is required to access
the master nodes of our [computational clusters](
../../infrastructure/clusters/overview.md), where the compilation shall be
performed. This permission can be requested by following [these instructions](
../../ui/support.md).

We also explain how to add python packages to the environment [in this page](
create-python-env.md).

## Example: New Quantum ESPRESSO Version

The user might wish to compile a version of the [Quantum ESPRESSO](
../../software-directory/modeling/quantum-espresso/overview.md) simulation
package different from the ones offered [through environment modules](
modules-actions.md#list-available-modules). This new versions might also include
modifications to the source code by the user.

We refer to the official documentation[^3] for the instructions on how to
compile Quantum ESPRESSO via CLI. Sample routines that allow for the compilation
are demonstrated below:

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

!!! warning "Compilation routines are given for demonstration purpose only"
    The commands above are present to demonstrate the approach only and are
    limited in applicability. They do not include any consideration of the
    optimization of parallel performance, for example.

## Links

[^1]: [Apptainer User Guide](https://apptainer.org/docs/user/latest/)
[^2]: [Singularity User Guide](https://docs.sylabs.io/guides/latest/user-guide/)
[^3]: [User’s Guide for Quantum ESPRESSO, Document](https://www.quantum-espresso.org/Doc/user_guide.pdf)
