# Creating High-k Metal Gate Stack: Si/SiO2/HfO2/TiN

## Introduction

This tutorial demonstrates how to create a high-k metal gate stack heterostructure consisting of four materials: Si (substrate), SiO2 (gate oxide), HfO2 (high-k dielectric), and TiN (metal gate). The process involves:
1. Creating individual slabs for HfO2 and TiN
2. Building the Si/SiO2 interface using strain matching
3. Adding the pre-created slabs sequentially using simple interface builder

We use the [Materials Designer](../../../materials-designer/overview.md) to create the high-k metal gate stack.

## 1. Set Up Materials

First, navigate to Materials Designer and import from [Standata](../../../materials-designer/header-menu/input-output/standata-import.md) the following materials:
- Silicon (Si)
- Silicon dioxide (SiO2)
- Hafnium dioxide (HfO2)
- Titanium nitride (TiN)

![Standata Import](/images/tutorials/materials/heterostructures/heterostructure-high-k-metal-gate-stack/import-standata.webp "Standata Import")

## 2. Create HfO2 and TiN Slabs

Before building the stack, we need to create properly terminated slabs for HfO2 and TiN.

### 2.1. Create HfO2 Slab

More detailed instructions on slab creation can be found in the [SrTiO3 Slab](slab-strontium-titanate.md) tutorial.

Open `create_slab_with_termination.ipynb` and set parameters:

```python
# HfO2 slab parameters
MILLER_INDICES = (0, 0, 1)
THICKNESS = 4  # atomic layers
VACUUM = 0.5  # Angstroms
XY_SUPERCELL_MATRIX = [[1, 0], [0, 2]]
USE_ORTHOGONAL_Z = True
USE_CONVENTIONAL_CELL = True

# Select termination (usually first one is fine)
TERMINATION_INDEX = 0
```

Run the notebook to create the HfO2 slab and pass it to Materials Designer.

![HfO2 slab](/images/tutorials/materials/heterostructures/heterostructure-high-k-metal-gate-stack/wave-result-hfo2-slab-wave.webp "HfO2 slab")

### 2.2. Create TiN Slab

Open another instance of `create_slab_with_termination.ipynb` for TiN:

```python
# TiN slab parameters
MILLER_INDICES = (0, 0, 1)
THICKNESS = 3  # atomic layers
VACUUM = 10.0  # Angstroms - more vacuum for final layer
XY_SUPERCELL_MATRIX = [[1, 0], [0, 1]]
USE_ORTHOGONAL_Z = True
USE_CONVENTIONAL_CELL = True

TERMINATION_INDEX = 0
```

Run the notebook to create and pass the TiN slab to Materials Designer.

![TiN slab](/images/tutorials/materials/heterostructures/heterostructure-high-k-metal-gate-stack/wave-result-tin-slab.webp "TiN slab")

## 3. Create Si/SiO2 Interface

### 3.1. Launch ZSL Interface Builder

Open `create_interface_with_min_strain_zsl.ipynb` and configure:

```python
MAX_AREA = 200  # Maximum area for strain matching
MAX_AREA_RATIO_TOLERANCE = 0.25  # Maximum area ratio tolerance
MAX_ANGLE_TOLERANCE = 0.15  # Maximum angle tolerance
MAX_LENGTH_TOLERANCE = 0.15  # Maximum length tolerance

FILM_INDEX = 1  # SiO2
FILM_MILLER_INDICES = (1, 0, 0)
FILM_THICKNESS = 3
FILM_XY_SUPERCELL_MATRIX = [[1, 0], [0, 1]]
FILM_VACUUM = 0.0
FILM_USE_ORTHOGONAL_Z = True

SUBSTRATE_INDEX = 0  # Si
SUBSTRATE_MILLER_INDICES = (1, 0, 0)
SUBSTRATE_THICKNESS = 4
SUBSTRATE_XY_SUPERCELL_MATRIX = [[1, 0], [0, 1]]
SUBSTRATE_VACUUM = 5.0
SUBSTRATE_USE_ORTHOGONAL_Z = True

INTERFACE_DISTANCE = 2.5  # Angstroms
INTERFACE_VACUUM = 5.0  # Angstroms
TERMINATION_PAIR_INDEX = 0
```

We set a higher tolerances to achieve smaller cell with higher strain of the film (SiO2).

![Interface Setup](/images/tutorials/materials/heterostructures/heterostructure-high-k-metal-gate-stack/jl-setup-notebook-si-sio2.webp "Interface Setup")

### 3.2. Create Initial Interface

Run the notebook to create the Si/SiO2 interface. This is the most critical interface, so we use strain matching to optimize it.

## 4. Add HfO2 Layer

### 4.1. Configure Simple Interface Builder

Open JupyterLite Session again and select the Si/SiO2 interface and HfO2 slab as input materials.

Open `create_interface_with_no_strain.ipynb` and set:

```python
# Important: Disable slab creation since we're using pre-created slab
ENABLE_FILM_SCALING = True
CREATE_SLABS = False  # We already have our HfO2 slab

FILM_INDEX = 1  # Pre-created HfO2 slab
SUBSTRATE_INDEX = 0  # Si/SiO2 structure

# Interface parameters
INTERFACE_DISTANCE = 2.5  # Angstroms
INTERFACE_VACUUM = 0.5  # Angstroms
```

Film is the material that will be strained (scaled) to match the substrate.

![HfO2 Interface Setup](/images/tutorials/materials/heterostructures/heterostructure-high-k-metal-gate-stack/jl-setup-notebook-si-sio2-hfo2.webp "HfO2 Interface Setup")

### 4.2. Add HfO2

Run the notebook to add the pre-created HfO2 slab to the Si/SiO2 structure.

![Si/SiO2/HfO2](/images/tutorials/materials/heterostructures/heterostructure-high-k-metal-gate-stack/wave-result-si-sio2-hfo2.webp "Si/SiO2/HfO2")

## 5. Add TiN Layer

### 5.1. Configure Final Layer Addition

Similar to steps in Section 4, we add the TiN layer to the Si/SiO2/HfO2 stack.

Use `create_interface_with_no_strain.ipynb` again:

```python
# Keep slabs disabled
ENABLE_FILM_SCALING = True
CREATE_SLABS = False  # Using pre-created TiN slab

FILM_INDEX = 1  # Pre-created TiN slab
SUBSTRATE_INDEX = 0  # Si/SiO2/HfO2 structure

# Final interface parameters
INTERFACE_DISTANCE = 2.5  # Angstroms
INTERFACE_VACUUM = 10.0  # Final vacuum spacing
```

### 5.2. Complete the Stack

Run the notebook to add the TiN layer and complete the stack.

![Final Stack](/images/tutorials/materials/heterostructures/heterostructure-high-k-metal-gate-stack/wave-result-si-sio2-hfo2-tin.webp "Final Stack")


## References

1. **D. A. Muller et al.**
    "The electronic structure at the atomic scale of ultrathin gate oxides"
    Nature 399, 758–761 (1999)
    [DOI: 10.1038/21602](https://doi.org/10.1038/21602)

2. **J. Robertson**
    "High dielectric constant gate oxides for metal oxide Si transistors"
    Reports on Progress in Physics 69, 327 (2006)
    [DOI: 10.1088/0034-4885/69/2/R02](https://doi.org/10.1088/0034-4885/69/2/R02)

## Tags

`slab-creation`, `interfaces`, `high-k`, `metal-gate`, `semiconductor`, `heterostructure`, `strain-matching`