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

![Workflow Diagram](../../../images/software-directory/machine-learning/python-ml/ML_Train_Diagram.png)

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

### Setup Flavors

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

### Data Input Flavors

pyml:data_input:**read_csv**:pandas

---

### Pre-Processing Flavors

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

### Model Flavors

pyml:model:**multilayer_perceptron**:skearn

---

### Post-Processing Flavors

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


## Custom Machine Learning Units

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
