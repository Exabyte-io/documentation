# Quickstart

This page explains how to run a basic simulation based on [density functional theory](http://en.wikipedia.org/wiki/Density_functional_theory) to obtain an [electronic bandstructure](http://en.wikipedia.org/wiki/Electronic_band_structure). We will be studying silicon in face-centered cubic structure and using [Quantum ESPRESSO](quantum-espresso.org) as our simulation engine during this tutorial.

## Create a new project or use default

To create a new project, one needs to click on the "Project" link located in the sidebar on the left. After that, click "(+)" button in the top right corner, as it is shown in the animation below. Every user has a default project by default, we can use it futher in this tutorial.


## Create a New Job

Jobs belong to a Project. Therefore, to create a new job, one needs to be inside one of the projects and click "(+)" button in the top right corner.


You will be taken to a the "Job wizard" - a page where you can create a material (or choose one that you created and saved before) using [Materials Designer](), choose and edit a simulation [Workflow](), and setup the [Compute Parameters](). For the sake of this tutorial, we will keep the default parameters at each step.

### Materials Designer

Materials Designer lets you create and save materials for future use. The default structure here corresponds to Silicon in face-centered cubic
configuration. We will leave it so.

<br>
<img src="../images/job-create-material.gif">
<br>

### Workflow

Simulations usually have multiple steps that need to be executed in a certain order. This step sequence is called a "Workflow". By default the first workflow - "Bandstructure" - is selected. One can modify the input files for each part of the calculation,  available under input tabs. One can also customize the workflow by adding and deleting individual "Units" by adding and deleting the tabs containing input files. We will leave parameters at their default values here again.

<br>
<img src="../images/job-create-workflow.gif">
<br>

### Compute parameters

This tab lets you set up the compute parameters: number of processors and the maximum time limit for your calculation to be run for. Increasing the number of processors allocated to the job lets accelerate calculations for materials with large unit cells, for example. We need to set the maximum time limit for the calculation to properly schedule the allocation of compute resources to this job. Again - we will leave all parameters at their default values and click "Save calculation".

<br>
<img src="../images/job-create-compute.gif">
<br>

### Summary

You have created your first material, simulation workflow and allocated compute parameters for it. You saved your first job to be run in the future. Next steps explains how do that.

## Run the Job

After saving the job, you are redirected back to the project page. Here you can start the job and track its status.

### Submit for execution

Let's run the job by clicking the checkbox on the left and choosing the left-pointing triangle icon at the top.

<br>
<img src="../images/job-run-start.gif">
<br>

You will see the status changing from "pre-submission" to "submitted", and to "active" within a few seconds. This means that the job was submitted to our compute platform and was started successfully.

### View summary

You can view the summary information for the job by clicking down-pointing arrow button next to the "actions" column while the job is active.

<br>
<img src="../images/job-run-summary.gif">
<br>


### View progress

You can click on the job name and monitor the progress of the job in real time.

<br>
<img src="../images/job-run-status.gif" width="800">
<br>

### View results and access output files

Job view screen lets you track the input parameters, output text, convergence parameters (total energy in this tutorial), and view the results of the calculation and download output files when finished.

<br>
<img src="../images/job-run-results.gif" width="800">
<br>

## Done

This is how you can run a band structure calculation using exabyte.io.
