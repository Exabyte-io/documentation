# Generate Combinatorial Sets

This tutorial demonstrates how to create a **combinatorial set** of III-V compound semiconductor materials with permutations and combinations of n and p-type dopants. This **combinatorial screening** could for example be used to investigate the impact of inserting dopants onto the [electronic band gap](../../properties-directory/non-scalar/band-gaps.md) of such semiconductors. 

We shall make use of [Quantum ESPRESSO](../../software-directory/modeling/quantum-espresso/overview.md) as our simulation engine for this tutorial.

## Import Material into Account-owned Collection

We begin by importing one of the III-V compound semiconductors, Gallium Phosphide (GaP), into the user's [collection](../../accounts/collections.md) of materials, starting from which we will then build further combinatorial sets. This crystal structure can be imported directly from the Materials Project repository, by following the instructions outlined in [this page](../../materials/actions/import.md) (the F-43m space group option is the lowest energy polymorph for GaP). 

## Import Material into Materials Designer

The reader should now [open](../../entities-general/actions/create.md) a new instance of the [Materials Designer Interface](../../materials-designer/overview.md) for creating and designing new material structures. The first step here involves importing the above-mentioned Gallium Phosphide crystal structure into the designer itself, via the [Import option](../../materials-designer/header-menu/input-output/import.md) under the [Input/Output Menu](../../materials-designer/header-menu/input-output.md) of the interface.

## Create Combinatorial Set

### Open "Generate Combinatorial Set" Dialog

The functionality to create combinatorial sets can be accessed via the [Advanced Menu](../../materials-designer/header-menu/advanced.md) of the [Materials Designer Interface](../../materials-designer/overview.md). Under this "Advanced Menu", the user should select the relevant "Combinatorial Set" option. The operations of the resulting "Generate Combinatorial Set" dialog are reviewed in detail [in this page](../../materials-designer/header-menu/advanced/combinatorial-set.md). 

### n and p-type Dopants for Gallium Phosphide

We will examine the effects of n and p-type dopants on Gallium Phosphide. We remind the reader about which elements represent dopant atoms when inserted in Gallium Phosphide.

- n-type: tellurium, selenium, sulphur (substituting phosphorus).
- p-type: zinc, magnesium (substituting Ga), tin (substituting P).

### Generate Permutations

**Permutations** change all element atoms in the [basis](../../properties-directory/structural/basis.md) of the crystal structure simultaneously, and are enabled when chemical elements are separated by slashes (`/`) with no trailing spaces.

The user should try replacing the first line under the "Generate Combinatorial Set" dialog, containing the Gallium atom located at the origin of the unit cell, with the following line.

```text
Zn/Mg 0.0 0.0 0.0
```

Pressing the "Generate Combinatorial Set" button at the bottom of the dialog will generate permutations of the Gallium Phosphide crystal structure containing p-type dopants, which are added to the [left-hand sidebar list of structures](../../materials-designer/sidebar-items.md) of Materials Designer on top of the original GaP material structure.

Hence, if the basis atoms of the original GaP structure had the following atomic positions, expressed in fractional coordinates and viewable under the [source editor](../../materials-designer/source-editor/basis.md) interface component:

```text
Ga     0.000000    0.000000    0.000000 
P      0.750000    0.750000    0.750000 
```

Consequently, the resulting permutations will consist in the following two crystal structures:

```text
Zn     0.000000    0.000000    0.000000 
P      0.750000    0.750000    0.750000 
```

```text
Mg     0.000000    0.000000    0.000000 
P      0.750000    0.750000    0.750000 
```

Therefore, we see how permutations had the effect of replacing the original Gallium atom at the origin with each of the Zinc and Magnesium p-type dopants.

### Generate Combinations

**Combinations** change the elements in the [basis](../../properties-directory/structural/basis.md) of the crystal structure one at a time, and are enabled when commas are used as separators (`,`) with no trailing spaces. 

In order to explore the alternative case of Combinations, we shall replace both the Phosphorus and Gallium atoms in GaP with all possible aforementioned n and p-type dopant atoms. This can be achieved by replacing the two lines in the "Generate Combinatorial Set" dialog with the following content.

```text
Zn,Mg           0.000000    0.000000    0.000000
Te,Se,S,Sn      0.750000    0.750000    0.750000 
```

We reproduce below the resulting combinatorial list of atomic positions, which can be retrieved under the [left-hand sidebar list of structures](../../materials-designer/sidebar-items.md) of Materials Designer once the "Generate Combinatorial Set" button is clicked.

```text
Zn     0.000000    0.000000    0.000000 
Te     0.750000    0.750000    0.750000 
```

```text
Zn     0.000000    0.000000    0.000000 
Se     0.750000    0.750000    0.750000 
```

```text
Zn     0.000000    0.000000    0.000000 
S      0.750000    0.750000    0.750000 
```

```text
Zn     0.000000    0.000000    0.000000 
Sn     0.750000    0.750000    0.750000 
```

```text
Mg     0.000000    0.000000    0.000000 
Te     0.750000    0.750000    0.750000 
```

```text
Mg     0.000000    0.000000    0.000000 
Se     0.750000    0.750000    0.750000 
```

```text
Mg     0.000000    0.000000    0.000000 
S      0.750000    0.750000    0.750000 
```

```text
Mg     0.000000    0.000000    0.000000 
Sn     0.750000    0.750000    0.750000 
```

### Generate Vacancy Sites

When the "VAC" keyword is used instead of an element name, such as "Ga" or "P", a vacancy will be created at the corresponding crystal site. Vacancies can be added as part of the generated combinatorial set, and can be combined with either slashes to generate corresponding permutations, or commas for combinations (with no trailing spaces). 

An example of this functionality is provided [in this page](../../materials-designer/header-menu/advanced/combinatorial-set.md#vacancy-sites).

## Animation

We demonstrate how the above-mentioned combinatorial sets can be generated within [Materials Designer](../../materials-designer/overview.md) in the following animation, where we first import the original Gallium Phosphide crystal structure.

<div class="video-wrapper">
<iframe class="gifffer" width="100%" height="100%" src="https://www.youtube.com/embed/em55roTB7fc" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>
