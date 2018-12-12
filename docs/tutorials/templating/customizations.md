# Tutorial: Custom Input Script Templates with the Jinja Engine

We provide in the present tutorial some examples on how [templates](../../workflows/templating/overview.md), for generating simulation input scripts, can be written and customized by the user using the [Jinja syntax and template engine](../../workflows/templating/engine.md) implemented on our platform.

Templates and their respective Contexts can be entered under [Workflow Designer](../../workflow-designer/overview.md), as introduced [here](../../workflows/templating/ui.md).

## Example: Setting Input Parameters for VASP

The code below automatically sets the value of the "encut" variable to higher values for materials that contain Aluminum within their structures than for those than don't. In particular, encut = 600 eV if Aluminium is present, or encut = 450 eV otherwise. This variable is typically found in [VASP](../../software/modeling/vasp.md) input scripts, for defining the plane-wave cutoff energy characterizing the precision of the [DFT computation](../../models/dft/overview.md) to be executed on the material structure under investigation.                   

```jinja2
{% set high_cutoff_element = "Al" %}
{% set poscar_string = input.POSCAR|e("js") %}
{% set atoms = poscar_string.split('direct')[0] %}
{% set lines = atoms.split("\u000A") %}
{% set element_lines = lines[5] %}
{% if element_lines.includes(high_cutoff_element) %}
{% set encut = 600 %}
{% else %}
{% set encut = 450 %}
{% endif %}
encut ={{ encut }}
```

Each line number in the above block of statements is described in what follows.

### 1. Set Element Requiring Higher Cutoff Parameter (Aluminum)

We begin by defining the element that needs a high plane-wave cutoff to be "Al" for Aluminum, using the [set statement](../../workflows/templating/engine.md#variables-assignment).

### 2. Read POSCAR File Contents

We then read the POSCAR input file for [VASP](../../software/modeling/vasp.md), containing the numerical data defining the crystal structure, and assign the text contents of this file to the variable "poscar_string". Examples of POSCAR files are included at the end of this section.

### 3 - 5. Extract Elements Contained in Material

We then identify the lines within the POSCAR file containing the element chemical symbols, by using the "split" function for breaking up the file text contents at every occurrence of the argument passed to this function (the functioning and format of this split function is analogous to its Python counterpart [^1]). 

We first break the lines at the mention of the "direct" string, and take all the preceding content. We then split this content at every new line (denoted by the newline unicode character "\u000A"). As can be seen from the POSCAR examples shown below, the fifth line in the POSCAR format (starting to count from zero at the top of the file as customary in the Jinja language) is indeed the line containing the chemical symbols of the elements comprised in the material structure. The list of elements contained in the material is consequently assigned to the variable "element_lines".

### 6 - 10. Check for Presence of Aluminum in Material 

An "if/else" [conditional block of statements](../../workflows/templating/engine.md#conditionals) is then included in the remainder of the above template. This checks for the presence of "Al" within the list of elements extracted from the POSCAR file of the material under investigation. If a positive match is encountered, then the variable "encut" for the material simulation is correspondingly set to the higher value of 600 eV, otherwise in the contrary case it is set to a lower 450 eV. 

### 11. Print Encut Variable Result

We conclude this first templating example by printing out the value of "encut" identified in the preceding step, through the use of the double curly braces notation for printing the value of variables in the Jinja syntax.

### Example Outputs

#### Negative Match

Let us first assume that the POSCAR file under consideration consists in the following crystal structure data.

```
Ga4 Sb4
1.0
6.219063 0.000000 0.000000
0.000000 6.219063 0.000000
0.000000 0.000000 6.219063
Ga Sb
4 4
direct
0.000000 0.000000 0.000000 Ga
0.000000 0.500000 0.500000 Ga
0.500000 0.000000 0.500000 Ga
0.500000 0.500000 0.000000 Ga
0.250000 0.250000 0.750000 Sb
0.250000 0.750000 0.250000 Sb
0.750000 0.250000 0.250000 Sb
0.750000 0.750000 0.750000 Sb
```

Hence, the output of the above template at the moment of rendering would in this case be `encut =450`, since no Aluminum is present in this particular material structure.

#### Positive Match

If, on the other hand, we consider the following alternative crystal structure definition, also expressed in a POSCAR format.

```
mp-661
1.0
   3.128588000	   0.000000000	   0.000000000
  -1.564294000	   2.709436686	   0.000000000
   0.000000000	   0.000000000	   5.016955000
Al N
2 2
direct
   0.666667000    0.333333000    0.499287000 Al
   0.333333000    0.666667000    0.000000000 Al
   0.666667000    0.333333000    0.880713000 N
   0.333333000    0.666667000    0.380713000 N
```

Then the rendered output of the template would in this case consist in `encut =600`, since Aluminum is this time present within the crystal structure.

## Setting Magnetic Moments


## Links

[^1]: [Python Split Function Explanation, Website](https://www.pythonforbeginners.com/dictionary/python-split)
