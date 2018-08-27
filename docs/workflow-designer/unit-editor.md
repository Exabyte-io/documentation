# Unit Editor

The unit editor for each elementary unit computation comprised in a parent subworkflow can be accessed by clicking on the corresponding unit box from within the units flowchart, which can be found at the bottom of the Subworkflow Editor interface and is first introduced [here](subworkflow-editor/units-flowchart.md). Once this is done, the user will be greeted with the various settings sections contained in the Unit Editor interface, as shown in the following example:

![](/images/unit-editor.png)

Each distinct section within the overall Unit Editor interface highlighted in the image above will now be reviewed separately throughout the remainder of this documentation page:

# Unit name

The first line at the top of the interface, labelled with the general logo for elementary units <i class="zmdi zmdi-circle-o zmdi-hc-border"></i>, offers a reminder of the unit's name within the general units flowchart, or "pw_scf" in the above example. This latter unit name is in reference to its implementation of a ground-state self-consistent energy calculation in DFT performed with the "pw" code, which is part of the Quantum ESPRESSO distribution (pw_scf specifically stands for Plane-Wave Self-Consistent Field). This unit name can be edited by the user following the item re-naming conventions outlined [here](/general/actions/name.md). 

This first line also contains a reminder of the unit's type (execution unit in the above example), and of the unique identification label of the unit within the overall units flowchart (the so-called flowchartId). 

# The "Application" section

Similarly to the "Application" settings section in the [Overview tab](subworkflow-editor/overview.md) of the parent Subworkflow Editor interface, this section reviews the computational engine (otherwise known as application) that is to be employed in the current unit calculation, and in which specific version and build. 

Normally these two settings cannot be changed by the user within the Unit Editor interface, due to them being set at the general parent subworkflow level. What can be changed inside this "Application" section of the Unit Editor is the specific component executable of the simulation engine that is to be employed as part of the current unit calculation, under the corresponding "Executable" drop-down menu.

## Examples with Quantum Espresso

For example, the Quantum Espresso DFT simulation package (contrary to VASP) breaks its operations into a relatively large number of distinct executables, as explained in its [dedicated documentation page](/applications/quantum-espresso.md). The "pw.x" executable in Quantum Espresso is the most commonly encountered one, and is used primarily for performing general total energy self-consistent calculations. This said, many other executables distributed as part of the Quantum Espresso package can be selected from the "Executable" drop-down menu, such as the "ph.x" code which is at the core of phonon linear response calculations through the Density Functional Perturbation Theory formalism, using the data previously produced by pw.x.    

For each executable object, several different calculation "Flavors" can in turn be chosen by the user under the corresponding drop-down menu. For example, many different types of computations can be performed within the context of the pw.x executable itself, such as [variable-cell relaxation calculations](/workflows/addons/structural-relaxation.md) via the "pw_vc-relax" flavor setting, or electronic band structure calculations with "pw_bands".

# The "Properties" and "Monitors" sections

The "Properties" and "Monitor" settings sections of the Unit Editor interface are presented in a way which is exactly analogous to the equivalent sections under the "Detailed View" tab of the parent Subworkflow Editor interface. The reader is therefore referred to the relevant parts of the "Detailed View" [documentation page](/workflow-designer/subworkflow-editor/detailed-view.md#'The "Properties" section'), and to [this other reference page](/materials/properties.md). The tables presented towards the end of this latter page, in particular, display firstly a complete list of physical properties that can be selected in the Unit Editor interface and then retrieved as part of the final output of the unit's computational tasks,  and secondly a list of quantities that can be monitored for correct convergence during the course of the execution of the unit's calculations. 

# The "Next" section

This section permits the user to view, under the corresponding "Next" drop-down menu, which other units are contained in the overall units flowchart sequence, besides the unit currently being consulted under the Unit Editor interface. Each time a unit is selected from this drop-down menu, its corresponding identification label gets displayed under the "FlowchartId" entry to the right of the same line. The default unit entry displayed in this "Next" drop-down menu is the unit that follows in the flowchart immediately after the one being currently inspected. 

# Unit input templates

The final section at the bottom of the Unit Editor interface is explained in detail in its own [dedicated documentation page](unit-editor/input-templates.md), due to the rather complex nature of the input script templates contained there.


