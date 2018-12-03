#!/bin/bash

# ---------------------------------------------------------- #
#                                                            #
#  Example job submission script for Exabyte.io platform     #
#                                                            #
#  Shows resource manager directives for:                    #
#                                                            #
#    1. the name of the job                (-N)              #
#    2. the number of nodes to be used     (-l nodes=)       #
#    3. the number of processors per node  (-l ppn=)         #
#    4. queue                              (-q D) or OR, OF  #
#    5. merging standard output and error  (-j oe)           #
#    6. email about job abort, begin, end  (-m abe)          #
#    7. email address to use               (-M)              #
#    8. the walltime in dd:hh:mm:ss format (-l walltime=)    #
#                                                            #
# ---------------------------------------------------------- #

#PBS -N job_name
#PBS -l nodes=1
#PBS -l ppn=2
#PBS -q D
#PBS -j oe
#PBS -l walltime=00:10:00
#PBS -m abe
#PBS -M name@domain.com

MODULES="module names separated by single space: module1 module2"

cd $PBS_O_WORKDIR
module load $MODULES
mpirun -np $PBS_NP ./my_executable






