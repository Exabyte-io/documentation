# Unit Editor

The unit editor for each elementary unit computation comprised in a parent subworkflow can be accessed by clicking on the corresponding unit box from within the units flowchart at the bottom of the Subworkflow Editor interface, first introduced [here](subworkflow-editor/units-flowchart.md). Once this is done, the user will be greeted with the various settings sections contained in the Unit Editor interface, as in the following example:

![](/images/unit-editor.png)

The first line at the top of the interface, labelled with the general logo for elementary units <i class="zmdi zmdi-circle-o zmdi-hc-border"></i>, offers a reminder of the unit's name within the units flowchart, or "pw_scf" in the above example in reference to its implementation of a ground-state  energy calculation in DFT performed with the "pw" code, which is part of the Quantum Espresso distribution (pw_scf specifically stands for Plane-Wave Self-Consistent Field). This first line also contains a reminder of the unit's type (execution unit in the above example), and of the identification label for the overall units flowchart (flowchartId). 

Each distinct section within the overall Unit Editor interface highlighted in the image above will now be reviewed separately:

# The "Application" section

Similarly to the "Application" settings section in the [Overview tab](subworkflow-editor/overview.md) of the parent Subworkflow Editor interface, this section reviews the computational engine (otherwise known as application) that is to be employed in the current unit calculation, and in which version. 

Normally these two settings cannot be changed by the user within the Unit Editor interface, due to them being set at the general parent subworkflow level. What can be changed inside this "Application" section of the Unit Editor is the specific component executable of the simulation engine that is to be employed as part of the current unit calculation, under the corresponding "Executable" drop-down menu.

## Examples with Quantum Espresso

For example, the Quantum Espresso DFT simulation package (contrary to VASP) breaks its operations into a relatively large number of distinct executables, as explained in its [dedicated documentation page](/applications/quantum-espresso.md). The "pw.x" executable in Quantum Espresso is the most commonly encountered one, and is used primarily for performing general total energy self-consistent calculations. This said, many other executables distributed as part of the Quantum Espresso package can be selected from the "Executable" drop-down menu, such as the "ph.x" code which is at the core of phonon linear response calculations through the Density Functional Perturbation Theory formalism, using the data previously produced by pw.x.    

For each executable object, several different calculation "Flavors" can in turn be chosen by the user under the corresponding drop-down menu. For example, many different types of computations can be performed within the context of the pw.x executable itself, such as [variable-cell relaxation calculations](/workflows/addons/structural-relaxation.md) via the "pw_vc-relax" flavor setting, or electronic band structure calculations with "pw_bands".

# The "Properties" section

The "Properties" settings section of the Unit Editor interface is presented in a way which is exactly 





