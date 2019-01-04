# Machine Learning Parameters
 
We present in what follows the [parameters](../../models/parameters.md) which apply specifically to the Machine Learning **model type**.

## Subtype

We support the following **Subtypes**:

- **Regression** [^1] (default): predict a [property](../../properties/overview.md) (e.g. Band gap) of the target material given a relationship between material features (**descriptors**) of similar materials (**training set**), and same property of the materials in the training set. 

## Training Data Categorization

### Supervised

Some data is already available, for example the band gaps of Si-Ge alloys. This available data can thus be used to train a machine learning model, affording for the prediction of the band gap of a new material.

### Unsupervised

Some Data is available, however no information is present about the nature of this data. In this case, we identify a subset of descriptors and/or characteristics to bin materials within the training data based on their similarity.

## Links

[^1]: [Wikipedia Regression analysis, Website](https://en.wikipedia.org/wiki/Regression_analysis)
