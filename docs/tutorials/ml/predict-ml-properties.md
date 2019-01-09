# Machine Learning: Predict New Properties

In the present tutorial page, we will explore how the results of the [Train Model](train-ml-model.md) derived from [Machine Learning (ML)](../../models-directory/machine-learning/overview.md) can be used to predict new material [properties](../../properties/overview.md) by [linear regression](../../methods-directory/linear-regression/overview.md), such as implemented by the [Exabyte Machine Learning Engine](../../software-directory/machine-learning/exabyte/overview.md).

We consider the [Electronic Band Gap](../../properties-directory/non-scalar/band-gaps.md) calculated in the [previous tutorial](train-ml-model.md) in the present example, however the general approach exposed herein can work for many different properties.

## Steps

We follow the below steps, by making use of our [Web Interface](../../ui/overview.md).

1. Extract ML train model as workflow
2. Predict property using the model

## 1. Extract ML Train Model as Workflow

Once the ML Train Model has been [built](train-ml-model.md#3.-build-ml-train-model) following the execution of the relevant [job](../../jobs/overview.md), a new [Workflow](../../workflows/overview.md) called **"ml_predict"** is generated and can be retrieved under the [results tab](../../jobs/ui/results-tab.md) of [job viewer](../../jobs/ui/viewer.md).

This "ml_predict" workflow should be opened under the [Viewer Interface](../../workflows/ui/viewer.md), and then [saved](../../workflow-designer/header-menu.md#saving-the-workflow) to the account-owned [collection](../../accounts/collections.md) of workflows. It can subsequently be used at the moment of [creation of a new Job](../../jobs-designer/overview.md), to **predict** the properties (such as the band-gap) of new materials based upon statistical considerations formed from the trained model, without consequently the need for further physics-based simulations.

## 2. Predict Property Using the Model

The properties which will be predicted are the **target properties** which have been ticked and selected under the [unit editor interface](../../workflow-designer/unit-editor.md) of the "input" [unit](../../workflows/components/units.md) of the "ml_predict" workflow, under the "Targets" section of the interface.

After [creating and executing a new Job](../../jobs-designer/overview.md), with "ml_predict" as the main [Workflow](../../jobs-designer/workflow-tab.md) applied to a new set of [materials](../../jobs-designer/materials-tab.md) similar to the ones used originally to train the model, the newly predicted properties can be inspected under the [results tab](../../jobs/ui/results-tab.md) of [job viewer](../../jobs/ui/viewer.md).

## Animation

In the following animation, we demonstrate how the above steps can be followed to predict the band-gap of a new set of Si/Ge-based materials, using the model trained in a [previous tutorial](train-ml-model.md). For the sake of this example, we predict the bang-gap for the Si16Ge16 stochiometric composition. The results of the ML prediction for both the direct and indirect band gaps (2.231 and 0.378 eV respectively) are in very good agreement with the results of their direct computation using [DFT](../../models-directory/dft/overview.md).

<div class="video-wrapper">
<iframe class="gifffer" width="100%" height="100%" src="https://www.youtube.com/embed/T3bsT3uD3VI" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>
