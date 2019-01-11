# Machine Learning Units

Multiple additional **unit types** exist in the context of [Workflows](../../workflows/overview.md) based upon the [Machine Learning Model](overview.md), besides those of [general applicability](../../workflows/components/units.md).

## Unit types

The following types of Machine Learning-specific units are available.

### Input/Output

The input/output type of units are used to define the training data, to select [target properties](../../properties/classification/machine-learning.md) that need to be predicted as output of the Machine Learning computation, and to select [feature properties](../../properties/classification/machine-learning.md) used as input.

### Processing

Processing units are used for general data manipulation, for example cleaning missing data or remove duplicates in the data.
 
### Data Transformation

Data transformation might for example involve the scaling and reducing of the input data. Scaling is a method used to standardize the range of independent variables or features of data, through for instance the normalization of the data.
 
### Feature Selection

Feature selection units involve selecting the number of [feature properties](../../properties/classification/machine-learning.md) for model training. If equal to 0, will use all available features. The feature selection algorithm can also be chosen (e.g. by regression).

## Machine Learning Workflow

Overall, a complete Machine Learning [workflow](../../workflows/overview.md) consists of the following multiple steps, operated in a sequential order through the implementation of the above-mentioned units.

1. Generating and gathering the training data set
2. Manipulating and Processing the data 
3. Transforming the data through scaling, etc.
4. Selecting the best features, through for example regression
5. Building the Machine Learning train model
6. Predicting new properties from the trained model

The user is referred to the [tutorial section](../../tutorials/ml/overview.md) on machine learning for more detailed information on the above steps.
