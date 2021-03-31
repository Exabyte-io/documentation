# Machine Learning Parameters

We present in what follows the [parameters](../../models/parameters.md) which apply specifically to the Machine
Learning **model type**.

## Subtype

We support the following **Subtypes**:

- **Regression** [^1] (default): predict a [property](../../properties/overview.md) (e.g. Band gap) of the target
  material given a relationship between material features (**descriptors**) of similar materials (**training set**), and
  same property of the materials in the training set.
- **Classification** [^2]: predict which category (e.g. superconductor, etc) a target material belongs to based on
  the **descriptors** of similar materials in the **training set**.
- **Clustering** [^3]: given a set of **descriptors**, partition the data into several sets, such that materials within
  one set are more similar to one-another than they are to materials in another set.

## Links

[^1]: [Wikipedia Regression analysis, Website](https://en.wikipedia.org/wiki/Regression_analysis)

[^2]: [Wikipedia Statistical classification, Website](https://en.wikipedia.org/wiki/Statistical_classification)

[^3]: [Wikipedia Cluster analysis, Website](https://en.wikipedia.org/wiki/Cluster_analysis)
