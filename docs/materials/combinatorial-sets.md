<!-- by MH -->

Combinatorial sets are used to study a wide variety of modifications to a base crystal structure through atomic substituion of elements at particular atomic positions.  To this end it is possible to specify what elements are substituted for each element in a structure and specify a different substituion rule for each position in the atomic structure as well.

To activate this capability, go to the `Create Job` webpage.  On this page near the upper right corner of the three dimensional window showing the visual representation of the atoms you will see a box called `Activate Comibinatorial`.  If you click on this button new functionality will appear on your screen that may not be immediately self-explanatory.  To get more information to read on how to set up the combinatorics, click on the `i` information button.  The contents of that page are also displayed below as well.

<img data-gifffer="/images/ActivateCombinatorial.gif" />


# Feature Overview
This feature lets users create multiple jobs at the same time using a combinatorial set of materials and input templates for workflows.

The combinatorial part is reflected in 2 input fields: `basis` and `lattice basis`
Any input line that has element characters separated by slashes is triggering the generation of the set.

## Basis

### Permutations
<details>
<summary>**Quantum Espresso - 1st scenario - input**</summary>
```py
Si/Ge/As 0.0 0.0 0.0
Si/Ge    0.5 0.5 0.0
```
</details>

In case slashes are used the elements are changed all at once, eg. in the above case there will be 3 total basises created

<details>
<summary>**Quantum Espresso - Case 1 - executed structure**</summary>
```
Si 0.0 0.0 0.0
Si 0.5 0.5 0.0
```
</details>
<details>
<summary>**Quantum Espresso - Case 2 - executed structure**</summary>
```
Ge 0.0 0.0 0.0
Ge 0.5 0.5 0.0
```
</details>
<details>
<summary>**Quantum Espresso - Case 3 - executed structure**</summary>
```
As 0.0 0.0 0.0
Ge 0.5 0.5 0.0
```
</details>

### Combinations
<details>
<summary>**Quantum Espresso - 2nd scenario - input**</summary>
```
Si,Ge,As 0.0 0.0 0.0
Si,Ge    0.5 0.5 0.0
```
</details>

In case commas are used the elements are changed one at a time, eg. in the above case there will be 6 total basises created

<details>
<summary>**Quantum Espresso - Case 1 - executed structure**</summary>
```
Si 0.0 0.0 0.0
Si 0.5 0.5 0.0
```
</details>
<details>
<summary>**Quantum Espresso - Case 2 - executed structure**</summary>
```
Si 0.0 0.0 0.0
Ge 0.5 0.5 0.0
```
</details>
<details>
<summary>**Quantum Espresso - Case 3 - executed structure**</summary>
```
Ge 0.0 0.0 0.0
Si 0.5 0.5 0.0
```
</details>
<details>
<summary>**Quantum Espresso - Case 4 - executed structure**</summary>
```
Si 0.0 0.0 0.0
Si 0.5 0.5 0.0
```
</details>
<details>
<summary>**Quantum Espresso - Case 5 - executed structure**</summary>
```
As 0.0 0.0 0.0
Si 0.5 0.5 0.0
```
</details>
<details>
<summary>**Quantum Espresso - Case 6 - executed structure**</summary>
```
As 0.0 0.0 0.0
Ge 0.5 0.5 0.0
```
</details>

To see the result of these capabilities on the [input files generated](/models/combinatorial-set-input.md).

<BR>

## Lattice

Multiple lattices could also be selected at the same time from UI: for example BCC, FCC, SC. For each of them a new material will be created.

This functionality can be used by clicking on the + button in Combinatorial functionality, choosing the new lattice type, and updating as seen below.

<img data-gifffer="/images/AddCombinatorialCell.gif" />

!!! warning "Basis input units"
    When multiple lattices selection is used, the Basis input units should be automatically converted to "crystal".