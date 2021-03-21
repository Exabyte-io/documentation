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

Take note of the name of the file. For the purposes of this tutorial, it should be named `data_to_train_with.csv`

## 3. Copy the "Python ML Train" Workflow from the Workflow Bank

Next, we select the`Bank Worfklows` button in the [left sidebar](../../ui/left-sidebar.md), which brings us to
the [Bank Workflows Page](../../workflows/bank.md). We then search for the "Python ML Train" workflow owned by the "
Curators" account, and [copy it to our account](../../workflows/actions/copy-bank.md).

## 4. Create the ML Job

Next, we can create a new job by selecting the `Create Job` button in the [left sidebar](../../ui/left-sidebar.md). This
will bring us to a new job on the [Job Designer](../../jobs-designer/overview.md) page.

First, we will give the job a friendly name, such as "Python ML Tutorial" (see below). Then, we will click
the [Actions Button](../../jobs-designer/header-menu.md#Actions) (the three vertical dots in the upper-right of the job
designer), and choose "Select Workflow."

![Job Designer with Circles](../../images/tutorials/job_designer_with_python_ml_name_and_three_dots_circled.png "Job designer page")

This will bring up the [Select Workflow](../../jobs-designer/actions-header-menu/select-workflow.md) dialogue. We then
search for "Python ML Train" and click on it to bring it into our account.

## 5. Configure the ML Workflow

We now have our ML workflow selected. Select the [Workflows Tab](../../jobs-designer/workflow-tab.md), and we can see
our training workflow.

We can see two [subworkflows](../../workflows/components/subworkflows.md) available: `Set Up the Job`
and `Machine Learning`.

### Specify the Training Data

We will first configure the `Set Up the Job` workflow to accept our training data.

Begin by selecting the "Declare Training Data" workflow unit, circled below:

![ML Workflow Tab](../../images/tutorials/workflows_tab_with_ml_workflow_and_declare_training_data_circled.png "Workflow Tab")

We can now see the "Declare Training Data" IO unit. Because we named our file in dropbox `data_to_train_with.csv`
earlier, we do not need to modify this unit. In a scenario where we wanted to use a different file name for our training
data, the [Workflow Designer](../../workflow-designer/overview.md) could be used to modify the value.

![Training Data IO Unit](../../images/tutorials/training_data_io_unit.png "Training Data IO Unit")

!!!warning "A Word of Caution"
> The _only_ modifications that should be made in the `Set Up the Job` subworkflow are the filenames in the "Declare
> Training Data" and "Declare Predict Data" IO units. The `Set Up the Job` subworkflow is automatically re-configured
> during the training process. Modifying other values, or adding/removing workflow units to this subworkflow, can disrupt
> creation of the Predict workflow.

We will then close the Declare Training Data IO unit by clicking on the "X" in the dialogue's upper right corner. This
will bring us back to the [Workflows Tab](../../jobs-designer/workflow-tab.md "Workflows Tab").

### Configure Settings.py

We can now configure our settings file. Begin by selecting the `Machine Learning` subworkflow. This will make visible
all of the machine learning units that are inside the workflow:

![ML Train](../../images/tutorials/workflows_tab_with_ml_train_subworkflow_circled.png "ML Train Subworkflow")

This workflow has the following steps:

0. `Setup Packages and Variables` - Configures the job and downloads all required packages with `pip`
1. `Data Input` - Reads the training data from disk
2. `Data Standardize` - Scales the data such that it has mean 0 and standard deviation 1
3. `Model Train and Predict` - Handles model training, and prediction
4. `Parity Plot` - Draws a plot of model predictions versus training data, and saves it to the disk. This plot is shown
   on the Results tab.

We will configure the `settings.py` file by selecting the `Setup Packages and Variables` unit (see above figure). This
will open a dialogue containing the content of `settings.py`. Scroll down to line 41 of the file, and note the presence
of a variable named `target_column_name`, with the value of `"target"`. This value should instead be the target column
of our training data, so change it to `"PBE_BE_eV"` as below:

![SettingsPy](../../images/tutorials/settings_py_with_target_colname_circled.png "Settings with Colname Selected")

Then, close the dialogue. We can now demonstrate how a workflow unit's parameters can be changed. For this tutorial, we
will set our neural network to have 2 hidden layers of 100 layers each, and we will train for 5000 iterations.

Begin by selecting the `ML Train and Predict` workflow unit, as below:

![ML Train and Predict](../../images/tutorials/workflows_tab_with_ml_train_subworkflow_and_train_unit_circled.png "Workflow tab with ml train unit circled")

We can then scroll down to line 36, and change the `hidden_layer_sizes` argument from `(100,)` to `(100,100)` to add an
extra hidden layer of 100 neurons each to the model. We can then find line 40, and adjust the `max_iter` argument
from `500`
to `5000`, to give the network enough time to train. These changes are circled below.

![Neural Network Settings](../../images/tutorials/ml_train_neural_network_with_2_hidden_layers.png "Neural Network Settings")

Then, close the dialogue. The workflow has now been configured, and we are ready to train.

## 6. Submit the Job

Click the check-mark in the upper right of the job designer, in the [Header Menu](../../jobs-designer/header-menu.md) to
save the job. We now return to the [job explorer](../../jobs/ui/explorer.md) page with the job in a pre-submission
status.

![PreSubmission](../../images/tutorials/jobs_tab_with_ml_train_job_set_up.png "Files Explorer Tab")

We can now [run the job](../../jobs/actions/run.md) and wait for it to complete.

## 7. Analyze the Training Results

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
<iframe class="gifffer" width="100%" height="100%" src="https://www.youtube.com/watch?v=Eiw6bYn_w74" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>
