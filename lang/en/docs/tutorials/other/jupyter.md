# Jupyter Notebook

This tutorial page explains how to create a Jupyter Notebook environment through [Jupyter Lab](../../software-directory/scripting/jupyter-lab/overview.md) application following the below steps.

## Generate RESTFul API Tokens

The Jupyter notebook environment in the present tutorial is used to run an IPython notebook from [Exabyte API Examples Repository](../../rest-api/api-examples.md) in which a connection is made to the RESTFul API to retrieve a list of materials. In order to establish the connection, one should generate RESTFul API tokens following the steps described in [here](../../rest-api/authentication.md). 

## Upload IPython Notebooks

Jupyter Notebook is started on the account [Dropbox](../../data-in-objectstorage/dropbox.md) directory. This will provide users with access to previously uploaded/created IPython notebooks. Here, **settings.py** file which contains essentials variables to configure RESTFul API endpoints and **get_materials_by_formula.ipynb** from [Exabyte API Examples Repository](../../rest-api/api-examples.md) are uploaded to Dropbox to be later used inside the Jupyter notebook environment. 

## Create job

A simulation job is required to launch a Jupyter notebook. To create a new job, click on the **Create Job** link located on the [left-hand Sidebar](../../ui/left-sidebar.md) which takes you to the [Job Designer](../../jobs-designer/overview.md) page where you can configure Jupyter Notebook environment.

## Choose Workflow

Jupyter Notebook installation and configuration is handled through the Jupyter Notebook [workflow](../../workflows/overview.md) that should be [imported](../../workflows/actions/copy-bank.md) from the [Workflows Bank](../../workflows/bank.md) into the account-owned [collection](../../accounts/collections.md) before the job is created. This workflow can later be [selected](../../jobs-designer/actions-header-menu/select-workflow.md) and added to the [job being created](../../jobs-designer/workflow-tab.md).

## Adjust Jupyter Notebook Environment

Jupyter Notebook is installed inside a Python virtual environment with no additional packages. The environment can be customized by navigating to the [workflow tab](../../jobs-designer/workflow-tab.md) and adjusting the **configure.sh** script located in **notebook** unit. Here, we install [Exabyte API Client](../../rest-api/api-client.md) Python package to connect to Exabyte RESTFul API. 

## Submit Job

Before [submitting](../../jobs/actions/run.md) the [job](../../jobs/overview.md), you should click on the ["Compute" tab](../../jobs-designer/compute-tab.md) of [Job Designer](../../jobs-designer/overview.md) and inspect the [compute parameters](../../infrastructure/compute/parameters.md) included therein.

## Access Jupyter Notebook

The Jupyter notebook can be accessed When the job is active by navigating to the [workflow tab](../../jobs-designer/workflow-tab.md) and opening the **notebook** unit. Wait for the Jupyter Notebook to start as installation and configuration process takes time and then click on **Notebook** or **Lab** tabs to access the environment.

!!! Note "Jupyter Notebook URL Inside Output File"
    Do not use the URL printed in the output file as the notebooks can not be accessed via printed URL for security reasons.

## Save Jupyter Notebooks

Make sure to save and checkpoint the notebook after introducing any changes. The "save and checkpoint" Jupyter action overwrites the original notebook loaded from Dropbox and saves a copy of the notebook inside **checkpoints** directory located in the [job working directory](../../jobs-cli/batch-scripts/directories.md#working-directory). The checkpoints will be later accessible through the [Job Files Explorer](../../data-in-objectstorage/files.md) tab.

## Stop Jupyter Environment

Jupyter Notebook environment can be stopped by either clicking on **Quit** button in Jupyter Notebook main page or [terminating](../../jobs/actions/terminate.md) the job. In either case, Make sure to save any changes you have made before stopping the notebook as unsaved changes will be lost otherwise.

## Animation

We demonstrate the above-mentioned steps involved in creating Jupyter Notebook environment in the following animation.

<div class="video-wrapper">
<iframe class="gifffer" width="100%" height="100%" src="https://www.youtube.com/embed/G5L52T6fjeQ" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>
