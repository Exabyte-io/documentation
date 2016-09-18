<!-- by MH -->

Combinatorial sets are used to study a wide variety of modifications to a base crystal structure through substitution of elements at particular atomic positions.  To this end it is possible to specify what elements are substituted for each atomic site in a structure and specify a different substituion rule for each position as well.

To activate combinatorial set generation, go to `Create Job` webpage. On this page near the upper right corner of the structure visualization you will see the corresponding button. To get more information to read on how to set up the combinatorics, click on the <i class="zmdi zmdi-info"></i> button.  The contents of the page are also displayed below.


# Overview

This feature lets users create multiple jobs at the same time using a combinatorial set of materials and input templates for workflows.

The combinatorial part is reflected in 2 input fields: `basis` and `lattice basis`
Any input line that has element characters separated by slashes or commas is triggering the generation of the set.

## Basis

Here's how you can activate combinatorial set and edit crystal basis. For example, above we have added P atom into the crystal basis of FCC Silicon such that combinatorial set will contain 2 materials - Si2 and SiP in diamond FCC lattice arrangements

<img data-gifffer="/images/ActivateCombinatorial.gif" />

### Permutations

Permutations change all elements in basis "at once" when separated by slashes

**1st scenario - input**
```
Si/Ge/As 0.0 0.0 0.0
Si/Ge    0.5 0.5 0.0
```

In case slashes are used the elements are changed all at once, eg. in the above case there will be 3 total basises created.

**Case 1 - structure used**
```
Si 0.0 0.0 0.0
Si 0.5 0.5 0.0
```
**Case 2 - structure used**
```
Ge 0.0 0.0 0.0
Ge 0.5 0.5 0.0
```
**Case 3 - structure used**
```
As 0.0 0.0 0.0
Ge 0.5 0.5 0.0
```

<hr>

### Combinations

**2nd scenario - input**
```
Si,Ge,As 0.0 0.0 0.0
Si,Ge    0.5 0.5 0.0
```
In case commas are used the elements are changed one at a time, eg. in the above case there will be 6 total basises created

**Case 1 - structure used**
```
Si 0.0 0.0 0.0
Si 0.5 0.5 0.0
```
**Case 2 - structure used**
```
Si 0.0 0.0 0.0
Ge 0.5 0.5 0.0
```
**Case 3 - structure used**
```
Ge 0.0 0.0 0.0
Si 0.5 0.5 0.0
```
**Case 4 - structure used**
```
Si 0.0 0.0 0.0
Si 0.5 0.5 0.0
```
**Case 5 - structure used**
```
As 0.0 0.0 0.0
Si 0.5 0.5 0.0
```
**Case 6 - structure used**
```
As 0.0 0.0 0.0
Ge 0.5 0.5 0.0
```

To see the result of these capabilities on the [input files generated](/models/combinatorial-set-input.md).

<BR>

## Lattice

Multiple lattices could also be selected at the same time from UI: for example BCC, FCC, SC. For each of them a new material will be created.

This functionality can be used by clicking on the + button in Combinatorial functionality, choosing the new lattice type, and updating as seen below.

<img data-gifffer="/images/AddCombinatorialCell.gif" />

!!! warning "Basis input units"
    When multiple lattices selection is used, the Basis input units are automatically converted to "crystal".
