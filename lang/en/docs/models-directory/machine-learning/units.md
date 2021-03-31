# Machine Learning Units

Multiple additional **unit types** exist in the context of [Workflows](../../workflows/overview.md) based upon
the [Machine Learning Model](overview.md), besides those of [general applicability](../../workflows/components/units.md)
.

The below table describes the types of Machine Learning-specific units are available.

| Category             | Definition                                                                           | Example                                            |
| -------------------- | ------------------------------------------------------------------------------------ | -------------------------------------------------- |
| Pre-Processing       | Transformations performed on the data prior to training                              | Data Standardization                               |
| Feature Extraction   | Creates new featues from existing data                                               | Principle-Component Analysis                       |
| Feature Selection    | Automatically selects features as descriptors                                        | Random Forest Importance Score                     |
| Hyperparameter tuning| Automatically optimizes the model architecture                                       | Model Generation via Genetic Algorithm             |
| Model Training       | Adjusting model parameters and coefficients to minimize a training set loss          | Training a neural network                          |
| Model Prediction     | Using a trained model, predict what a new datapoint's values will be                 | Predicting a band gap with a trained neural network|
| Post-Processing      | Any action taken after a model is trained, we lump into the post-processing category | Showing a learning curve of the neural network     |

## Pre-Processing

The DataFrame [input/output type of units](../../workflows/components/units.md#i/o) are used to define the **training
data**, to select [target properties](../../properties/classification/machine-learning.md) that need to be predicted as
output of the Machine Learning computation,
and [feature properties](../../properties/classification/machine-learning.md) used as input. The data is returned in the
Pandas DataFrame format [^1].

[Processing units](../../workflows/components/units.md#processing) are used for general **data manipulation**, for
example cleaning missing data or remove duplicates in the data. Other examples might include the **scaling and
reducing** of the input data. Scaling is a method used to standardize the range of independent variables or features of
data, through for instance the normalization of the data.

## Feature Extraction

Feature extraction is the process of generating new features from an existing set of features. For
example, Auto-Encoders [^2] are commonly-used in dimensionality-reduction,
taking an input vector and encoding into a vector with fewer dimensions.

## Feature Selection

Feature selection units involve selecting the number
of [feature properties](../../properties/classification/machine-learning.md) for model training.

## Hyperparameter Tuning

Oftentimes, models will have hyperparameters which must be tuned prior to their use. For example, to
develop LASSO Regression [^3], an extra penalty term is added to the loss
function. This penalty term is equal to a coefficient (Lambda) multiplied by the sum of the absolue values of the model
coefficients. This extra penalty term helps prevent overfitting, and results in LASSO reducing some coefficients to 0 at
higher values of lambda. By choosing lambda, one can control how many coefficients are extinguished. Becuse lambda is
chosen before the model is trained, it is known as a hyperparameter to the model.

## Model Training

Training a model refers to optimizing a model's parameters such that some loss function is minimized. For example, when
a Convolutional Neural Network [^4] is trained for image
classification, the weights and biases of the network are adjusted to improve the model's performance against the
training set.

## Model Prediction

Prediction refers to taking a set of data for-which the targets are unknown, and using a model to decide what value the
targets are likely to have. For example, a classifier might be used to predict whether a picture contains a dog or cat.
A regressor might be used to predict a material's catalytic activity, given descriptors such as the band-gap or chemical
potential.

## Post-Processing

Post-processing refers to the actions taken after a model is trained, oftentimes aimed at simplifying a model for
performance reasons. For example, this can
include pruning [^5] a neural network to reduce the
number of mathematical optimizations that need to be performed,
or knowledge distillation [^6], where a simpler model is trained
using the outputs of a more complex model.

In addition, on the platform we use "post-processing" to refer to any action which is taken after a model is trained,
such as the visual display of data (such as training metrics or a parity plot).

## Links

[^1]: [Pandas DataFrame, Official Documentation Website](https://pandas.pydata.org/pandas-docs/stable/dsintro.html#dataframe)

[^2]: [Auto-Encoders, Wikipedia](https://en.wikipedia.org/wiki/Autoencoder)

[^3]: [LASSO Regression, Wikipedia](https://en.wikipedia.org/wiki/Lasso_(statistics))

[^4]: [Convolutional Neural Network, Wikipedia](https://en.wikipedia.org/wiki/Convolutional_neural_network)

[^5]: [Pruning, Wikipedia](https://en.wikipedia.org/wiki/Pruning_(artificial_neural_network))

[^6]: [Knowledge Distillation, Wikipedia](https://en.wikipedia.org/wiki/Knowledge_distillation)
