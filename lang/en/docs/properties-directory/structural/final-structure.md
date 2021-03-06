# Final Structure

The final structure represents the [crystal structure](../../materials/classification/crystalline.md) of a [material](../../materials/overview.md) which is generated during the execution of a [modeling unit](../../workflows/components/units.md/#execution). The final structure(s) is extracted and stored inside user's materials collection if it is different from the initial structure, the structure from which the execution unit starts. The final structure is stored inside a new [set](../../entities-general/sets.md) with `$MATERIAL_NAME - final - $JOB_NAME` as name and `$JOB_ID` as the tag at the same level as the initial structure. The final structure(s) is ordered if the initial one(s) is ordered.

## Relevance for Structural Relaxations

The visualization of the final structure is especially resourceful in the context of simulation runs that include a preliminary [structural relaxation](../../workflows/addons/structural-relaxation.md) step. In this case, it becomes important to understand how the material [originally defined](../../jobs-designer/materials-tab.md) during [Job creation](../../jobs-designer/overview.md) was structurally altered by the relaxation algorithms.

## Example

The final structure can be inspected under an instance of the [Materials Viewer interface](../../materials/ui/viewer.md) within the [Results Tab](../../jobs/ui/results-tab.md) of the corresponding [Job Viewer](../../jobs/ui/viewer.md). 

We refer to this interface as the "Final Structure Viewer" in this particular context.

Below we show an example of a material structure as it appears under the Final Structure Viewer (demarcated in red), following a relaxation run performed on it using [VASP](../../software-directory/modeling/vasp/overview.md). 

The viewer is shown in the general context of the other relevant computed material [properties](../overview.md), displayed together in their own panel.

![Final Structure Viewer](../../images/properties-directory/final-structure-viewer.png "Final Structure Viewer")
