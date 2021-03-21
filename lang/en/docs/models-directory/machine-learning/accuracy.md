# Accuracy

## Importance of Accurate Training Data

When training a machine learning model, care must be taken to ensure that the dataset being used is a quality one.
Indeed, the concept of "garbage-in, garbage-out" is highly applicable to models trained on poor a low-quality dataset -
a model is only as good as the data it was trained on.

Consider a hypothetical machine learning model which is able to achieve perfect accuracy on any dataset it's given,
without overfitting. Now consider what would happen if such a model were trained on two different datasets of vastly
different quality - for example, electronic energies calculated using the Local Density Approximation [^1] versus
electronic energies calculated with a Coupled Cluster [^2] technique. Despite performing perfectly, the model would only
ever be as accurate as the underlying data used to train it.

## Common Accuracy Metrics

Assessing model performance is a topic which has received significant attention, and there is as a result no shortage of
methods by-which a model's performance can be evaluated. We present a few more-common metrics below.

### Regression

- The **Root Mean Squared Error** is the square root of the average of the squared difference between the training data
  and the model's predictions.
- The **Mean Absolute Error** is the average of the absolute difference between the training data and the model's
  predictions.

### Classification

- The **Confusion Matrix** can be used to derive a plethora of error metrics [^3], including the **true positive rate**,
  the **false positive rate**, **precision**, **recall**, and many others.

## Links

[^1]: [Local-Density Approximation, Wikipedia](https://en.wikipedia.org/wiki/Local-density_approximation)

[^2]: [Coupled-Cluster, Wikipedia](https://en.wikipedia.org/wiki/Coupled_cluster)

[^3]: [Confusion Matrix, Wikipedia](https://en.wikipedia.org/wiki/Confusion_matrix)
