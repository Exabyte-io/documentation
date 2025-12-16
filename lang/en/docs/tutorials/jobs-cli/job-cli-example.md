# Creating, Running, and Inspecting Jobs via Command Line Interface

This tutorial explains how to run a [job](../../jobs/overview.md) via the [Command Line Interface](../../cli/overview.md) (CLI) of our platform. 
Additionally, we discuss how to enable (or disable, if desired) an automatic extraction of information from the job output files, to make them available for user analysis in the web interface, under the [Files Tab](../../jobs/ui/files-tab.md) of [Job Viewer](../../jobs/ui/viewer.md). For further details, you can consult the [relevant part of the documentation](../../jobs-cli/overview.md) as you follow the tutorial. 

The reader is assumed to be familiar with command line basics, such as file system navigation and file editing in Linux. 
<!--
Before proceeding with the tutorial, the reader is advised to log into CLI using one of the available [remote connection methods](../../remote-connection/overview.md).
-->
 
Here, we will use a template input file and a bash script to sweep the lattice parameter space for a given structure. We will use [Quantum ESPRESSO](../../software-directory/modeling/quantum-espresso/overview.md) (**QE**) as an example simulations engine, however all command-line related directives apply universally.

## 1. Connect to CLI

First, [navigate](../../remote-connection/actions/open-terminal.md) to the [Web Terminal](../../remote-connection/web-terminal.md) for accessing the [command-line interface](../../cli/overview.md) of our platform. (You can also use any other available [remote connection method](../../remote-connection/overview.md).) 

Once CLI is open, navigate to (or create) the desired job [working directory](../../jobs-cli/batch-scripts/directories.md), which you *must* position into a subdirectory of the [Home Folder](../../infrastructure/clusters/directories.md) of one of the [clusters](../../infrastructure/clusters/overview.md). Remember that it is the *location* of the   working directory (or, more precisely, of the directory from which you submit the job) that will determine *which cluster* your job would run at. (Here we assume you are logged into the main login node, which is the default behavior; however, if you log in directly into one of the clusters, you would not be able to access home directories of other clusters anyway, nor to submit to other clusters.)


## 2. Input File
We now need to prepare the **input file(s)**, defining our desired calculation. For our example, you can copy-paste the template **QE** input file from the expandable section below 
(you can also copy from <a href="https://raw.githubusercontent.com/Exabyte-io/documentation/648565e031b6cbd5c86b1618a0ad16be41832a25/lang/en/docs/tutorials/jobs-cli/script_examples/pw.in" target="_blank" type="text/plain">this link</a>, which opens in a new browser tab.) 
Name the file `pw.in` and place it in your [working directory](../../jobs-cli/batch-scripts/directories.md).
??? example "Template input file (click to expand)"
    
    ```fortran title="pw.in"
    ! scf for SrZrO3 for a supercell of Pnma ground state  structure
    &control
        calculation = 'scf',
        restart_mode = 'from_scratch',
        prefix = 'srzro'
        tstress =.true.
        tprnfor=.true.
        outdir = './_outdir'
        wfcdir = './'
        prefix = '${celldm1}'
        pseudo_dir = './_pseudo'
     /
     &system
        ibrav = 1
        celldm(1) = ${celldm1},
        nat = 40
        ntyp = 3
        ecutwfc = 40
        ecutrho = 200
        tot_charge = 0
    /
    &electrons
       mixing_beta = 0.7
       conv_thr = 1.0d-8
    /
    ATOMIC_SPECIES
     Sr 87.62     sr_pbe_gbrv_1.0.upf
     Zr 91.224    zr_pbe_gbrv_1.0.upf
     O  15.999    o_pbe_gbrv_1.2.upf
    !supercell of  "Strontium Zirconate" (SrZrO3), in its ground state equilibrium crystal structure (space group "Pnma")
    ATOMIC_POSITIONS (crystal)
    Zr     0.250000000         0.250000000         0.250000000
    Zr     0.750000000         0.250000000         0.250000000
    Zr     0.250000000         0.750000000         0.250000000
    Zr     0.750000000         0.750000000         0.250000000
    Zr     0.250000000         0.250000000         0.750000000
    Zr     0.750000000         0.250000000         0.750000000
    Zr     0.250000000         0.750000000         0.750000000
    Zr     0.750000000         0.750000000         0.750000000
    Sr     0.000000000         0.000000000         0.000000000
    Sr     0.500000000         0.000000000         0.000000000
    Sr     0.000000000         0.500000000         0.000000000
    Sr     0.500000000         0.500000000         0.000000000
    Sr     0.000000000         0.000000000         0.500000000
    Sr     0.500000000         0.000000000         0.500000000
    Sr     0.000000000         0.500000000         0.500000000
    Sr     0.500000000         0.500000000         0.500000000
    O      0.000000000         0.250000000         0.250000000
    O      0.250000000         0.000000000         0.250000000
    O      0.250000000         0.250000000         0.000000000
    O      0.500000000         0.250000000         0.250000000
    O      0.750000000         0.000000000         0.250000000
    O      0.750000000         0.250000000         0.000000000
    O      0.000000000         0.750000000         0.250000000
    O      0.250000000         0.500000000         0.250000000
    O      0.250000000         0.750000000         0.000000000
    O      0.500000000         0.750000000         0.250000000
    O      0.750000000         0.500000000         0.250000000
    O      0.750000000         0.750000000         0.000000000
    O      0.000000000         0.250000000         0.750000000
    O      0.250000000         0.000000000         0.750000000
    O      0.250000000         0.250000000         0.500000000
    O      0.500000000         0.250000000         0.750000000
    O      0.750000000         0.000000000         0.750000000
    O      0.750000000         0.250000000         0.500000000
    O      0.000000000         0.750000000         0.750000000
    O      0.250000000         0.500000000         0.750000000
    O      0.250000000         0.750000000         0.500000000
    O      0.500000000         0.750000000         0.750000000
    O      0.750000000         0.500000000         0.750000000
    O      0.750000000         0.750000000         0.500000000
    K_POINTS (automatic)
    3 3 3 1 1 1
    ```
    This input file instructs [**QE**](../../software-directory/modeling/quantum-espresso/overview.md) to perform a "self-consistent field" (scf) total energy computation for a supercell of  "Strontium Zirconate" (SrZrO3), in its equilibrium crystal structure (space group *Pnma* [^1]). (The reader is referred to the official documentation for the "PWscf" module of Quantum ESPRESSO [^2] [^3] for a description of the keyword parameters contained in our input example.)

Note that since we want to sweep the values of the lattice parameter, our template input file is using a variable on line 15 of the file:
```fortran
    celldm(1) = ${celldm1},
```
indicating that the lattice parameter `celldm(1)` for the underlying simple cubic [Bravais Lattice](../../properties-directory/structural/lattice.md) of the crystal structure would need be defined by the combined `run.sh` script, as explained below.

For pseudopotentials, our input file references (on lines 27-29) the default **"gbrv"** set of pseudopotentials[^4], available on our platform at `/export/share/pseudo`. To use them, we need to copy the pseudopotential files fto the working directory (more accurately, to the subdirectory `_pseudo`, as indicated on line 16). For our example, don't copy them right now, as they will be copied by the `run.sh` script below.
<!--
```bash
mkdir -p _pseudo
cp /export/share/pseudo/sr/gga/pbe/gbrv/1.0/us/sr_pbe_gbrv_1.0.upf ./_pseudo
cp /export/share/pseudo/zr/gga/pbe/gbrv/1.0/us/zr_pbe_gbrv_1.0.upf ./_pseudo
cp /export/share/pseudo/o/gga/pbe/gbrv/1.2/us/o_pbe_gbrv_1.2.upf ./_pseudo
```
-->

This completes the standard **QE** input setup. Note that in the case of [**QE**](../../software-directory/modeling/quantum-espresso/overview.md) a single input file describes both the atomic positions and all the calculation parameters; for other codes (e.g. [VASP](../../software-directory/modeling/vasp/overview.md)), multiple input files may need be created, as would be defined by the respective documentation. 

## 3. Batch Job Script

A [job batch script file](../../jobs-cli/batch-scripts/overview.md) is used to both submit the job to the `PBS` scheduler and to control whether the system should collect the job information and create job entry inside the web interface. [In this page](../../jobs-cli/batch-scripts/sample-scripts.md), the reader can find **sample job script files** for running  [Job simulations via Command Line Interface](../../jobs-cli/overview.md) that can be used as templates. The general structure of such scripts is further explained [here](../../jobs-cli/batch-scripts/general-structure.md).

!!!note "Keep job scripts simple"
    Please avoid using complex formatting and extra indentations or spacing in the job script. (See [this subsection](#31-importing-job-results-to-the-web-interface) for details.)

For our example, copy-paste the following template `PBS` script into a file `jobpbs.temp`:

```bash
#!/bin/bash
#PBS -A ${PROJECT} ### omit this line to charge the default project
#PBS -M ${EMAIL}
#PBS -N SrZrO3
#PBS -l nodes=1
#PBS -l ppn=16
#PBS -q SR
#PBS -j oe
#PBS -l walltime=02:00:00
#PBS -m abe

module add espresso
cd $PBS_O_WORKDIR
# $EXEC_CMD is set by the environment module
mpirun  -np $PBS_NP $EXEC_CMD pw.x -in srzro3_${celldm1}.in | tee srzro3_${celldm1}.out
```

Just like before, we are using template variables instead of the [project](../../jobs/projects.md) name, email, and the lattice-parameter-specific input and output filenames; those would all be set by `run.sh` below. The variables starting with `$PBS` are automatically set by the [resource manager](../../infrastructure/resource/overview.md), and are known as ["PBS Directives"](../../jobs-cli/batch-scripts/directives.md). The variable `$EXEC_CMD` is set by the  `module add` command.

The reader should note that within the `mpirun` line we make use of the `tee` command. This redirects the output of the simulation to both the standard output (abbreviated as "stdout") and to the output file simultaneously. Redirecting to "stdout" in this way allows the status of the job to be regularly updated and refreshed under the corresponding [Job Viewer](../../jobs/ui/viewer.md) in the [Web Interface](../../ui/overview.md), as we discuss next.

### 3.1 Importing Job Results to the Web Interface
In order to submit a new job through [command-line interface](../../cli/overview.md), and then view its progress and the corresponding output files under the [Web Interface](../../ui/overview.md), the following [directive](../../jobs-cli/batch-scripts/directives.md) can be added to the [job submission script](../../jobs-cli/batch-scripts/overview.md):
```bash
#PBS -R y
```

!!!note "Default Behavior"
    The `#PBS -R y` [directive](../../jobs-cli/batch-scripts/directives.md) is always enabled by default, but it can still be added manually as a failsafe. 

This directive instructs our software to automatically parse the output of the calculation, and send back the results to the web interface. After adding this directive, the job can then be [submitted](../../jobs-cli/actions/submit.md) as usual, and once the job starts executing, the user should be able to see the job entry in the web interface under [Jobs Explorer](../../jobs/ui/explorer.md), including the [status](../../jobs/status.md) of its execution, the produced files, and the extracted results.

This feature can conversely be *disabled* by inserting the following other directive option in the [job submission script](../../jobs-cli/batch-scripts/overview.md).

```bash
#PBS -R n
```

Note that currently only simple job scripts containing a single [execution command](../../jobs-cli/batch-scripts/general-structure.md#4.-commands) support import to web interface. Hence, the user is advised make sure that the script's content is straightforward and properly formatted. 


## 4. Shell Script

Since we want to sweep the the lattice parameter space, we'll use a script to prepare and submit not just one job, but separate jobs for each lattice parameter value.
The logic for parameter sweep calculations through shell scripting can be summarized as below (in pseudo code).

```bash
#!/bin/sh  
### DO NOT USE VERBATIM - PSEUDO-CODE ONLY!!!
for celldm1 in 5.81 5.82 5.83
do
    render_input_files(celldm1)
    render_job_submission_script(email, project)
    submit_job("cluster-001")
done
```
This logic can be implemented either by using `sed` command to explicitly process the template input and job files that we created above, or, alternatively, by incorporating the text of the template files into the shell script itself.

### 4.1 Using `sed` to Explicitly Process Template Files

This approach allows one to separate changes one may later want to make to the main input file from the changes to the `PBS` job script or to the shell script itself. Copy-paste the following script into a file `run.sh`:

```bash
#!/bin/sh

# Email to receive info on job progress
EMAIL="user@exabyte.io" 
## if not using default account, uncomment the next line and specify account name
#ACCOUNT= 

#  Copy Quantum ESPRESSO pseudopotentials:                 #
mkdir -p _pseudo
cp /export/share/pseudo/sr/gga/pbe/gbrv/1.0/us/sr_pbe_gbrv_1.0.upf ./_pseudo
cp /export/share/pseudo/zr/gga/pbe/gbrv/1.0/us/zr_pbe_gbrv_1.0.upf ./_pseudo
cp /export/share/pseudo/o/gga/pbe/gbrv/1.2/us/o_pbe_gbrv_1.2.upf ./_pseudo

#loop over parameter values, create job files, and submit them:
for celldm1 in 5.81 5.82 5.83
do
# ---------------------------------------------------------- #
#  Quantum ESPRESSO input file                               #
# ---------------------------------------------------------- #
    cat pw.in |sed "s/\${celldm1}/${celldm1}/g"> srzro3_${celldm1}.in
    cat jobpbs.temp |sed "s/\${EMAIL}/${EMAIL}/g; s/\${celldm1}/${celldm1}/g" > run_QE_${celldm1}.pbs
    qsub run_QE_${celldm1}.pbs
done
```

### 4.2 Alternative: Incorporating Templates into a Single Script
Instead of creating separate template files `pw.in` and `jobpbs.temp`, as we did above, one can also combine the above components into a single script, giving the following structure for the alternative version of `run.sh`:
??? example "Combined input script (click to expand)"
    ```bash
    #!/bin/sh
    
    # ---------------------------------------------------------- #
    #                                                            #
    #  Example job submission script for Exabyte.io platform     #
    #                                                            #
    #  Combines bash and resource management directives:         #
    #                                                            #
    #    1. creates input files for simulations                  #
    #    2. creates resource management scripts (PBS)            #
    #    3. submits resource management scripts for execution    #
    #                                                            #
    # ---------------------------------------------------------- #
    
    # Email to receive info on job progress
    EMAIL="user@exabyte.io"
    
    # ---------------------------------------------------------- #
    #  Quantum ESPRESSO pseudopotentials                         #
    # ---------------------------------------------------------- #
    mkdir -p _pseudo
    cp /export/share/pseudo/sr/gga/pbe/gbrv/1.0/us/sr_pbe_gbrv_1.0.upf ./_pseudo 
    cp /export/share/pseudo/zr/gga/pbe/gbrv/1.0/us/zr_pbe_gbrv_1.0.upf ./_pseudo
    cp /export/share/pseudo/o/gga/pbe/gbrv/1.2/us/o_pbe_gbrv_1.2.upf ./_pseudo
    
    for celldm1 in 5.81 5.82 5.83
    do
    # ---------------------------------------------------------- #
    #  Quantum ESPRESSO input file                               #
    # ---------------------------------------------------------- #
        cat > srzro3_${celldm1}.in <<EOF
    &control
        calculation = 'scf',
        restart_mode = 'from_scratch',
        prefix = 'srzro'
        tstress =.true.
        tprnfor=.true.
        outdir = './_outdir'
        wfcdir = './'
        prefix = '${celldm1}'
        pseudo_dir = './_pseudo'
     /
     &system
        ibrav = 1
        celldm(1) = ${celldm1},
        nat = 40
        ntyp = 3
        ecutwfc = 40
        ecutrho = 300
        tot_charge = 0
    /
    &electrons
       mixing_beta = 0.7
       conv_thr = 1.0d-8
    /
    ATOMIC_SPECIES
     Sr 87.62     sr_pbe_gbrv_1.0.upf
     Zr 91.224    zr_pbe_gbrv_1.0.upf
     O  15.999    o_pbe_gbrv_1.2.upf
    ATOMIC_POSITIONS (crystal)
    Zr     0.250000000         0.250000000         0.250000000
    Zr     0.750000000         0.250000000         0.250000000
    Zr     0.250000000         0.750000000         0.250000000
    Zr     0.750000000         0.750000000         0.250000000
    Zr     0.250000000         0.250000000         0.750000000
    Zr     0.750000000         0.250000000         0.750000000
    Zr     0.250000000         0.750000000         0.750000000
    Zr     0.750000000         0.750000000         0.750000000
    Sr     0.000000000         0.000000000         0.000000000
    Sr     0.500000000         0.000000000         0.000000000
    Sr     0.000000000         0.500000000         0.000000000
    Sr     0.500000000         0.500000000         0.000000000
    Sr     0.000000000         0.000000000         0.500000000
    Sr     0.500000000         0.000000000         0.500000000
    Sr     0.000000000         0.500000000         0.500000000
    Sr     0.500000000         0.500000000         0.500000000
    O      0.000000000         0.250000000         0.250000000
    O      0.250000000         0.000000000         0.250000000
    O      0.250000000         0.250000000         0.000000000
    O      0.500000000         0.250000000         0.250000000
    O      0.750000000         0.000000000         0.250000000
    O      0.750000000         0.250000000         0.000000000
    O      0.000000000         0.750000000         0.250000000
    O      0.250000000         0.500000000         0.250000000
    O      0.250000000         0.750000000         0.000000000
    O      0.500000000         0.750000000         0.250000000
    O      0.750000000         0.500000000         0.250000000
    O      0.750000000         0.750000000         0.000000000
    O      0.000000000         0.250000000         0.750000000
    O      0.250000000         0.000000000         0.750000000
    O      0.250000000         0.250000000         0.500000000
    O      0.500000000         0.250000000         0.750000000
    O      0.750000000         0.000000000         0.750000000
    O      0.750000000         0.250000000         0.500000000
    O      0.000000000         0.750000000         0.750000000
    O      0.250000000         0.500000000         0.750000000
    O      0.250000000         0.750000000         0.500000000
    O      0.500000000         0.750000000         0.750000000
    O      0.750000000         0.500000000         0.750000000
    O      0.750000000         0.750000000         0.500000000
    K_POINTS (automatic)
    3 3 3 0 0 0
    EOF
    
    # ---------------------------------------------------------- #
    #  Resource manager directives (PBS)                         #
    # ---------------------------------------------------------- #
        cat > run_QE_${celldm1}.pbs <<-EOF
    #!/bin/bash
    #PBS -M ${EMAIL}
    #PBS -N SrZrO3
    #PBS -l nodes=1
    #PBS -l ppn=16
    #PBS -q OR
    #PBS -j oe
    #PBS -l walltime=02:00:00
    #PBS -m abe
    
    module add espresso
    cd \$PBS_O_WORKDIR
    mpirun -np \$PBS_NP $EXEC_CMD pw.x -in srzro3_${celldm1}.in | tee srzro3_${celldm1}.out
    EOF
        qsub run_QE_${celldm1}.pbs
    done
    
    ```


## 5. Submitting and Viewing Submitted Jobs

After you put the content of the above file into a bash script called (for example)`run.sh`, make the script executable with `chmod a+x run.sh` command.
 
For a single job, you would normally [submit](../../jobs-cli/actions/submit.md) it using `qsub` command. However, as we made a script submitting a set of jobs sweeping parameter values, we only need to invoke our the script via the 
```bash
./run.sh
``` 
command (in this case, the `qsub` command is not necessary, since it is already included as part of `run.sh`, towards the end of the script). 

You can view the currently submitted jobs and their statuses in CLI with the `qstat` [command](../../jobs-cli/actions/check-status.md). You can also use `watch qstat` command for an automatically-refreshing version of `qstat`.

Assuming you have **not** added the `#PBS -R n` option to the script, you should also be able to see the job entry in the web interface under [Jobs Explorer](../../jobs/ui/explorer.md), and thus monitor the corresponding [status](../../jobs/status.md) of its execution. The reader is referred to the videos below for an explanation on how to inspect the simulation results under the [Web Interface](../../ui/overview.md) of our platform.


## Animations of Job Submission and Inspection

You can watch the following video, which illustrates job submission and inspection, starting from a pre-prepared `run.sh` script (using the single-script approach of [section 4.2](#42-alternative-incorporating-templates-into-a-single-script).) Here, the `run.sh` script is submitted for execution under the [Home Folder](../../infrastructure/clusters/directories.md) of `cluster-007`, and you can see that the [status of the job](../../jobs-cli/actions/check-status.md) inspected with the `watch qstat` command indicates that it is running on cluster number "007". Note that in the animation, only one lattice parameter has been tested for simplicity, and thus only one job has been launched and is returned by `qstat` in this case (scanning over all three lattice parameters, as in the original script shown above, would have correspondingly launched three distinct jobs). The video explains how to inspect the stdin/stdout while the job is running, and inspect the job files once the job completes.

<div class="video-wrapper">
<iframe class="gifffer" width="100%" height="100%" src="https://www.youtube.com/embed/sXKvHahZdoA" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

As another illustration, we also provide an animation of a submission of a [VASP Template Job](../../jobs-cli/batch-scripts/directories.md#job-templates). Here, we edit the [job submission script](../../jobs-cli/batch-scripts/overview.md) to insert the aforementioned `#PBS -R y` [directive](../../jobs-cli/batch-scripts/directives.md) for completeness (even though as explained earlier this directive is already enabled by default.) This ensures we can monitor the job [status](../../jobs/status.md) under [Jobs Explorer](../../jobs/ui/explorer.md) in [Web Interface](../../ui/overview.md), which we inspect towards the end of the animation.

<div class="video-wrapper">
<iframe class="gifffer" width="100%" height="100%" src="https://www.youtube.com/embed/p7ex0V0husY" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>


## Links

[^1]: [Strontium Zirconate, Materials Project Website](https://materialsproject.org/materials/mp-4387/)

[^2]: [PWscf User’s Guide, Document](https://www.quantum-espresso.org/Doc/pw_user_guide.pdf)

[^3]: [PWscf Input File Description, Website](https://www.quantum-espresso.org/Doc/INPUT_PW.html)

[^4]: [GBRV pseudopotential library, Official Website](https://www.physics.rutgers.edu/gbrv/)
