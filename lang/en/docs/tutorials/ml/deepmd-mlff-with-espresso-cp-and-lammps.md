# Obtain force field with DeePMD to use in LAMMPS

In this tutorial, we demonstrate how to perform large-scale molecular dynamics
simulation using Density Functional Theory, DeePMD, and LAMMPS in Mat3ra web
platform. The workflow consists of the following steps:

1. Perform *ab-initio* molecular dynamics calculation using Quantum ESPRESSO
Car-Parrinello (`cp.x`) program
2. Prepare Quantum ESPRESSO output files for DeePMD using `dpdata`, split data
set into training and validation sets
3. Train DeePMD model, and freeze training results
4. Transform Quantum ESPRESSO structure into LAMMPS format
5. Perform classical molecular dynamics simulation using LAMMPS based on
potential and force fields predicted by DeePMD.


## Create Structure

For this demonstration, we create a new structure from scratch using material
designer. Navigate to **Materials** page from the left sidebar, and click create
new material. We may clone the default structure.

![DeePMD clone structure](/images/tutorials/deepmd/deepmd-clone-structure.webp "DeePMD clone structure")

![DeePMD edit material](/images/tutorials/deepmd/deepmd-edit-material.webp "DeePMD edit material")

We use water molecule with simple cubic structure. Set lattice parameters,
atomic positions, and click **apply edits**. Finally, go to **Input/Output**
menu, and save the structure. Alternatively, user can import CIF or POSCAR
structure files.


## Create Workflow

### (1) CP calculation

We perform *ab-initio* molecular dynamics calculation using Quantum ESPRESSO
Car-Parrinello (`cp.x`) program. Navigate to workflows page, and click create
new workflow.

![DeePMD create workflow](/images/tutorials/deepmd/deepmd-create-workflow.webp "DeePMD create workflow")

Click **edit** unit. On the unit modal, expand the details pane, and select
executable to **cp.x** We set `prefix` and unit name to `cp` so that various
output files have the same base name (e.g., cp.out, cp.for, etc.).

![DeePMD edit unit](/images/tutorials/deepmd/deepmd-edit-unit.webp "DeePMD edit unit")

![DeePMD edit unit modal](/images/tutorials/deepmd/deepmd-edit-unit-modal.webp "DeePMD edit unit modal")

Some of the CP parameters such as the number of steps, time step, etc. can be
set in the **Important Settings** tab. Users can modify or add additional
parameters directly on the template on the unit modal. Close the unit modal, and
return to workflows page. Set Quantum ESPRESSO version (e.g., 7.3) and build
(e.g., GNU).

For the next steps, we need to use another executable (deepmd), so we will add
new subworkflow and select deepmd application.

![DeePMD add subworkflow](/images/tutorials/deepmd/deepmd-add-subworkflow.webp "DeePMD add subworkflow")


### (2) Prepare data sets for DeePMD

We will use Python script and `dpdata` to load the Quantum ESPRESSO output files
obtained in the previous CP calculation step. Add first unit to deepmd
subworkflow.

![DeePMD set application and add units](/images/tutorials/deepmd/deepmd-application-and-units.webp "DeePMD set application and add units")

Select executable to **python** and flavor to **espresso_cp_to_deepmd**.

![DeePMD edit python script](/images/tutorials/deepmd/deepmd-edit-python-script.webp "DeePMD edit python script")

We will split the available number of molecular dynamics steps into training and
validation sets (80% and 20%, respectively). One can modify the python script/
template directly in the unit modal, and adjust the ratio between sets.


### (3) Run DeePMD model

We need to specify the descriptor and related model parameters here. Append
another execution unit to deepmd subworkflow. This time select **dp**
executable. Set the descriptor and various model parameters. After the training
step is executed, the output is saved into `graph.pb` file.


### (4) Prepare LAMMPS structure

Here we will again use Python script to prepare input structure for LAMMPS
calculation. Again add new executable unit, select **python** executable and
**espresso_to_lammps_structure**. We use `dpdata` to convert the Quantum
ESPRESSO input file in the first step into LAMMPS format. User can extend the
structure, build supercell, or hardcode the structure and save it to
`system.lmp` file.


### (5) LAMMPS calculation

Finally, we perform classical molecular dynamics calculation using LAMMPS.
LAMMPS parameters can be adjusted in `in.lammps` input template. Add the final
unit, and select **lmp** executable. We use deepmd pair style. We can adjust
LAMMPS parameters in the template. The LAMMPS output is written to
`system.dump`.

![DeePMD workflow](/images/tutorials/deepmd/deepmd-workflow.webp "DeePMD workflow")


## Create and submit job

Navigate to Jobs page from the left sidebar. Click create new job. Select
material (in our case, H<sub>2</sub>O structure we created), select
molecular-dynamics workflow that we created in the previous step. Navigate
**compute** tab adjust compute parameters such as queue, number of nodes and
processors. Submit job for execution. Once the job is completed, various output
files are placed under the **Files** tab of the jobs page. Users may launch a
Jupyter Notebook session in our platform to further analyze output files.

![DeePMD create job](/images/tutorials/deepmd/deepmd-create-job.webp "DeePMD create job")


## Step-by-step screenshare video

In the below animation, we walk you through the whole workflow process.

<div class="video-wrapper">
<iframe class="gifffer" width="100%" height="100%" src="https://www.youtube.com/embed/daTwJyMPIvE" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>
