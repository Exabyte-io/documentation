# Run Jupyter Notebook

This tutorial page explains how to create a Jupyter Notebook environment through [Jupyter Lab](../../software-directory/scripting/jupyter-lab/overview.md) application.

## Create job

To create a new job, click on the **Create Job** link located on the [left-hand Sidebar](../../ui/left-sidebar.md) which takes you to the [Job Designer](../../../jobs-designer/overview.md) page where you can configure Jupyter Notebook environment.

## Choose Workflow

Jupyter Notebook installation and configuration is handled through the Jupyter Notebook [workflow](../../../workflows/overview.md) that should be [imported](../../../workflows/actions/copy-bank.md) from the [Workflows Bank](../../../workflows/bank.md) into the account-owned [collection](../../../accounts/collections.md) before the job is created and then get [selected](../../../jobs-designer/actions-header-menu/select-workflow.md) and added to the [job being created](../../../jobs-designer/workflow-tab.md).

## Adjust Jupyter Notebook Environment

Jupyter Notebook is installed inside a Python virtual environment with no additional packages. The environment can be customized by navigating to the [workflow tab](../../jobs-designer/workflow-tab.md) and adjusting the **configure.sh** script located in **notebook** unit. 

## Access IPython Notebooks

Jupyter Notebook is started on the account [Dropbox](../../data-in-objectstorage/dropbox.md) directory to access previously uploaded/created IPython notebooks.

## Submit Job

Before [submitting](../../../jobs/actions/run.md) the [job](../../../jobs/overview.md), you should click on the ["Compute" tab](../../../jobs-designer/compute-tab.md) of [Job Designer](../../../jobs-designer/overview.md) and inspect the [compute parameters](../../../infrastructure/compute/parameters.md) included therein.

## Access Jupyter Notebook

When the job becomes active, navigate to the [workflow tab](../../jobs-designer/workflow-tab.md) and open the **notebook** unit. 
You should wait for the Jupyter Notebook environment to start and then click on **Notebook** or **Lab** tabs to access the environment.


!!! Note "Jupyter Notebook URL Inside Output File"
    Do not use the URL printed in the output file as the notebook can not be accessed directly for security reasons.

## Stop Jupyter Environment

Jupyter Notebook environment can be stopped either by clicking on **Quite** button in Jupyter Notebook main page or [terminating](../../jobs/actions/terminate.md) the job. In either case, please make sure to save any changes you have made before stopping the notebook as unsaved changes will be lost otherwise.

## Animation

We demonstrate the above-mentioned steps involved in running Jupyter Notebook environment in the following animation.

<div class="video-wrapper">
<iframe class="gifffer" width="100%" height="100%" src="https://www.youtube.com/embed/G5L52T6fjeQ" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>
