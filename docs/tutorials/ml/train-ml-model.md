# Machine Learning: Train Linear Regression

This tutorial demonstrates how to build a [machine learning (ML)](../../models-directory/machine-learning/overview.md) **training model** for a set of [materials](../../materials/overview.md) called **"train materials"**. This model can then be used to predict the [properties](../../properties/overview.md) of another set called **"target materials"**, based on the procedure outlined in a [separate tutorial](predict-ml-properties.md). 

We consider the [Electronic Band Gap](../../properties-directory/non-scalar/band-gaps.md) in the present example, however the general approach can work for many different properties.

For the sake of the present tutorial example, we will consider the following stochiometric combinations of the elements silicon (Si) and germanium (Ge) to train our ML model for predicting the band-gap. These structures all contain a total of 16 atoms, and can be generated through the help of [combinatorial sets](../../materials-designer/header-menu/advanced/combinatorial-set.md) via [Materials Designer](../../materials-designer/overview.md).

- Ge16
- Si2 Ge14
- Si6 Ge10
- Si8 Ge8
- Si10 Ge6
- Si12 Ge4
- Si14 Ge2
- Si16

## Steps

We follow the below steps, by making use of our [Web Interface](../../ui/overview.md).

1. Calculate band gap for the "train materials"
2. Build ML Train model based on the "train materials"

## 1. Calculate Band Gap

### Import Band-gap Workflow from Bank

The user can import a pre-assembled [workflow](../../workflows/overview.md) for calculating the band-gap of materials directly from the [Workflow Bank](../../workflows/bank.md) into the account-owned [collection](../../accounts/collections.md). We explain the procedure for doing so [in this page](../../workflows/actions/copy-bank.md).

### Create and Run Job

Once the appropriate workflow has been copied from the Bank, we can proceed with the creation of a new [Job](../../jobs/overview.md)
using the [Job Designer interface](../../jobs-designer/overview.md). We first need to [select](../../jobs-designer/actions-header-menu/select-materials.md) all the aforementioned materials containing Si and Ge from the account-owned materials [collection](../../accounts/collections.md), and thus add them to the job being created. 

Under the [Workflow Tab](../../jobs-designer/workflow-tab.md) of Job Designer, we then need to [select](../../jobs-designer/actions-header-menu/select-workflow.md) the band-gap workflow imported previously. At this point, the Job can be [executed](../../jobs/actions/run.md) for the computation of the band-gap for our set of Si/Ge-based materials. 

## 2. Build ML Train Model

The "ML Train Model" Workflow can be imported from the Bank into the account-owned collection by repeating the procedure outlined [here](../../workflows/actions/copy-bank.md).

The user should then repeat the same procedure for [creating and executing](../../jobs-designer/overview.md) a new [Job](../../jobs/overview.md) as the preceding step, selecting the "ML Train Model" Workflow this time in conjunction with the Si/Ge-containing materials for which the band gap was calculated previously. This allows the [Exabyte Machine Learning Engine](../../software-directory/machine-learning/exabyte/overview.md) to build the ML Train Model based upon the results of such band gap computations, which can then be used to [predict](predict-ml-properties.md) the band gaps of other similar materials.

The [target properties](../../properties/classification/machine-learning.md) (the band gap in this case) can be selected by opening the [unit editor](../../workflow-designer/unit-editor.md) for the "input" [unit](../../workflows/components/units.md) of the "ML Train Model" Workflow, and scrolling down to the "Targets" section within the editor interface.

## Animation

We demonstrate the [Web Interface](../../ui/overview.md)-based procedure involved in the above final step for building the ML Train Model in the animation below.   

<div class="video-wrapper">
<iframe class="gifffer" width="100%" height="100%" src="https://www.youtube.com/embed/vUhtS-pa0HA" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>
