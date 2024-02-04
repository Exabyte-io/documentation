# Molecular dynamic using DeePMD

In this tutorial, we will walk you through the following steps:

1. Perform *ab-initio* molecular dynamics calculation using Quantum ESPRESSO
Car-Parrinello (`cp.x`) code
2. Prepare Quantum ESPRESSO output files for DeePMD using `dpdata`, split data
set into training and validation sets
3. Train DeePMD model, and freeze training results
4. Transform Quantum ESPRESSO structure into LAMMPS format
5. Perform classical molecular dynamics simulation using LAMMPS based on
potential and force fields predicted by DeePMD.


## (1) CP calculation

We perform *ab-initio* molecular dynamics calculation using Quantum ESPRESSO
Car-Parrinello (`cp.x`) program. We set `prefix` and unit name to `cp` so that
various output files have the same base name (e.g., cp.out, cp.for, etc.). Some
of the CP parameters such as the number of steps, time step, etc. can be set in
the **Important Settings** tab. Users can modify or add new parameters directly
on the template via edit unit.

For this demonstration, we create a new structure from the scratch using
material designer. We use water molecule with simple cubic structure.


## (2) Prepare data sets for DeePMD

We will Python script and `dpdata` to load the Quantum ESPRESSO output obtained
in the previous step. We will split the available number of molecular dynamics
steps into training and validation sets (80% and 20%, respectively).


## (3) Run DeePMD model

We need to specify the descriptor and related model parameters here. After the
training, the output is saved into `graph.pb`.


## (4) Prepare LAMMPS structure

Here we will again use Python script to prepare input structure for LAMMPS
calculation. We use `dpdata` to convert the Quantum ESPRESSO input file in the
first step into LAMMPS format. User can extend the structure, build supercell,
or hardcode the structure and save it to `system.lmp` file.


## (5) LAMMPS calculation

Finally, we perform classical molecular dynamics calculation using LAMMPS. The
output is written to `system.dump`. Various output files are placed in the
**Files** tab of the jobs page. Users may launch a Jupyter Notebook session in
our platform to further analyze output files.

## Step-by-step screenshare video

In the below animation, we walk you through the whole workflow process.

<div class="video-wrapper">
<iframe class="gifffer" width="100%" height="100%" src="https://www.youtube.com/embed/33PykNO8QlQ" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>
