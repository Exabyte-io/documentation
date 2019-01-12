# Machine Learning Units

Multiple additional **unit types** exist in the context of [Workflows](../../workflows/overview.md) based upon the [Machine Learning Model](overview.md), besides those of [general applicability](../../workflows/components/units.md).

## Unit types

The following types of Machine Learning-specific units are available.

### Input/Output

The [input/output type of units](../../workflows/components/units.md#i/o) are used to define the **training data**, to select [target properties](../../properties/classification/machine-learning.md) that need to be predicted as output of the Machine Learning computation, and to select [feature properties](../../properties/classification/machine-learning.md) used as input.

### Processing

[Processing units](../../workflows/components/units.md#processing) are used for general **data manipulation**, for example cleaning missing data or remove duplicates in the data.
 
### Data Transformation

Data transformation might for example involve the **scaling and reducing** of the input data. Scaling is a method used to standardize the range of independent variables or features of data, through for instance the normalization of the data.
 
### Feature Selection

Feature selection units involve selecting the number of [feature properties](../../properties/classification/machine-learning.md) for model training. If equal to 0, will use all available features. The feature selection algorithm can also be chosen (e.g. by regression).
