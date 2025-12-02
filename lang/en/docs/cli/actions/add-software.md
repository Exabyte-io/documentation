# Add New Software

The user can compile new software on the [Command Line Interface](
../overview.md) (CLI). This is helpful, for example, after introducing some
changes or patches to the source code. Currently, majority of our applications
are packaged as Apptainer[^1] (Singularity[^2]) containers along with their
dependencies. In that way each application is independent of each other, and
there is no conflict among dependencies. If you wish to run an application that
is installed in our cluster, you are encouraged to build your application and
dependencies as Apptainer/<wbr/>Singularity container. It is also possible to
convert docker containers into Apptainer/<wbr/>Singularity image.

Below is an example Apptainer/<wbr/>Singularity definition to build Quantum
ESPRESSO along with its dependencies.


```singularity title="espresso.def"
Bootstrap: docker  # (1)!
From: almalinux:9.7  # (2)!

%labels  # (3)!
    Maintainer Mat3ra.com
    Version QE-6.3-gcc-openmpi-openblas

%environment  # (4)!
    export PATH=/usr/lib64/openmpi/bin:/opt/qe-6.3/bin:$PATH
    export LD_LIBRARY_PATH=/usr/lib64/openmpi/lib:$LD_LIBRARY_PATH

%post  # (5)!
    # install dependencies
    dnf install -y epel-release
    dnf config-manager --set-enabled crb
    dnf install -y gcc-gfortran \
        git \
        make \
        fftw-devel \
        openblas \
        openblas-devel \
        openmpi-devel \
        scalapack-openmpi-devel \
        wget \
        which

    # download QE and compile
    VERSION=6.3
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

    ./configure MPIF90=mpif90 CC=mpicc F90=gfortran F77=gfortran \
      --with-scalapack=yes \
      BLAS_LIBS="-lopenblas" LAPACK_LIBS="-lopenblas" \
      LDFLAGS="-Wl,-rpath,/usr/lib64/openmpi/lib -Wl,-rpath,/usr/lib64"

    make all
    make -B install

    # cleanup
    rm -rf $BUILD_DIR
    dnf clean all && rm -rf /var/lib/dnf /var/cache/dnf /var/cache/yum
```

1. Bootstrap from a Docker image
2. Select your base image
3. Metadata such as version, maintainer details, etc.
4. Set runtime environment variables
5. Build routine goes under the `post` section

Container can be built with:
```bash
apptainer build espresso.sif espresso.def
```

Once the container image is build, it maybe pushed to a container registry such
as [GitHub Container Registry](
https://docs.github.com/en/packages/working-with-a-github-packages-registry/working-with-the-container-registry).

```bash
apptainer push espresso.sif oras://ghcr.io/<user-or-org-name>/<namespace>/<container-name>:<tag>
```

Now, the image can be pulled from another machine with:
```bash
apptainer pull oras://ghcr.io/<user-or-org-name>/<namespace>/<container-name>:<tag>
```

Alternatively, user can secure copy the image file:
```bash
scp espresso.sif <username>@login.mat3ra.com:/cluster-001-home/<username>
```

!!! info
    Large libraries such as Intel OneAPI, NVIDIA HPC SDK, which are several
    Gigabyte in size, can be mapped from our custer host instead of bundling
    together with the application.


## Compiling software in our cluster
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

!!! warning "Compilation routines are given for demonstration only"
    The commands above are present to demonstrate the approach only and are
    limited in applicability. They do not include any consideration of the
    optimization of parallel performance, for example.

## Links

[^1]: [Apptainer User Guide](https://apptainer.org/docs/user/latest/)
[^2]: [Singularity User Guide](https://docs.sylabs.io/guides/latest/user-guide/)
[^3]: [User’s Guide for Quantum ESPRESSO, Document](https://www.quantum-espresso.org/Doc/user_guide.pdf)
