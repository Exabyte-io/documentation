# Machine Learning: Predict New Properties

In the present tutorial page, we will explore how the results of the [Train Model](train-ml-model.md) derived from [Machine Learning (ML)](../../models-directory/machine-learning/overview.md) can be used to predict new material [properties](../../properties/overview.md) by [linear regression](../../methods-directory/linear-regression/overview.md), such as implemented by the [Exabyte Machine Learning Engine](../../software-directory/machine-learning/exabyte/overview.md).

In the present example, we consider the [Electronic Band Gap](../../properties-directory/non-scalar/band-gaps.md) calculated in the [previous tutorial](train-ml-model.md) for the case of Si/Ge-based materials, however the general approach exposed herein can work for many different properties.

## Steps

We follow the below steps, by making use of our [Web Interface](../../ui/overview.md).

1. Extract ML train model as workflow
2. Predict property using the model

## 2. Predict Property Using the Model

The properties which will be predicted are the **target properties** which have been ticked and selected under the [unit editor interface](../../workflow-designer/unit-editor.md) of the "input" [unit](../../workflows/components/units.md) of the "ml_predict" workflow, under the "Targets" section of the interface.

After [creating and executing a new Job](../../jobs-designer/overview.md), with "ml_predict" as the main [Workflow](../../jobs-designer/workflow-tab.md), it can be applied to a new set of [materials](../../jobs-designer/materials-tab.md) similar to the ones used originally to train the model. The newly predicted properties can finally be inspected under the [results tab](../../jobs/ui/results-tab.md) of [job viewer](../../jobs/ui/viewer.md).

## Animation

In the following animation, we demonstrate how the above steps can be followed to predict the band-gap of a new set of Si/Ge-based materials, using the model trained in a [previous tutorial](train-ml-model.md). For the sake of this example, we predict the bang-gap for the Si4Ge12 stochiometric composition. The results of the ML prediction for both the direct and indirect band gaps (0.525 and 0.490
 eV respectively) are in very good agreement with the values of their direct computation using [DFT](../../models-directory/dft/overview.md) (0.517 and 0.441 eV respectively).

<div class="video-wrapper">
<iframe class="gifffer" width="100%" height="100%" src="https://www.youtube.com/embed/fHAEToVJog0" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>
