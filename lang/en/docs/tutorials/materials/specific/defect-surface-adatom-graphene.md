---
# YAML header
render_macros: true
---

# Adatom on Graphene Surface

## Introduction

This tutorial demonstrates the process of creating a graphene structure with an adatom on the surface based on the work presented in the following manuscript.

!!!note "Manuscript"
    **Kevin T. Chan, J. B. Neaton, and Marvin L. Cohen**, 
    "First-principles study of metal adatom adsorption on graphene" Phys. Rev. B 77, 235430, 2008
    [DOI: 10.1103/PhysRevB.77.235430](https://doi.org/10.1103/PhysRevB.77.235430){:target='_blank'}.

We use the [Materials Designer](../../../materials-designer/overview.md) to create a graphene structure with a metal adatom on the surface.

The image shows the adatom on the graphene surface.

![Adatom on Graphene Surface](/images/tutorials/materials/specific/defect-surface-adatom-graphene/adatom-on-graphene.png "Adatom on Graphene Surface")

## 1. Load and preview Graphene structure

First, we navigate to [Materials Designer](../../../materials-designer/overview.md) and import the Graphene material from the [Standata](../../../materials-designer/header-menu/input-output/standata-import.md).

![Standata Graphene Import](/images/tutorials/materials/specific/defect-surface-adatom-graphene/standata-import-graphene.png "Standata Graphene Import")

Then we will use the [JupyterLite](../../../jupyterlite/overview.md) environment to create a graphene structure with an adatom on the surface.

## 2. Graphene structure with Li adatom

### 2.1 Launch JupyterLite Session

Select the "Advanced > [JupyterLite Transformation](../../../materials-designer/header-menu/advanced/jupyterlite-dialog.md)" menu item to launch the JupyterLite environment.

![JupyterLite Dialog](/images/jupyterlite/md-advanced-jl.webp "JupyterLite Dialog")

### 2.2. Open and modify the notebook

Next, edit `create_adatom_defect.ipynb` notebook to modify the parameters by changing values:
- `CHEMICAL_ELEMENT = "Li"` - the element of the adatom
- `APPROXIMATE_POSITION_ON_SURFACE = [0.5, 0.5]` - position that corresponds to the hollow site in the center of the cell
- `DISTANCE_Z = 1.71` - the distance between the adatom and the graphene surface (from the Table 1 in the manuscript)
- `MILLER_INDICES = (0,0, 1)` - the Miller indices of the plane of Graphene
- `SLAB_THICKNESS = 1` - the thickness of the Graphene monolayer slab 
- `SUPERCELL_MATRIX = [[4, 0, 0], [0, 4, 0], [0, 0, 1]]` - the supercell matrix

Adjust the "1.1. Set up slab parameters" cell in the notebook according to:

```python
DEFECT_TYPE = "adatom"  
PLACEMENT_METHOD = "equidistant"
CHEMICAL_ELEMENT = "Li"  
APPROXIMATE_POSITION_ON_SURFACE = [0.5, 0.5]  
USE_CARTESIAN_COORDINATES = False 
DISTANCE_Z = 1.71

# Slab parameters
MILLER_INDICES = (0, 0, 1)  
SLAB_THICKNESS = 1  
VACUUM = 6 
SUPERCELL_MATRIX = [[4, 0, 0], [0, 4, 0], [0, 0, 1]] 
```

### 2.3. Run the notebook

Run the notebook by selecting "Run > Run All Cells" from the menu.

![Run All](/images/jupyterlite/run-all.webp "Run All")

### 2.4. Analyze the Results

After running the notebook, the Graphene structure with a Li adatom on the surface will be created.

The user will be able to visualize the created structure and download the corresponding files.

![Adatom on Graphene Surface](/images/tutorials/materials/specific/defect-surface-adatom-graphene/jl-result-preview-li.png "Li Adatom on Graphene Surface")

### 2.5. Pass the Material to Materials Designer

After reviewing the results, the user can pass the material to Materials Designer for further analysis.

![Final Material](/images/tutorials/materials/specific/defect-surface-adatom-graphene/wave-result-li.png "Li Adatom on Graphene Surface")

Or the user can [save or download](../../../materials-designer/header-menu/input-output.md) the material in Material JSON format or POSCAR format.

## 3. Graphene with other metals adatoms

### 3.1. Repeat the steps above

To create a Graphene structure with other metal adatoms, repeat the steps above by changing the `CHEMICAL_ELEMENT`, `APPORXIMATE_POSITION_ON_SURFACE`, and `DISTANCE_Z` parameters according to he values in the table 1 of the manuscript.




