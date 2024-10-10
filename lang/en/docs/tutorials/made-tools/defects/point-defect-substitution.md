# Create materials with substitution defects from the paper 

This tutorial demonstrates the process of creating materials with substitution defects, based on the research presented in:
<h3>Formation, stabilities, and electronic properties of nitrogen defects in graphene </h3>
Yoshitaka Fujimoto and Susumu Saito

Physical Review B, 2011. 

The paper is available [here](https://journals.aps.org/prb/abstract/10.1103/PhysRevB.84.245446).

## Pre-requisites

This tutorial assumes that the user knows how to:

- Open [Materials Designer](../../../materials-designer/overview.md).
- Launch [JupyterLite Session](../../../jupyterlite/overview.md) (inside Materials Designer) or Jupyter Notebook (on the local machine).
- Import materials into Materials Designer (from Standata, Materials Bank or as upload).
- Pass data between JupyterLite Session or Jupyter Notebook and outside runtime.

## Procedure overview

- Import Graphene material into Materials Designer and load in JupyterLite Session.
- Configure defect settings (for single -- use existing notebook, for multiple -- edit the notebook).
- Run the notebook to create the material with defects.
- Analyze and save the results.

## Option A: Single substitution defect

To replicate the material from FIG. 1. a) of the paper: 

<img src="/images/tutorials/made-tools/defects/point_defect_substitution/point_defect_substitution_0.webp" title="FIG. 1. a)">

Use the existing `create_point_defect.ipynb` notebook and modify the parameters.

For the desired material we will use approximate coordinates to place the substituting atom since it's easier to do that based on the picture from the paper.
The notebook will use that `APPROXIMATE_COORDINATE` parameter to create corresponding configuration and ignore other methods. 

Add the following code to the "1.1. Set up defect parameters" cell:

```python
DEFECT_TYPE = "substitution"
SITE_ID = None # `from_site_id` method will be ignored
COORDINATE = None # default method will be ignored
APPROXIMATE_COORDINATE = [0.51, 0.5, 0.5]    
CHEMICAL_ELEMENT = "N"
SUPERCELL_MATRIX = [[5, 0, 0], [0, 5, 0], [0, 0, 1]]
```

## Option B: Multiple substitution and vacancy defects

To reproduce the material from FIG. 1. b) of the paper we will need to add 3 substitution and 1 vacancy defects to the same material.

Create a copy of the notebook to preserve the original and edit the copy.

Under the "2.1. Set defect configuration and builder parameters" cell, add the following code:

```python
from mat3ra.made.tools.build.defect import PointDefectConfiguration
from mat3ra.made.tools.build.defect.builders import PointDefectBuilderParameters

defect_configuration_1 = PointDefectConfiguration.from_approximate_position(crystal=supercell,
                                                                              defect_type="substitution",
                                                                              approximate_coordinate=[0.51, 0.5, 0.5],
                                                                              chemical_element=CHEMICAL_ELEMENT)

defect_configuration_2 = PointDefectConfiguration.from_approximate_position(crystal=supercell,
                                                                              defect_type="substitution",
                                                                              approximate_coordinate=[0.5, 0.75, 0.5],
                                                                              chemical_element=CHEMICAL_ELEMENT)

defect_configuration_3 = PointDefectConfiguration.from_approximate_position(crystal=supercell,
                                                                                defect_type="substitution",
                                                                                approximate_coordinate=[0.25, 0.5, 0.5],
                                                                                chemical_element=CHEMICAL_ELEMENT)

defect_configuration_4 = PointDefectConfiguration.from_approximate_position(crystal=supercell,
                                                                                defect_type="vacancy",
                                                                                approximate_coordinate=[0.5, 0.5, 0.5])

defect_builder_parameters = PointDefectBuilderParameters(center_defect=False)
```

Under the "2.2. Create the defects" cell, add the following code to create add multiple defects consecutively:

```python
from mat3ra.made.tools.build.defect import create_defect

defect_1 = create_defect(defect_configuration_1, defect_builder_parameters)
defect_configuration_2.crystal = defect_1  # Update crystal for the next defect
defect_2 = create_defect(defect_configuration_2, defect_builder_parameters)
defect_configuration_3.crystal = defect_2  # Update crystal for the next defect
defect_3 = create_defect(defect_configuration_3, defect_builder_parameters)
defect_configuration_4.crystal = defect_3  # Update crystal for the next defect
defect_4 = create_defect(defect_configuration_4, defect_builder_parameters)
```

## Execution and Analysis

### 1. Run the Notebook

Run the notebook by clicking `Run` > `Run All` in the top menu to run cells and wait for the results to appear.

## 2. Analyze the Results

After running the notebook, the user will be able to visualize the structure of Graphene with substitution defects.

For the single substitution defect, the user will see the following structure:
<img src="/images/tutorials/made-tools/defects/point_defect_substitution/point_defect_substitution_1.webp" title="Graphene with substitution defects">

For the multiple substitution and vacancy defects, the user will see the following structure:
<img src="/images/tutorials/made-tools/defects/point_defect_substitution/point_defect_substitution_2.webp" title="Graphene with multiple substitution and vacancy defects">
## 3. Save the Material

The user can pass the material with substitution defects in the current Materials Designer environment and save it.

Or the user can download the material in Material JSON format or POSCAR format.

## Interactive JupyterLite Notebook

{% with notebook_name='create_point_defect.ipynb' %}
{% include 'includes/jupyterlite_embed.html' %}
{% endwith %}