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
- Set the `approximate coordinate` and `element` of the defect atom and the `supercell matrix` for the Graphene supercell.
- Run the notebook to create a material with substitution defects in Graphene.
- Review the results.

## 1. Adjust notebook settings

For the desired material we will use approximate coordinates to place the substituting atom since it's easier to do that based on the picture from the paper.
The notebook will use that `APPROXIMATE_COORDINATE` parameter to create corresponding configuration and ignore other methods. 

To replicate the material from FIG. 1. a) of the paper: 

<img src="/images/tutorials/made-tools/defects/point_defect_substitution/point_defect_substitution_0.webp" title="FIG. 1. a)">

we will use the following settings:

```python
DEFECT_TYPE = "substitution"
SITE_ID = None # `from_site_id` method will be ignored
COORDINATE = None # default method will be ignored
APPROXIMATE_COORDINATE = [0.51, 0.5, 0.5]    
CHEMICAL_ELEMENT = "N"
SUPERCELL_MATRIX = [[5, 0, 0], [0, 5, 0], [0, 0, 1]]

```
## 2. Run the Notebook

Run the notebook by clicking `Run` > `Run All` in the top menu to run cells and wait for the results to appear.

## 3. Analyze the Results

After running the notebook, the user will be able to visualize the structure of Graphene with substitution defects.

<img src="/images/tutorials/made-tools/defects/point_defect_substitution/point_defect_substitution_1.webp" title="Graphene with substitution defects">

## 4. Save the Material

The user can pass the material with substitution defects in the current Materials Designer environment and save it.

Or the user can download the material in Material JSON format or POSCAR format.

## Interactive JupyterLite Notebook

{% with notebook_name='create_point_defect.ipynb' %}
{% include 'includes/jupyterlite_embed.html' %}
{% endwith %}