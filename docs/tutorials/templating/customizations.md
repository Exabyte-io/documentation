# Tutorial: Custom Input Script Templates

We provide in the present tutorial some examples on how [templates](../../workflows/templating/overview.md), for generating simulation input scripts, can be written and customized by the user using the [Jinja syntax and template engine](../../workflows/templating/engine.md) implemented on our platform.

Templates and their respective Contexts can be entered under [Workflow Designer](../../workflow-designer/overview.md), as introduced [here](../../workflows/templating/ui.md).

## Example: Setting Input Parameters for VASP

The code below automatically sets the value of the "ENCUT" variable to higher values for materials that contain Aluminum within their structures than for those than don't. In particular, ENCUT = 600 eV if Aluminium is present, or ENCUT = 450 eV otherwise. This variable is typically found in [VASP](../../software-directory/modeling/vasp.md) input scripts, for defining the plane-wave cutoff energy characterizing the precision of the [DFT computation](../../models/dft/parameters.md) to be executed on the material structure under investigation.                   

```jinja2
{% spaceless %}
{% set high_cutoff_element = "Al" %}
{% set poscar_string = input.POSCAR|e("js") %}
{% set atoms = poscar_string.split('direct')[0] %}
{% set lines = atoms.split("\u000A") %}
{% set element_lines = lines[5] %}
{% if element_lines.includes(high_cutoff_element) %}
{% set ENCUT = 600 %}
{% else %}
{% set ENCUT = 450 %}
{% endif %}
ENCUT ={{ ENCUT }}
{% endspaceless %}
```

Each line number in the above block of statements is described in what follows.

### 1. Spaceless Rendering

The initial "spaceless" statement ensures that the template output is rendered with no extra white spaces or empty lines added to it. 

### 2. Set Element Requiring Higher Cutoff Parameter (Aluminum)

We begin the logic of our template by defining the element that needs a high plane-wave cutoff to be "Al" for Aluminum, using the [set statement](../../workflows/templating/engine.md#variables-assignment). 

### 3. Read POSCAR File Contents

We then read the POSCAR input file for [VASP](../../software-directory/modeling/vasp.md), containing the numerical data defining the crystal structure, and assign the text contents of this file to the variable "poscar_string". Examples of POSCAR files are included at the end of this section.

### 4 - 6. Extract Elements Contained in Material

We then identify the lines within the POSCAR file containing the element chemical symbols, by using the "split" function for breaking up the file text contents at every occurrence of the argument passed to this function (the functioning and format of this split function is analogous to its Python counterpart [^1]). 

We first break the lines at the mention of the "direct" string, and take all the preceding content. We then split this content at every new line (denoted by the newline unicode character "\u000A"). As can be seen from the POSCAR examples shown below, the fifth line in the POSCAR format (starting to count from zero at the top of the file as customary in the Jinja language) is indeed the line containing the chemical symbols of the elements comprised in the material structure. The list of elements contained in the material is consequently assigned to the variable "element_lines".

### 7 - 11. Check for Presence of Aluminum in Material 

An "if/else" [conditional block of statements](../../workflows/templating/engine.md#conditionals) is then included in the remainder of the above template. This checks for the presence of "Al" within the list of elements extracted from the POSCAR file of the material under investigation. If a positive match is encountered, then the variable "ENCUT" for the material simulation is correspondingly set to the higher value of 600 eV, otherwise in the contrary case it is set to a lower 450 eV. 

### 12. Print Encut Variable Result

We conclude this first templating example by printing out the value of "ENCUT" identified in the preceding step, through the use of the double curly braces notation for printing the value of variables in the Jinja syntax.

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

Hence, the output of the above template at the moment of rendering would in this case be `ENCUT =450`, since no Aluminum is present in this particular material structure.

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

Then the rendered output of the template would in this case consist in `ENCUT =600`, since Aluminum is this time present within the crystal structure.

### Animation

In the animation below, we demonstrate how to switch between viewing the POSCAR structure file within the [Workflow Designer Interface](../../workflow-designer/unit-editor/input-templates.md), to viewing the same template as above for setting the "ENCUT" parameter, and finally its rendered output. The final result is `ENCUT =600` in this case since the material under investigation consists in the Aluminum-containing Al2N2 structure, shown in the above POSCAR file example.

<img data-gifffer="/images/tutorials/encut_template.gif">

## Example: Setting Magnetic Moments of Ferromagnetic Elements

The template code below automatically sets the value of magnetic moments for ferromagnetic elements present in a material structure to 5, and alternates the sign. Non-magnetic elements are instead set to zero. The rendered output of this template is suitable for a [VASP](../../software-directory/modeling/vasp.md) simulation.
                                          
```jinja2
MAGMOM ={% spaceless %}
{% set magnetic_elements = ['V', 'Cr', 'Mn', 'Fe', 'Co', 'Ni'] %}
{% set poscar_string = input.POSCAR|e("js") %}
{% set coordinates = poscar_string.split('direct')[1] %}
{% set sign = 1 %}
{% for line in coordinates.split("\u000A") %}
{% if loop.index0 > 0 %}
{% set trimmed_line =  line.trim() | replace(' +(?= )','','g') %}
{% set element = trimmed_line.split(' ')[3] %}
{% set is_magnetic = 0 %}
{% if magnetic_elements.includes(element) %}{{' '}}{{ 5 * sign }}
{% set sign = sign * -1 %}
{% set is_magnetic = 1 %}
{% endif magnetic_elements.includes(element) %}
{% if is_magnetic == 0 %}{{' '}}{{ 0 }}{% endif %}
{% endif loop.index0 %}
{% endfor line in coordinates.split("\u000A") %}
{% endspaceless %}
```                        

Each line number in the above block of statements is further explained in the ensuing sections.

### 1. Define MAGMOM Variable

We begin by defining the "MAGMOM" variable [^2], which will be included in the input script for a [VASP](../../software-directory/modeling/vasp.md) computation, within the "INCAR" input parameters file associated with this code.

### 2. Define Ferromagnetic Elements

In the second line, we [set](../../workflows/templating/engine.md#variables-assignment) the ferromagnetic elements, that need to have magnetic moments attributed to them, to be constituted of the following list: Vanadium (V), Chromium (Cr), Manganese (Mn), Iron (Fe), Cobalt (Co), and Nickel (Ni).

### 3. Read POSCAR File Contents

We then read the POSCAR input file used by [VASP](../../software-directory/modeling/vasp.md), containing the numerical data defining the crystal structure under investigation. We assign the text contents of this structure file to the variable "poscar_string". 

### 4. Read Atomic Coordinates

The lines containing the atomic coordinates and element chemical symbols within the POSCAR file are then read. This is done by splitting the file contents ensuing the "direct" line, which are then passed to the "coordinates" variable.

### 5-17. Set Magnetic Moments

The list of atomic coordinates defined previously is then looped over through the use of a [for loop](../../workflows/templating/engine.md#for-loops). 

The element symbol indicated at the end of each coordinate line is isolated in turn (line 8) and assigned to the variable "element", which is checked against the aforementioned list of ferromagnetic elements (line 10) through a [conditional statement](../../workflows/templating/engine.md#conditionals). If a positive match is detected, this element is assigned a magnetic moment value of +/- 5 in an alternating order (line 11). Otherwise, in case the element is found to be non-ferromagnetic, it is given a magnetic moment of zero (line 15).

### 18. Return Final Output

The final result of the "MAGMOM" variable is returned once the template is rendered, as a list of magnetic moment values.
                                           
### Example Output

Let us consider the following hypothetical example of a material structure (Cobalt Oxide), inserted under the POSCAR format.

```
Cobalt Oxide
1.0
8.151852 0.000000 0.000000
0.000000 8.151852 0.000000
0.000000 0.000000 8.151852
Co O
8 5
direct
0.000000 0.000000 0.000000 Co
0.750000 0.750000 0.250000 Co
0.500000 0.500000 0.000000 Co
0.000000 0.500000 0.500000 Co
0.250000 0.250000 0.250000 Co
0.500000 0.000000 0.500000 Co
0.250000 0.750000 0.750000 Co
0.750000 0.250000 0.750000 Co
0.111256 0.111256 0.388744 O
0.138744 0.861256 0.138744 O
0.888744 0.111256 0.611256 O
0.361256 0.861256 0.361256 O
0.611256 0.388744 0.611256 O
```

The rendered output of the above template for this particular case would be the following line, since Cobalt is ferromagnetic and Oxygen is not. This output line can be added to the "INCAR" input file for defining the [VASP](../../software-directory/modeling/vasp.md) computational parameters.

```
MAGMOM = 5 -5 5 -5 5 -5 5 -5 0 0 0 0 0
```

### Animation

In the following animation, we demonstrate how to switch between viewing the POSCAR structure file for Cobalt Oxide within [Workflow Designer](../../workflow-designer/unit-editor/input-templates.md), to viewing the template for adding the MAGMOM parameter to the INCAR input script, and finally its rendered output.

<img data-gifffer="/images/tutorials/magmom_template.gif">

## Links

[^1]: [Python Split Function Explanation, Website](https://www.pythonforbeginners.com/dictionary/python-split)

[^2]: [MAGMOM Tag in VASP, Official Documentation](https://cms.mpi.univie.ac.at/vasp/vasp/MAGMOM_tag.html)
