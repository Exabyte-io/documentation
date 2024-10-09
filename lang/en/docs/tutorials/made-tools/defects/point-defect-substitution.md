# Create materials with substitution defects from the paper 

This tutorial guides to create materials from "Formation, stabilities, and electronic properties of nitrogen defects in graphene" https://journals.aps.org/prb/abstract/10.1103/PhysRevB.84.245446 paper.

## Pre-requisites

This tutorial assumes that the user knows how to:

- Open [Materials Designer](../../../materials-designer/overview.md).
- Launch [JupyterLite Session](../../../jupyterlite/overview.md) (inside Materials Designer) or Jupyter Notebook (on the local machine).
- Import materials into Materials Designer (from Standata, Materials Bank or as upload).
- Pass data between JupyterLite Session or Jupyter Notebook and outside runtime.

## 1. Procedure overview

- Import Graphene material into Materials Designer and load in JupyterLite Session.
- Create a 5x5 supercell of Graphene to introduce substitution defects. 
- Set the method, approximate coordinate and element of the defect atom to be added to the Graphene supercell.
- Run the notebook to create a material with substitution defects in Graphene.
- Review the results.

## 2. Adjust notebook settings

For the expected material we will use approximate coordinates to place the substituting atom since it's easier to do that based on the picture from the paper.

To replicate the material from FIG. 1. a) of the paper: 

<img src="/images/tutorials/made-tools/defects/point_defect_substitution/point_defect_substitution_0.png" title="FIG. 1. a)">

we will use the following settings:

```python
METHOD = "approximate_coordinate" 
DEFECT_TYPE = "substitution"
APPROXIMATE_COORDINATE = [0.5, 0.5, 0.5]    
CHEMICAL_ELEMENT = "N"
SUPERCELL_MATRIX = [[5, 0, 0], [0, 5, 0], [0, 0, 1]]

```
## 3. Run the Notebook

Run the notebook to create a material with substitution defects in Graphene.

## 4. Analyze the Results

After running the notebook, the user will be able to visualize the structure of Graphene with substitution defects.

## 5. Save the Material

The user can save the material with substitution defects in the current Materials Designer session.

Or the user can download the material in Material JSON format or POSCAR format.

## Try notebook in JupyterLite

{% with notebook_name='create_point_defect.ipynb' %}
{% include 'includes/jupyterlite_embed.html' %}
{% endwith %}