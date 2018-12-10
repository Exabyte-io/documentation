# Combinatorial Sets

There is a quick way to generate different stoichiometric combinations of elements (or vacancies) inside a common structural framework (cell) is offered in the `Advanced` menu of the header bar of the Materials Designer.

## What are combinatorial sets?

Combinatorial sets are used to study a variety of modifications to a base structure through the substitution of elements at particular atomic positions. To this end it is possible to specify what elements are substituted for each atomic site in a structure and specify a different substitution rule for each position as well.

## Why are combinatorial sets useful?

This feature lets users create multiple materials at once using an extended syntax for crystal basis as explained below. When a study involves a screening of a large number (eg. hundreds, thousands) of different compounds (or alloys) in order to identify the ones that possess a target property with a desired technological objectives. users might find combinatorial sets to be particularly resourceful and time-efficient.

## The Generation Dialog

Open the "Generate Combinatorial Set" dialog via the `Advanced` menu. The dialog has the following appearance:

<img src="/images/materials-designer/Generate-Combinatorial-Set.png"/>
 
The dialog features a text field where the crystal basis of the desired combinatorial set can be edited, according to the format illustrated in the forthcoming examples. During the generation, the crystal lattice parameters will be taken for the currently selected structure. 

## Combinatorial Basis format

Combinatorial Basis syntax is a superset of the basis representation format explained [here](../../../materials-designer/source-editor/basis.md)). The characters denoting the chemical elements are separated by slashes or commas to generate "permutations" or "combinations", as illustrated in the following examples.

> NOTE: permutations and combinations have to be used independently and NOT within the same basis context.

### Permutations

Permutations change all elements in basis simultaneously and are enabled when chemical elements are separated by slashes (`/`) with no trailing spaces, such as in the example lines below:

**Input**
```txt
Si/Ge/As 0.0 0.0 0.0
Si/Ge    0.5 0.5 0.0
```
Hence, according to the above combinatorial set, the following 3 distinct structures will be generated:

**Case 1 - basis generated**
```txt
Si 0.0 0.0 0.0
Si 0.5 0.5 0.0
```
**Case 2 - basis generated**
```txt
Ge 0.0 0.0 0.0
Ge 0.5 0.5 0.0
```
**Case 3 - basis generated**
```txt
As 0.0 0.0 0.0
Ge 0.5 0.5 0.0
```

### Combinations

Combinations change the elements one at a time and are enabled when commas are used as separators (`,`) with no trailing spaces. This is demonstrated in the example below:

**Input**
```
Si,Ge,As 0.0 0.0 0.0
Si,Ge    0.5 0.5 0.0
```

This time, there will be a total of 6 structures created:

**Case 1 - basis generated**
```txt
Si 0.0 0.0 0.0
Si 0.5 0.5 0.0
```
**Case 2 - basis generated**
```txt
Si 0.0 0.0 0.0
Ge 0.5 0.5 0.0
```
**Case 3 - basis generated**
```
Ge 0.0 0.0 0.0
Si 0.5 0.5 0.0
```
**Case 4 - basis generated**
```txt
Si 0.0 0.0 0.0
Si 0.5 0.5 0.0
```
**Case 5 - basis generated**
```txt
As 0.0 0.0 0.0
Si 0.5 0.5 0.0
```
**Case 6 - basis generated**
```txt
As 0.0 0.0 0.0
Ge 0.5 0.5 0.0
```

### Vacancy sites

Vacancies can be added as part of the generated combinatorial set via the "VAC" keyword. This keyword can be inserted in the same way as an element name, and can be combined with either slashes to generate corresponding permutations, or commas for combinations (with no trailing spaces). 

**1st scenario - input**
```txt
Si,VAC,Ge  0.0 0.0 0.0
Si,Ge      0.25 0.25 0.25
```

As expected, a set of six structures is generated. Note the vacancy (missing atom) at site `0.0 0.0 0.0` in cases 3 and 4.

**Case 1 - basis generated**
```
Si 0.0  0.0  0.0
Si 0.25 0.25 0.25
```
**Case 2 - basis generated**
```
Si 0.0  0.0  0.0
Ge 0.25 0.25 0.25
```
**Case 3 - basis generated**
```
Si 0.25 0.25 0.25
```
**Case 4 - basis generated**
```
Ge 0.25 0.25 0.25
```
**Case 5 - basis generated**
```
Ge 0.0  0.0  0.0
Si 0.25 0.25 0.25
```
**Case 6 - basis generated**
```
Ge 0.0  0.0  0.0
Ge 0.25 0.25 0.25
```

## Generate Combinatorial Sets 

Once the text of the desired combinatorial set is entered, click on "Generate Combinatorial Set" at the bottom of the dialog of the same name, and the corresponding set of structures will appear in the list on the left-hand items [sidebar](../../sidebar-items.md) of the Materials Designer interface.

## Animation

An example of combinatorial set generation is in the animation below. Six different combinations are generated starting from a pure silicon sample, based on alternations between the elements Si, Ge and C following the second combination example above. At the end, each resulting crystal structure is reviewed to highlight the difference in atomic composition (crystal basis) and similarity in their underlying structural framework (crystal lattice). 

<img data-gifffer="/images/materials-designer/CreateCombinatorialSet.gif" />
