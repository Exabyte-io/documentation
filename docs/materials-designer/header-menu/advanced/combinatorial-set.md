# Combinatorial Sets

The possibility to generate different combinations of atoms or vacancies of different elements under a common underlying structural framework (combinatorial sets) is also offered in the `Advanced` menu on the header bar of the Materials Designer interface.

# What are combinatorial sets?

Combinatorial sets are used to study a variety of modifications to a base structure through substitution of elements at particular atomic positions. To this end it is possible to specify what elements are substituted for each atomic site in a structure and specify a different substitution rule for each position as well.

In particular, this feature lets users create multiple materials at the same time using an extended syntax for crystal basis (compared with regular XYZ format): an input line that has element characters separated by slashes or commas to generate elemental permutations or combinations respectively, as illustrated in the examples contained in the rest of this documentation page. 

# Why are combinatorial sets useful?

Imagine a scenario where tens or even hundreds of different binary or ternary semiconductors, or different metallic alloys, have to be studied as part of a common project to determine which particular composition (combination of element types) produces the most suitable material properties to achieve certain desired technological objectives. This is an example application where the user will find combinatorial sets to be particularly resourceful and time-effective.

# The "Generate Combinatorial Set" dialog

Open the "Generate Combinatorial Set" dialog via the `Advanced` menu. The dialog has the following appearance:

<img src="/images/Generate-Combinatorial-Set.png"/>
 
In particular, the dialog features a central text field where each line of the desired combinatorial set can be inserted or edited, according to the format illustrated in the forthcoming examples. 

# Permutations

Permutations change all elements in basis "at once" when separated by slashes ("/" - with no trailing spaces), such as in the example lines below:

**1st scenario - input**
```txt
Si/Ge/As 0.0 0.0 0.0
Si/Ge    0.5 0.5 0.0
```
Hence, according to the above combinatorial set, the following three distinct crystal structures will be generated:

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

In case commas ("," - with no trailing spaces) are used as separators, the elements are changed one at a time, such as demonstrated in the example below:

**1st scenario - input**
```
Si, P    0.0 0.0 0.0
Si       0.5 0.5 0.0
```

In the above example, we have added a P atom into the crystal basis of FCC Silicon, such that combinatorial set will contain two materials - Si2 and SiP in diamond FCC lattice arrangements.

The following is a more exhaustive example:

**2nd scenario - input**
```
Si,Ge,As 0.0 0.0 0.0
Si,Ge    0.5 0.5 0.0
```

This time, there will be a total of six distinct crystal structures created:

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

An example of combinatorial set generation is offered in the animation below. Six different combinations are generated starting from a pure silicon sample, based on alternations between the elements Si, Ge and C in much the same way as the second combination example above was presented. At the end of the combinatorial set generation process, each resulting crystal structure combination in the items list sidebar is reviewed in turn to highlight their difference in atomic composition, and at the same time the similarity in their underlying structural framework: 

<img data-gifffer="/images/CreateCombinatorialSet.gif" />

# Vacancy sites

Interstitial vacancies can be added as part of the generated combinatorial set via the "VAC" keyword. This keyword can be inserted in very much the same way as an element name, and can be combined with either slashes to generate corresponding permutations, or commas for combinations (with no trailing spaces). 

This feature is best demonstrated by way of an example:

**1st scenario - input**
```
Si,VAC,Ge  0.0 0.0 0.0
Si,Ge      0.25 0.25 0.25
```

As expected,  a new set of six distinct crystal structures is generated:

**Case 1 - structure generated**
```
Si 0.0  0.0  0.0
Si 0.25 0.25 0.25
```
**Case 2 - structure generated**
```
Si 0.0  0.0  0.0
Ge 0.25 0.25 0.25
```
**Case 3 - structure generated**
```
Si 0.25 0.25 0.25
```
**Case 4 - structure generated**
```
Ge 0.25 0.25 0.25
```
**Case 5 - structure generated**
```
Ge 0.0  0.0  0.0
Si 0.25 0.25 0.25
```
**Case 6 - structure generated**
```
Ge 0.0  0.0  0.0
Ge 0.25 0.25 0.25
```

# Execute Combinatorial Sets

Once the text of the desired combinatorial set is entered, click on "Generate Combinatorial Set" at the bottom of the dialog of the same name, and the corresponding set of structures will appear in the list on the left-hand items sidebar of the Materials Designer interface.
