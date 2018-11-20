# Final Structure

The final structure represents the [crystal structure](../../materials/data.md) of a [material](../../materials/overview.md) which is generated as part of the output of a simulation [Job](../../jobs/overview.md).

## Example

The final structure can be inspected under an instance of the [Materials Viewer interface](../../materials/ui/viewer.md) within the [Results Tab](../../jobs/ui/results-tab.md) of the corresponding [Job Viewer](../../jobs/ui/viewer.md). 

We refer to this interface as the "Final Structure Viewer" in this particular context.

## Relevance for Structural Relaxations

This visualization is especially resourceful in the context of simulation runs that include a preliminary [structural relaxation](../../workflows/addons/structural-relaxation.md) step. In this case, it becomes important to understand how the material [originally defined](../../jobs-designer/materials-tab.md) during [Job creation](../../jobs-designer/overview.md) was structurally altered by the relaxation algorithms.

## Appearance in Jobs Viewer

Below we show an example of a material structure as it appears under the Final Structure Viewer (demarcated in red), following a relaxation run performed on it using [VASP](../../software/modeling/vasp.md). 

The viewer is shown in the general context of the other relevant computed material [properties](../overview.md), displayed together in their own panel under the aforementioned [Results Tab](../../jobs/ui/results-tab.md) of [Job Viewer](../../jobs/ui/viewer.md).

![Final Structure Viewer](/images/Properties/final-structure-viewer.png "Final Structure Viewer")
