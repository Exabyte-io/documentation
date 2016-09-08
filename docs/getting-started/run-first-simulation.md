<!-- by MH -->

This page explains how to run a basic simulation based on density functional theory to obtain an electronic bandstructure. We will be study silicon in the standard diamond-centered cubic structure and use Quantum ESPRESSO as our simulation engine during this tutorial.

## Create a new project or use default

To create a new project, click on the "Project" link located in the sidebar/menu on the left. After that, click "(+)" button in the top right corner, as shown in the animation below. Every user has a default project and we will use during this tutorial.

## Create a new job

`Jobs` belong to a `Project`. Therefore, to create a new job, while inside a project and click the <i class="zmdi zmdi-plus-circle"></i> button in the top right corner.

You will be taken to the "Job wizard" page where you can:

- Create a material (or choose one that you created and saved before) using the Materials Designer
- Choose and edit a simulation Workflow
- Setup the Compute Parameters.
For the sake of this tutorial, we will keep the default parameters at each step.

## Materials Designer

Materials Designer lets you create and save materials for future use. We will use the default structure of Silicon in diamond-centered cubic configuration

## Workflow

Simulations usually have multiple steps that need to be executed in a certain order. This step sequence is called a "Workflow". By default the first workflow - "Bandstructure" - is selected. One can modify the input files for each part of the calculation, available under input tabs by double clicking on each file tab. One can also customize the workflow by adding and deleting individual "Units" by adding and deleting the tabs containing input files.

## Compute parameters

This tab lets you set up the compute parameters of the number of processors and the maximum time limit for your calculation to be run. Increasing the number of processors allocated to the job may accelerate the calculation if you have a larger unit cell.  For smaller cells there is likely a certain number of cores at which it becomes inefficent to add anymore cores to the simulation. We also need to set the maximum time limit for the calculation to properly schedule the allocation of compute resources to this job. Leave all parameters at their default values and click "Save calculation".

## Summary

You have created your first material, simulation workflow, and allocated compute parameters for it. You saved your first job to be run in the future. Now you are ready to submit your job.

## Execute the job
After saving the job, you are redirected back to the project page. Here you can start the job and track its status.

### Submit for execution

Run the job by clicking the checkbox on the left and choosing the left-pointing triangle icon at the top.

You will see the status changing from "pre-submission" to "submitted", and to "active". This means that the job was submitted to our compute platform and was started successfully.  Depending on the load of your computer and the cloud services it may take some time to become active.

### View summary

You can view the summary information for the job by clicking down-pointing arrow button next to the "actions" column while the job is active.

### View progress

You can click on the job name and monitor the progress of the job in real time.

### View results and access output files

Job view screen lets you track the input parameters, output text, convergence parameters (total energy in this tutorial), and view the results of the calculation and download output files when finished.

# Done
This is how you can run a band structure calculation using exabyte.io.

*/ Basic information on where to click to run a first simulation for the electronic band structure of Si, similar to what we have in https://docs.exabyte.io/tutorials/quickstart/. No advanced options discussed yet./*
