# Components

We present in this page the different [components](../../../software/components.md) (executables and flavors)
comprised within our [Python-based](overview.md) machine learning implementation.

Only those components implemented on our platform to date are mentioned here, as can be inspected from the lists of
available executables and flavors under the
[Unit Editor Interface](../../../workflow-designer/unit-editor.md#application).

!!!warning "Implementation on our platform"
    The user who wishes for additional functionality to be added to our platform in future should express so via
    a [support request](../../../ui/support.md).

## Executable

PythonML is based on the `python` [executable](../../../software/components.md#executables), and through this executable
the implemented ML calculations can be performed.

## Workflow Structure

PythonML workflows contain two subworkflows. The first, called "Set Up the Job" performs actions such as copying data
and setting environment variables necessary for the job to run. The second, called "Machine Learning," contains the
actual machine learning units. A diagram can be found below, based on the bank workflow located
[here](https://platform.exabyte.io/analytics/workflows/rg3HcXd9Rg7hTa5Q3).

![Machine Learning Subworkflow Diagram with Automated Calculation Setup and Pipeline](../../../images/software-directory/machine-learning/python-ml/ml-train-diagram.png "Machine Learning Subworkflow Diagram with Automated Calculation Setup and Pipeline")

### Subworkflow: Set Up the Job

This subworkflow facilitates setting up the PythonML job. Users should not need to edit this workflow. The configuration
of this workflow is handled automatically on the
when [the predict workflow is generated](../../../properties-directory/non-scalar/workflow.md).

### Subworkflow: Machine Learning

This subworkflow is where a user's requested machine learning units reside. This subworkflow is generally the one that
users are expected to modify, to add or remove different machine learning workflow units. In the above diagram, we find
the following units:

| Unit Name                     | Flavor                                       | Description |
|-------------------------------|----------------------------------------------|-------------|
| `Setup Packages and Variables`| `pyml:setup_variables_packages`              |Contains functions and configuration essential for all python-ML Workflows|
| ` Data Input`                 | `pyml:data_input:read_csv:pandas`            |for reading in CSV data using Pandas [^1]|
| `Data Standardize`            | `pyml:pre_processing:standardization:sklearn`|scales the data [^2] such that it has a mean of 0 and a standard deviation of 1, as implemented in Scikit-Learn [^3]|
| `Model Train and Predict`     | `pyml:model:multilayer_perceptron:sklearn`   |a Multilayer Perceptron [^4] implemented in Scikit-Learn [^5]|
| `Parity Plot`                 | `pyml:post_processing:parity_plot:matplotlib`|generates a parity plot [^6] using Matplotlib [^7]|

## Flavors

A variety of flavors are available for use in machine learning. Generally, flavors behave different based on whether a
workflow is being run to train or whether the workflow is being run to predict.
---

### Setup

Setup flavors facilitate the initialization and setup of ML jobs.

pyml:**setup_variables_packages**

- General settings for PythonML jobs on the platform. This file generally shouldn't be modified directly by users. The "
  datafile" and "is_workflow_running_to_predict" variables are defined in the Important Settings portion of the Jobs
  Designer, and templated into this file. This facilitates the workflow's diverging behavior based on whether it is in
  a "
  train" or "predict" mode.

- Also in this file is the "Context" object, which helps certain python objects persist between workflow units, and
  between training / predict runs.

- Whenever a python object needs to be stored for subsequent runs (such as in the case of a trained model)
  , `context.save()` can be called to save it. The object can then be loaded again by using `context.load`

---

### Data Input

Data input flavors generally perform I/O or other initial operations on the dataset.

pyml:data_input:**read_csv**:pandas

- This workflow unit reads in data for the ML workflow. If the workflow is in training mode, it will ead in the data
  before converting it to a numpy array, and save it for use later.
- This unit will create variables for the "target" and "descriptors" used by the training set.

pyml:data_input:**train_test_split**:sklearn

- Splits the dataset into a training and testing set. The variable `percent_held_as_test` in the important settings
  controls how much of the input dataset is held back as a testing set. By default, this unit will place 20% of the
  dataset into the testing set, and 80% into the training set.
- This unit will do nothing in the case of predictions.

---

### Pre-Processing

In our machine learning platform, "Pre-Processing" is a catch-all term for anything that happens before a model is
trained but after the data has been loaded.

pyml:pre_processing:**min_max_scaler**:sklearn

- This workflow unit scales the data such that it is on interval `[0,1]`. It then saves the data for use further down
  the road in the workflow, such as un-transforming the data.
- It is important that new predictions are made by scaling the new inputs using the min and max of the original training
  set. As a result, the scaler gets saved in the training phase.
- During a predict workflow, the scaler is loaded, and the new examples are scaled using the stored scaler.

pyml:pre_processing:**remove_missing**:pandas

- This workflow unit allows missing rows and/or columns to be dropped from the dataset by configuring the `to_drop`
  parameter.
- Valid values for `to_drop` are:
    - `rows`: Rows with missing values will be removed
    - `columns`: Columns with missing values will be removed
    - `both`: Rows and columns with missing values will be removed

pyml:pre_processing:**remove_duplicates**:pandas

- This workflow unit will drop all duplicate rows, if it is running in the "train" mode.

pyml:pre_processing:**standardization**:sklearn

- This workflow unit scales the data such that it has a mean of 0 and a standard deviation of 1. It then saves the data
  for use further down the road in the workflow, for use in un-transforming the data.
- It is important that new predictions are made by scaling the new inputs using the mean and variance of the original
  training set. As a result, the scaler gets saved in the training phase.
- During a predict workflow, the scaler is loaded, and the new examples are now scaled using the stored scaler.

---

### Modeling

When a workflow is run in the training mode, the model is trained and then it is saved, along with a metric to describe
the model's performance (such as RMSE). The model also makes predictions to facilitate generation of a plot of
performance (such as a parity plot or ROC curve).

When a workflow is run in the predict mode, the model is loaded and used to make predictions. These predictions are then
written to a file named "predictions.csv"

#### **Classification**

pyml:model:**random_forest_classification**:sklearn

- Workflow unit to train a random forest classification model with Scikit-Learn. Model parameters are derived from
  Scikit-Learn's defaults.

#### **Regression**

pyml:model:**adaboosted_trees_regression**:sklearn

- Workflow unit for adaptive-boosted trees regression with Scikit-Learn. Parameters for the estimator and ensemble are
  derived from Scikit-Learn's defaults.

pyml:model:**bagged_trees_regression**:sklearn

- Workflow unit for a bagged trees regression model with Scikit-Learn. Parameters for the estimator and ensemble are
  derived from Scikit-Learn's defaults.

pyml:model:**gradboosted_trees_regression**:sklearn

- Workflow to train the gradient-boosted trees ensemble method with Scikit-Learn. Model parameters are derivedf rom
  Scikit-Learn's defaults.
- Note: In the gradient-boosted trees ensemble used, the weak learners used as estimators cannot be tuned with the same
  level of fidelity allowed in the Adaptive-Boosted Trees ensemble.

pyml:model:**kernel_ridge_regression**:sklearn

- Workflow unit for a kernelized ridge regression model with Scikit-Learn. Model parameters are derived from
  Scikit-Learn's defaults.

pyml:model:**lasso_regression**:sklearn

- Workflow unit for a LASSO-based regression model with Scikit-Learn. Model parameters are derived from Scikit-Learn's
  defaults. The alpha parameter has been lowered from a value of 1.0 to 0.1.

pyml:model:**multilayer_perceptron**:sklearn

- Workflow unit to train a simple feedforward neural network model on a regression problem using Scikit-Learn. Model
  parameters are derived from Scikit-Learn's defaults.

pyml:model:**ridge_regression**:sklearn

- Workflow unit for a ridge regression model with Scikit-Learn. Alpha is taken from Scikit-Learn's default parameters.

pyml:model:**random_forest_regression**:sklearn

- This workflow unit trains a random forest regression model with Scikit-Learn. Model parameters are derived from
  Scikit-Learn's defaults.

#### **Unsupervised Learning**

pyml:model:**k_means_clustering**:sklearn

- Workflow unit to train a k-means clustering model with Scikit-Learn. Model parameters are derived from Scikit-Learn's
  defaults.

---

### Post-Processing

In our machine learning platform, "Post-Processing" is a catch-all term for anything that happens after a model is
trained. Currently, we offer three different ways to plot training data in this section, one type of plot each for
regression, classification, or unsupervised-learning problems.

pyml:post_processing:**pca_2d_clusters**:matplotlib

- This unit takes an N-dimensional feature space, and uses Principle Component Analysis (PCA) to project it onto a 2D
  space to facilitate plotting on a 2D scatter plot.
- The 2D space we project onto is the first two principle components identified in PCA, which are the two vectors with
  the highest variance.
- We then pot the labels assigned to the train and test set, and color by class.
- This unit only runs during a training job. It does nothing if the workflow is being run in predict mode.

pyml:post_processing:**parity_plot**:matplotlib

- This unit generates a parity plot based on the known values in the training data, and the predicted values generated
  using the training (or test) data.
- This unit only runs during a training job. It does nothing if the workflow is being run in predict mode.

pyml:post_processing:**roc_curve**:sklearn

- Computes and displays the Receiver Operating Characteristic (ROC) curve. This is restricted to binary classification
  tasks.
- This unit only runs during a training job. It does nothing if the workflow is being run in predict mode.

---

### Custom Machine Learning Units

Custom machine learning units are created by selecting the pyml:**custom** flavor.

Custom machine learning units take advantage of our implementation's ability to mark Python objects as needed for
subsequent predict runs. This can be accomplished by calling the `save` and `load` methods of `settings.context`.

Additionally, by taking advantage of `settings.is_workflow_running_to_train`
or `settings.is_workflow_running_to_predict`, users can mark certain sections of code to only run during training or
prediction.

Overall, this allows workflow units to have a divergent behavior based on whether the workflow is in "train" or "
predict" mode. For example, a unit can be configured to train (and then save) a model during a training job, and then to
load the same model and perform a prediction during a predict job.

```python3
import settings

# The context manager exists to facilitate
# saving and loading objects across Python units within a workflow.

# To load an object, simply do to `context.load("name-of-the-saved-object")`
# To save an object, simply do `context.save("name-for-the-object", object_here)`
with settings.context as context:
    # Train
    if settings.is_workflow_running_to_train:
        descriptors = context.load("descriptors")
        target = context.load("target")

        # Do some transformations to the data here

        context.save(descriptors, "descriptor")
        context.save(target, "target")


    # Predict
    else:
        descriptors = context.load("descriptors")

        # Do some predictions or transformation to the data here
```

## Links

[^1]: [read_csv function, Pandas](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html)

[^2]: [Feature Scaling, Wikipedia](https://en.wikipedia.org/wiki/Feature_scaling#Standardization_(Z-score_Normalization))

[^3]: [Standard Scaler, Scikit-Learn](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html)

[^4]: [Multilayer Perceptron, Wikipedia](https://en.wikipedia.org/wiki/Multilayer_perceptron)

[^5]: [MLPRegressor class Scikit-Learn](https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPRegressor.html)

[^6]: [Parity Plot, Wikipedia](https://en.wikipedia.org/wiki/Parity_plot)

[^7]: [Matpotlib Documentation](https://matplotlib.org/)
