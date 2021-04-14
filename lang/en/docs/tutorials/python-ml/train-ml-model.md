# Machine Learning: Train a Neural Network

This tutorial demonstrates how to train a a [multilayer perceptron](https://en.wikipedia.org/wiki/Multilayer_perceptron)
for regression
using [SciKit-Learn](https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPRegressor.html).

## 1. Acquire Training Data

The data we use in this tutorial is taken from a [recent model](http://doi.org/10.1126/sciadv.aax5101) of small molecule
adsorption to transition metal nanoparticles. Specifically, we use DFT-calculated values for the adsorption energy of
·CH<sub>3</sub>, CO, and ·OH radicals to Ag, Au, and Cu nanoparticles ranging in size from 55 to 172 atoms.

<a href="/extra/files/data_to_train_with.csv" download="data_to_train_with.csv">This File</a> contains the data we will
use in this tutorial. A sample of the first 5 lines in the file can be found below:

|PBE_BE_eV|CE_Local_eV|ChemPot_eV|MADS_eV
|-----|----|---|----
|-1.39|-2.38|-4.96|-2.10
|-1.11|-3.35|-4.96|-2.10
|-0.95|-4.81|-4.96|-2.10
|-0.74|-4.60|-4.96|-2.10

## 2. Upload the Training Data

In order to upload training data, we first click the `Dropbox` button in the [left sidebar](../../ui/left-sidebar.md).
This will bring us to the [Dropbox Page](../../jobs/ui/files-tab.md). We can then click the "Upload" button, circled
below:

![Dropbox Page with Upload](../../images/tutorials/dropbox_page_with_upload_circled.png "Dropbox page with upload circled")

Then, when the browser's upload window appears, we navigate to where we downloaded the file in section 1, and select it
for upload. If the upload was successful, the file will then be visible in the dropbox.

## 3. Copy the "Python ML Train Regression" Workflow from the Workflow Bank

Next, we select the`Bank Worfklows` button in the [left sidebar](../../ui/left-sidebar.md), which brings us to
the [Bank Workflows Page](../../workflows/bank.md). We then search for the "Python ML Train Regression" workflow owned
by the "Curators" account, and [copy it to our account](../../workflows/actions/copy-bank.md).

A diagram and detailed description of this workflow can be found
[here](../../software-directory/machine-learning/python-ml/components.md).

## 4. Create the ML Job

Next, we can create a new job by selecting the `Create Job` button in the [left sidebar](../../ui/left-sidebar.md). This
will bring us to a new job on the [Job Designer](../../jobs-designer/overview.md) page.

First, we will give the job a friendly name, such as "Python ML Tutorial" (see below). Then, we will click
the [Actions Button](../../jobs-designer/header-menu.md#Actions) (the three vertical dots in the upper-right of the job
designer), and choose "Select Workflow."

![Job Designer with Circles](../../images/tutorials/job_designer_with_python_ml_name_and_three_dots_circled.png "Job designer page")

This will bring up the [Select Workflow](../../jobs-designer/actions-header-menu/select-workflow.md) dialogue. We then
search for "Python ML Train" and select it.

## 5. Select the Dataset

The job designer changes now that our ML Training workflow is selected. The "Materials" tab has now been replaced with
a "Dataset" tab. Just as the "Materials" tab shows a preview of the materials the job will use, the "Dataset" tab shows
a preview of the dataset once it is selected.

To select a dataset, click the [Actions Button](../../jobs-designer/header-menu.md#Actions) (the three vertical dots in
the upper-right of the job designer) and choose "Select Dataset." This will bring up a files explorer containing all
files presently on the dropbox. Choose the training set we uploaded earlier, "data_to_train_with.csv."

A preview of the data then appears on the dataset tab, indicating that the data has successfully been loaded.

## 6. Configure the Workflow

We now chosen our ML workflow and training set. Select the [Workflows Tab](../../jobs-designer/workflow-tab.md), and we
can see our training workflow.

We can see two [subworkflows](../../workflows/components/subworkflows.md) available: `Set Up the Job`
and `Machine Learning`.

The `Set Up the Job` contains instructions to copy in the training data.

!!!warning "A Word of Caution"
    The `Set Up the Job` subworkflow is automatically re-configured during the training process. Modifying it can disrupt
    creation of the Predict workflow, leading to inaccurate results, or a failure to generate a predict workflow.

Select the `Machine Learning` subworkflow by clicking on it. The following workflow units should now be visible:

0. `Setup Packages and Variables` - Configures the job and downloads all required packages with `pip`
1. `Data Input` - Reads the training data from disk
2. `Data Standardize` - Scales the data such that it has mean 0 and standard deviation 1
3. `Model Train and Predict` - Handles model training, and prediction
4. `Parity Plot` - Draws a plot of model predictions versus training data, and saves it to the disk. This plot is shown
   on the Results tab.

We will begin by configuring our Machine Learning subworkflow. To begin, select the "Important Settings" portion of the
workflow editor. Then, set `target_column_name` to "PBE_BE_eV" to define the target column of the training set.

![SettingsPy](../../images/tutorials/settings_py_with_target_colname_circled.png "Settings with Colname Selected")

Then, go back to the "Overview" portion of the workflow editor. We can now demonstrate how a workflow unit's parameters
can be changed. For this tutorial, we will set our neural network to have 2 hidden layers of 100 layers each, and we
will train for 5000 iterations.

Begin by selecting the `Model Train and Predict` workflow unit, as below:

![ML Train and Predict](../../images/tutorials/workflows_tab_with_ml_train_subworkflow_and_train_unit_circled.png "Workflow tab with ml train unit circled")

We can then scroll down to line 37, and change the `hidden_layer_sizes` argument from `(100,)` to `(100,100)` to make
our model contain two hidden layers of 100 neurons each.

![Neural Network Settings](../../images/tutorials/ml_train_neural_network_with_2_hidden_layers.png "Neural Network Settings")

Then, close the dialogue. The workflow has now been configured, and we are ready to train.

## 7. Submit the Job

Click the check-mark in the upper right of the job designer, in the [Header Menu](../../jobs-designer/header-menu.md) to
save the job. We now return to the [job explorer](../../jobs/ui/explorer.md) page with the job in a pre-submission
status.

![PreSubmission](../../images/tutorials/jobs_tab_with_ml_train_job_set_up.png "Files Explorer Tab")

We can now [run the job](../../jobs/actions/run.md) and wait for it to complete.

## 8. Analyze the Training Results

After a few minutes, the job will complete. We can then visit the job's [results tab](../../jobs/ui/results-tab.md),
where we will see that two properties have been calculated. The first, `Machine Learning - Model Train and Predict` is
the predict workflow that was generated by the machine learning job. The predict workflow can be used to leverage the
trained model for additional predictions on new data.

The second result visible is `Machine Learning - Parity Plot`, which contains the predicted versus actual values for the
adsorption energies we trained the model on.

![Results Tab](../../images/tutorials/ml_train_results_tab.png "Results Tab")

## Animation

This tutorial is demonstrated in the following animation:

<div class="video-wrapper">
<iframe class="gifffer" width="100%" height="100%" src="https://www.youtube.com/embed/Eiw6bYn_w74" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>
