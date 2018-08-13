# Advanced tab

Advanced features of the Materials Designer can be accessed through the `Advanced` menu. Such features are designed to help the user build complex crystalline structures, in particular Supercells, Surfaces/Slabs, Polymers and Nanotubes. The possibility to generate different combinations of atoms or vacancies of different elements under a common underlying structural framework (combinatorial sets) is also offered. 

# Supercells

Under the `Advanced` menu, you may create supercells or multiplicative representations of a smaller building block in space. For example, silicon with a 2 atom unit cell, being replicated by 2x2x2 leads to a supercell with 8 copies of primitive unit cell and 16 atoms total.

The supercell overlay will allow you to set parameters of the supercell matrix.  When finished setting up the transformation matrix, click on "Submit" and both the "Crystal Basis" and 3D representation of the structure will change accordingly.

Click on the animation below to see the above in action:

<img data-gifffer="/images/CreateMaterialSupercell.gif" />

Please note that you are multiplying the structure of what is currently represented in the "Crystal Basis" and 3D visualization window.  If Si is replicated by 2x2x2, that results in a 16 atom supercell.  If you then do another 2x2x2 replication, that will result in a 128-atom Si supercell.

# Combinatorial sets 

Combinatorial sets are used to study a variety of modifications to a base structure through substitution of elements at particular atomic positions. To this end it is possible to specify what elements are substituted for each atomic site in a structure and specify a different substitution rule for each position as well.

This feature lets users create multiple materials at the same time using an extended syntax for crystal basis (compared with regular XYZ format): an input line that has element characters separated by slashes or commas to generate elemental permutations or combinations respectively, as explained in the following examples (once each combinatorial set is entered, click on "Generate Combinatorial Set" at the bottom of the dialog, and the corresponding set of structures will appear in the list on the left-hand sidebar of the Materials Designer).

## Permutations

Permutations change all elements in basis "at once" when separated by slashes.

**1st scenario - input**
```txt
Si/Ge/As 0.0 0.0 0.0
Si/Ge    0.5 0.5 0.0
```
In case slashes ("/") are used as separators, the elements are changed all at once, eg. there will be 3 total bases created in the above example:

**Case 1 - structure generated**
```txt
Si 0.0 0.0 0.0
Si 0.5 0.5 0.0
```
**Case 2 - structure generated**
```txt
Ge 0.0 0.0 0.0
Ge 0.5 0.5 0.0
```
**Case 3 - structure generated**
```txt
As 0.0 0.0 0.0
Ge 0.5 0.5 0.0
```

## Combinations

In case commas (",") are used as separators, the elements are changed one at a time.

**1st scenario - input**
```
Si, P    0.0 0.0 0.0
Si       0.5 0.5 0.0
```

In the above example we have added P atom into the crystal basis of FCC Silicon such that combinatorial set will contain 2 materials - Si2 and SiP in diamond FCC lattice arrangements.

**2nd scenario - input**
```
Si,Ge,As 0.0 0.0 0.0
Si,Ge    0.5 0.5 0.0
```

There will be 6 total bases created in the example above:

**Case 1 - structure generated**
```
Si 0.0 0.0 0.0
Si 0.5 0.5 0.0
```
**Case 2 - structure generated**
```
Si 0.0 0.0 0.0
Ge 0.5 0.5 0.0
```
**Case 3 - structure generated**
```
Ge 0.0 0.0 0.0
Si 0.5 0.5 0.0
```
**Case 4 - structure generated**
```
Si 0.0 0.0 0.0
Si 0.5 0.5 0.0
```
**Case 5 - structure generated**
```
As 0.0 0.0 0.0
Si 0.5 0.5 0.0
```
**Case 6 - structure generated**
```
As 0.0 0.0 0.0
Ge 0.5 0.5 0.0
```

# Surface / slab

Surfaces / slabs can easily be designed and generated with the Materials Designer upon entering information about the Miller indices of the corresponding crystal plane, the thickness of the slab in terms of layers, the vacuum ratio, and the supercell dimensions in both the planar x and y dimensions. Click on "Submit" once this information has been entered, and the corresponding surface / slab will appear in the graphical viewer. 

