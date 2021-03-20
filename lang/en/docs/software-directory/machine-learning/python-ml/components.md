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

## Flavors

The following flavors are available within the current ML implementation:

- `pyml:setup_variables_packages`: contains functions and configuration essential for all Python-ML worfklows
- `pyml:data_input:read_csv:pandas`: for reading in CSV data
  using [Pandas](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html)
- `pyml:pre_processing:standardization:sklearn`: [scales the data](https://en.wikipedia.org/wiki/Feature_scaling#Standardization_(Z-score_Normalization))
  such that it has a mean of 0 and a standar deviation of 1, as implemented
  in [Scikit-Learn](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html)
- `pyml:model:multilayer_perceptron:sklearn`:
  a [multilayer-perceptron](https://en.wikipedia.org/wiki/Multilayer_perceptron) implemented
  in [Scikit-Learn](https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPRegressor.html)
- `pyml:post_processing_parity_plot_matplotlib`: generates a [parity plot](https://en.wikipedia.org/wiki/Parity_plot)
  using [Matpotlib](https://matplotlib.org/)
- `pyml:custom`: contains the basic skeleton needed for ML workflow units

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

## Workflow Structure

PythonML workflows contain two subworkflows. The first, called "Set Up the Job" performs actions such as copying data
and setting environment variables necessary for the job to run. The second, called "Machine Learning," contains the
actual machine learning units.

### Subworkflow: Set Up the Job

This subworkflow facilitates setting up the PythonML job. Currently, the only thing users need to edit in this
subworfklow are the names of the data files to be copied in for training or prediction purposes. Reconfiguring this
subworfklow to set up for a predict job is handled automatically
when [ the predict workflow is generated](../../../properties-directory/non-scalar/workflow.md).

### Subworkflow: Machine Learning

This subworkflow is where a user's requested machine learning units reside. This subworkflow is generally the one that
users are expected to modify, to add or remove different machine learning workflow units.
