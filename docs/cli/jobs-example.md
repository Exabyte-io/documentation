<!-- by TB -->

This page explains how to run a command-line job for Quantum ESPRESSO. We will use a template input file and a bash script to sweep the lattice parameter space for a given structure.

# Input file

We start with preparing an input file. Below is example input file with pseudopotential paths set to use the default [gbrv](https://www.physics.rutgers.edu/gbrv/) set.

```fortran
&control
    calculation = 'scf',
    restart_mode = 'from_scratch',
    prefix = 'STO_exc1'
    tstress =.true.
    tprnfor=.true.
    outdir = './'
    wfcdir = './'
    prefix = '__prefix__'
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

Note that we are using a template variable in place of `celldm1`.

In order to use the above file we will need to copy the pseudopotential files into the current working directory:

```bash
cp /export/share/pseudo/si/gga/pbe/gbrv/1.0/us/sr_pbe_gbrv_1.0.upf .
cp /export/share/pseudo/zr/gga/pbe/gbrv/1.0/us/zr_pbe_gbrv_1.0.upf .
cp /export/share/pseudo/o/gga/pbe/gbrv/1.0/us/o_pbe_gbrv_1.2.upf .
```

# Job submission script

Second, we prepare a submission script:

```bash
#!/bin/bash
#PBS -A ${PROJECT}
#PBS -M ${EMAIL}
#PBS -N job_name
#PBS -l nodes=1
#PBS -l ppn=2
#PBS -q D
#PBS -j oe
#PBS -l walltime=01:00:00
#PBS -m abe

module add espresso
cd $PBS_O_WORKDIR
mpirun -np $PBS_NP pw.x -in pw.in > pw.out
```

Just like above, we are using template variables again instead of the project name and email. Variables starting with `$PBS` are automatically set by the resource manager.

# Bash script

The logic for parameter sweep calculations can be summarized as below (in pseudo code):

```bash
#!/bin/sh
for celldm1 in 1.81 1.82 1.83 1.84 1.85
do
    render_input_file(celldm1)
    render_job_submission_script(email, project)
    submit_job("cluster-001")
done
```

When combined together, all the above gives:

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
EMAIL="info@exabyte.io"

# Account+Project to run this calculation from
# Full name available from the project page in the web application
# Pattern: `<accountName>-<projectName>`:
#   - for organizations accountName = organization name, eg. "exabyte-io"
#   - for individual users accountName = user name, eg. "steve"
ACCOUNT="exabyte-io-exabyte-io"

# ---------------------------------------------------------- #
#  Quantum ESPRESSO pseudopotentials                         #
# ---------------------------------------------------------- #
cp /export/share/pseudo/sr/gga/pbe/gbrv/1.0/us/sr_pbe_gbrv_1.0.upf .
cp /export/share/pseudo/zr/gga/pbe/gbrv/1.0/us/zr_pbe_gbrv_1.0.upf .
cp /export/share/pseudo/o/gga/pbe/gbrv/1.2/us/o_pbe_gbrv_1.2.upf .

for celldm1 in 1.81 1.82 1.83 1.84 1.85
do
# ---------------------------------------------------------- #
#  Quantum ESPRESSO input file                               #
# ---------------------------------------------------------- #
    cat > srzro3_${celldm1}.in <<EOF
&control
    calculation = 'scf',
    restart_mode = 'from_scratch',
    prefix = 'STO_exc1'
    tstress =.true.
    tprnfor=.true.
    outdir = './'
    wfcdir = './'
    prefix = '__prefix__'
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
EOF

# ---------------------------------------------------------- #
#  Resource manager directives (PBS)                         #
# ---------------------------------------------------------- #
    cat > run_QE_${celldm1}.pbs <<-EOF
#!/bin/bash
#PBS -A ${PROJECT}
#PBS -M ${EMAIL}
#PBS -N job_name
#PBS -l nodes=1
#PBS -l ppn=2
#PBS -q D
#PBS -j oe
#PBS -l walltime=01:00:00
#PBS -m abe

module add espresso
cd \$PBS_O_WORKDIR
mpirun -np \$PBS_NP pw.x -in srzro3_${celldm1}.in > srzro3_${celldm1}.out
EOF
    qsub run_QE_${celldm1}.pbs
done

```

We can put the content of the above file into a bash script (`run.sh`) and invoke it to submit the jobs in a set (`sh run.sh`).

# View submitted jobs

View currently submitted jobs with `qstat` command. The output is simiiar to:

```
[steve@bohr.exabyte.io:~]$ qstat
JOBID              USERNAME    QUEUE    JOBNAME    STATE    MEMORY    USEDTIME    WALLTIME      NODES    CPU
-----------------  ----------  -------  ---------  -------  --------  ----------  ----------  -------  -----
11665.cluster-001  steve       D        my_job     C        0kb       00:00:10    00:10:00          1      1
11666.cluster-001  steve       OR       my_job     R        1235kb    00:00:10    00:10:00          1      1
```
