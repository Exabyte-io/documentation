# WIEN2k

WIEN2k allows to perform electronic structure calculations of solids using density functional theory (DFT). It is based on the full-potential (linearized) augmented plane-wave ((L)APW) + local orbitals (lo) method, one among the most accurate schemes for band structure calculations. WIEN2k is an all-electron scheme including relativistic effects and has many features. More information about WIEN2k can be retrieved under its official website [^1].

## Job Script File

In order to run WIEN2k one should use a job script file similar to the one given below and adjust machines file as necessary.

```bash
#!/bin/bash

# ---------------------------------------------------------------- #
#                                                                  #
#  Example job submission script for Exabyte.io platform           #
#                                                                  #
#  Shows resource manager directives for:                          #
#                                                                  #
#    1. the name of the job                (-N)                    #
#    2. the number of nodes to be used     (-l nodes=)             #
#    3. the number of processors per node  (-l ppn=)               #
#    4. the walltime in dd:hh:mm:ss format (-l walltime=)          #
#    5. queue                              (-q) D, OR, OF, SR, SF  #
#    6. merging standard output and error  (-j oe)                 #
#    7. email about job abort, begin, end  (-m abe)                #
#    8. email address to use               (-M)                    #
#                                                                  #
#  For more information visit https://docs.exabyte.io/cli/jobs     #
# ---------------------------------------------------------------- #

#PBS -N WIEN2K
#PBS -j oe
#PBS -l nodes=1
#PBS -l ppn=16
#PBS -l walltime=01:00:00
#PBS -q OR
#PBS -m abe
#PBS -M YOUR_EMAIL_ADDRESS

#
# create machines file for WIEN2K
#
machines=`cat $PBS_NODEFILE | sort -u`
echo -n "lapw0: " > $PBS_O_WORKDIR/.machines
for machine in $machines; do
    cpucnt=`grep "^$machine$" $PBS_NODEFILE | wc -l`
    echo -n "$machine:$cpucnt " >> $PBS_O_WORKDIR/.machines
done
echo >> $PBS_O_WORKDIR/.machines
for machine in $machines; do
    cpucnt=`grep "^$machine$" $PBS_NODEFILE | wc -l`
    echo "1:$machine:$cpucnt" >> $PBS_O_WORKDIR/.machines
done
echo granularity:1 >> $PBS_O_WORKDIR/.machines
echo extrafine:1 >> $PBS_O_WORKDIR/.machines

#
# load module
#
module add wien2k/171-i-174-impi-044

#
# go to the job working directory
#
cd $PBS_O_WORKDIR

#
# run the calculation
#
runsp_lapw -p -ec 0.00001 
```

## Generating Machines File

Reader should note the below code in the above script. The code is used to generate the machines file to run WIEN2k in parallel mode. Readers are referred to the official user's guide available at [^2] for more information about machines file format. In our queueing system the list of machines provided to the job can be obtained from `$PBS_NODEFILE` environment variable containing line delimited list of nodes allocated to the job.

```bash
machines=`cat $PBS_NODEFILE | sort -u`
echo -n "lapw0: " > $PBS_O_WORKDIR/.machines
for machine in $machines; do
    cpucnt=`grep "^$machine$" $PBS_NODEFILE | wc -l`
    echo -n "$machine:$cpucnt " >> $PBS_O_WORKDIR/.machines
done
echo >> $PBS_O_WORKDIR/.machines
for machine in $machines; do
    cpucnt=`grep "^$machine$" $PBS_NODEFILE | wc -l`
    echo "1:$machine:$cpucnt" >> $PBS_O_WORKDIR/.machines
done
echo granularity:1 >> $PBS_O_WORKDIR/.machines
echo extrafine:1 >> $PBS_O_WORKDIR/.machines
```

## Links

[^1]: [WIEN2k, Official Website](http://susi.theochem.tuwien.ac.at/)

[^2]: [WIEN2k Official User's Guide](http://susi.theochem.tuwien.ac.at/reg_user/textbooks/usersguide.pdf)
