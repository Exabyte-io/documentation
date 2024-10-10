# Create Nitrogen Defects in Graphene

This tutorial demonstrates the process of creating materials with substitution defects, based on the research presented in:
<h3>Formation, stabilities, and electronic properties of nitrogen defects in graphene </h3>
Yoshitaka Fujimoto and Susumu Saito

Physical Review B, 2011. 

The paper is available [here](https://journals.aps.org/prb/abstract/10.1103/PhysRevB.84.245446).


## Procedure overview

- Open Materials Designer and import Graphene material from [Standata](../../../materials-designer/header-menu/input-output/standata-import.md).
- Create supercell of Graphene.
- Get coordinates of the atoms to replace via 3D editor.
- Launch [JupyterLite Session](../../../jupyterlite/overview.md) and open the `create_point_defect.ipynb` notebook.
- Configure defect settings 
- Run the notebook to create the material with defects.
- Analyze the results and save the material.

## Step 1: Import Graphene Material

In this tutorial we will focus on replicating the material from FIG. 1. b) of the paper: 

<img src="/images/tutorials/made-tools/defects/point_defect_substitution/point_defect_substitution_0.webp" title="FIG. 1. a)">

Use the existing `create_point_defect.ipynb` notebook and modify the parameters.

## Step 2: Adjust the Notebook Settings

Adjust supercell matrix in the "1.1. Set up defect parameters" cell, since the supercell is already created outside the notebook:

```python
DEFECT_TYPE = "substitution"
SITE_ID = None # `from_site_id` method will be ignored
COORDINATE = None # default method will be ignored
APPROXIMATE_COORDINATE = None   
CHEMICAL_ELEMENT = "N"
SUPERCELL_MATRIX = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
```

For the desired material we will use approximate coordinates to place the substituting atom since it's easier to do that based on the picture from the paper.
The notebook will use that `APPROXIMATE_COORDINATE` parameter to create corresponding configuration and ignore other methods. 

Under the "2.1. Set defect configuration and builder parameters" cell, create configurations for multiple defects:
Use the same `crystal` material as its lattice is used to place the defects.

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
defect_configurations = [defect_configuration_1, defect_configuration_2, defect_configuration_3, defect_configuration_4]

defect_builder_parameters = PointDefectBuilderParameters(center_defect=False)
```

Under the "2.2. Create the defects" cell, add the following code to create add multiple defects consecutively:

```python
from mat3ra.made.tools.build.defect import create_defects

material_with_defects = create_defects(defect_configurations,
                                       supercell,
                                       defect_builder_parameters)
```


## 3. Run the Notebook

Run the notebook by clicking `Run` > `Run All` in the top menu to run cells and wait for the results to appear.

## 4. Analyze the Results

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