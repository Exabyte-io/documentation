<!-- by MH -->

This page explains how to run a basic simulation based on density functional theory to obtain an electronic bandstructure. We will study silicon in the standard diamond-centered cubic structure and use Quantum ESPRESSO as our simulation engine during this tutorial.

## Open default project

To create a new project, click on the "Project" link located in the sidebar/menu on the left. After that, click <i class="zmdi zmdi-plus-circle"></i> button in the top right corner, as shown in the animation below. Every user has a default project and we will use during this tutorial.

## Create a new job

`Jobs` belong to a `Project`. Therefore, to create a new job, while inside a project and click the <i class="zmdi zmdi-plus-circle"></i> button in the top right corner.

You will be taken to the "Job wizard" page where you can:

- Create a material (or choose one that you created and saved before) using the Materials Designer
- Choose and edit a simulation Workflow
- Setup the Compute Parameters.
For the sake of this tutorial, we will keep the default parameters at each step.

## Materials Designer

Materials Designer lets you create and save materials for future use. We will use the default structure of Silicon in diamond-centered cubic configuration

<img data-gifffer="/images/FirstJobCreate.gif" />

## Workflow

Simulations usually have multiple steps that need to be executed in a certain order. This step sequence is called a "Workflow". Go to the dropdown menu of "Workflows" and select "Bandstructure".  One can modify the input files for each part of the calculation, available under input tabs by double clicking on each file tab. One can also customize the workflow by adding and deleting individual "Units" by adding and deleting the tabs containing input files.  We will set the k-point density to 7x7x7.

<img data-gifffer="/images/FirstJobWorkflow.gif" />

## Compute parameters

This tab lets you set up the number of processors and the maximum time limit for your calculation to be run. Increasing the number of processors allocated to the job may accelerate the calculation if you have a larger unit cell.  For smaller cells there is likely a certain number of cores at which it becomes inefficient to add anymore cores to the simulation. We also need to set the maximum time limit for the calculation to properly schedule the allocation of compute resources to this job. We can also choose to be notified of the job status by clicking on our name in the "Notifications" section. Leave all parameters at their default values and click "Save calculation". If asked if you want to save a copy of the material since it already exists in the database, answer "No"

<img data-gifffer="/images/FirstJobCompute.gif" />

!!! Note "Summary"
    You have created your first material, simulation workflow, and allocated compute parameters for it. You saved your first job to be run in the future. Now you are ready to submit your job.

## Execute the job
After saving the job, you are redirected back to the project page. Here you can start the job and track its status.

### Submit for execution

Run the job by clicking the 3 vertical dots to the right of the "Pre-Submission" box and choosing the right-pointing triangle icon labeled "Run".

You will see the status changing from "pre-submission" to "submitted". This means that the job was submitted to our compute platform.  Depending on the load of your computer and the cloud services it may take some time to become "Active".

<img data-gifffer="/images/FirstJobSubmit.gif" />

### View summary

You can view the summary information for the job by clicking down-pointing arrow button next to the "actions" column while the job is active.

### View progress

You can click on the job name and monitor the progress of the job in real time.

<img data-gifffer="/images/FirstJobStatus.gif" />

### View results and access files

Job view screen lets you track the input parameters, output text, convergence parameters (total energy in this tutorial), and view the results of the calculation and download output files when finished.

<img data-gifffer="/images/FirstJobResults.gif" />

# Done

This is how you can run a band structure calculation using exabyte.io. For a more comprehensive tutorial on how to run a bandstructure calculation including editing input files click [here](/tutorials/band-structure.md).
