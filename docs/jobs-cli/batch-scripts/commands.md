# Batch Script Commands

Following the set of [resource manager directives](directives.md), [Batch Scripts](overview.md) should also include a series of **UNIX commands** that perform the relevant computations, in the format of a conventional Shell script [^1]. These UNIX commands may perform anything that can be done under a UNIX shell prompt, such as creating directories, transferring files, etc.

The most frequently needed sequence of commands encountered in our Batch scripts consists in the following. Each line is reviewed separately in the ensuing sections.

```bash
cd $PBS_O_WORKDIR
module load <intelmpi or openmpi libraries>
module load <list of other modules>
mpirun -np $PBS_NP ./my_executable
```

## 1. Change to Working Directory

Batch jobs by convention begin execution in the user's [Home Directory](../../infrastructure/login/directories.md) (referenced under the `$PBS_O_HOME` [environment variable](directives.md#environment-variables)). For this reason, many batch scripts execute `cd $PBS_O_WORKDIR` as the first executable statement, in order to switch to the corresponding [Working Directory](directories.md) in which the job was first defined and [submitted](../actions/submit.md). 

The required location of this working directory under the directory structure of our platform is explained [here](directories.md).

## 2. Load Parallel Libraries

Most jobs are executed **in parallel**, meaning that they are distributed over multiple [computing cores and/or nodes](../../infrastructure/compute/parameters.md#nodes-/-ppn) for better performance. This requires the loading of [parallel libraries](../../software/development/libraries.md) (also known as "MPI" libraries) within the Batch Script, via the `module load` command for the [loading](../../cli/actions/modules.md#load-desired-module) of [modules](../../cli/actions/modules.md) under the CLI.

Two such parallel libraries are offered on our platform, the proprietary MPI library by Intel [^2], and the open-source "OpenMPI" library [^3]. The Intel MPI library can be loaded by entering `module load mpi` since it is already the default MPI choice.

!!!note "Automatic loading of Parallel Libraries"
    Many [modeling applications](../../software/applications.md) implemented on our platform automatically load the Intel MPI library as one of their **dependencies** when they are themselves loaded. The parallel library does not therefore need to be loaded separately from the main application.

## 3. Load Other Modules 

Other available [modules](../../cli/actions/modules.md) required as part of the job computation, besides the aforementioned parallel library, can be [loaded](../../cli/actions/modules.md#load-desired-module) within the Batch Script via the same `module load <module name>` command. A convenient approach for loading multiple modules inside the same job, instead of repeating the load command every time, would consist in the following sequence.

```bash
MODULES="module names separated by single space: module1 module2 module3...."
module load $MODULES
```

## 4. Launch Parallel Job

The final launching of the parallel job, following the definition of all required module dependencies, is performed via the `mpirun` command implemented by the chosen Parallel MPI Library mentioned previously. This command consists of the following general structure.

```bash
mpirun -np <no_proc> name_executable`
```

Here, the `<no_proc>` parameter represents the number of processors selected for computation via the relevant [Directives](directives.md), which can be referenced directly with the `$PBS_NP` [environment variable](directives.md#environment-variables) within the command. 

The `name_executable` component of the `mpirun` command on the other hand refers to the name of the executable being run as part of the job. This can either be a **global variable** loaded in one of the modules or present in the user's global search path, or can also be a **local variable** available within the present working directory only. In the latter case, the executable has to be launched with the `./` standard executor command in UNIX operating systems. 

### Adding Executables to Global Search Path

To make an executable globally available across the entire CLI environment, the user should edit his/her `.bashrc` file under the [Login Home](../../infrastructure/login/directories.md) directory using his/her preferred command-line text editor. To add the desired executable on the `PATH` environmental variable defining the global search path, the following commands should be inserted inside `.bashrc`.

```bash
export PATH=<path/to/directory/containing/executable>:$PATH
```

If the executable relies on shared libraries, the following line should also be added to `.bashrc`.

```bash
export LD_LIBRARY_PATH=</path/to/library/>
```

Finally, under the CLI the user should enter the following command to register the executable to the search path and make it globally available.

```
source ~/.bashrc
```

!!!tip "Making user-created scripts executable"
    Whenever the user writes his/her own custom script under the CLI, the command `chmod a+x /path/to/script` should be entered to make it executable, by assigning it the appropriate permissions. 

## Links

[^1]: [Wikipedia Shell script, Website](https://en.wikipedia.org/wiki/Shell_script)

[^2]: [Intel MPI library, Official Website](https://software.intel.com/en-us/mpi-library)

[^3]: [Open MPI library, Official Website](https://www.open-mpi.org/)
