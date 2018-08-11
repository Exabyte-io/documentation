# Combinatorial Sets

Combinatorial sets are used to study a variety of modifications to a base structure through substitution of elements at particular atomic positions. To this end it is possible to specify what elements are substituted for each atomic site in a structure and specify a different substitution rule for each position as well.

This feature lets users create multiple materials at the same time using an extended syntax for crystal basis (compared with regular XYZ format): an input line that has element characters separated by slashes or commas to generate elemental permutations or combinations respectively, as illustrated in the examples contained in the rest of this documentation page. Finally, we explain how combinations of vacancy sites instead of atoms can also be built. 

# Execute Combinatorial Sets

Once each combinatorial set is entered, click on "Generate Combinatorial Set" at the bottom of the dialog, and the corresponding set of structures will appear in the list on the left-hand sidebar of the Materials Designer.

# Permutations

Permutations change all elements in basis "at once" when separated by slashes, such as in the example lines below:

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

# Combinations

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

# Animation

...
