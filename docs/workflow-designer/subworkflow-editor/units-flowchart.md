# Units Flowchart

At the bottom of the "Overview" tab page within the Subworkflow Editor interface, under the section titled "Units", the user can inspect the **units flowchart** offering a graphical representation of the subworkflow under consideration. Each unit included in this flowchart represents a distinct elementary unit computation, which can be mainly of purely logical (eg. "if" condition) or simulation (eg. ab-initio calculation) nature. The former category is further is narrated further [in its dedicated page](/workflows/data/units.md).

An example of elementary units flowchart at the bottom of an "Overview" tab, concerning a band structure calculation implemented with the Quantum Espresso DFT application, is depicted in the image below:  

<img src="/images/units-flowchart.png"/>

# Unit boxes in the flowchart

In the above image, the user can notice that each unit box has a number indicating its order within the overall flowchart sequence on its top-left corner. Moreover, the type of the unit is itself labelled on the bottom-left corner of each box (for example "E" for execution unit). At the top-right corner, an "X" button is offered to delete altogether the corresponding unit from the flowchart sequence.

# Currently selected unit

The currently selected unit is highlighted in color. Units can be selected by clicking on it. See "Opening the Unit Editor" below.

# Unit names

Each unit box is clearly labelled with the name of the elementary computation that it implements. For example, "pw_scf" is the name for a unit shown in the visual above. 

# Adding units

Finally, new elementary units can be added to this overall flowchart by clicking on the final empty unit box labelled with a "plus" sign <i class="zmdi zmdi-plus zmdi-hc-border"></i>. The following dialog will open, offering the user the possibility to choose the type of elementary unit that needs to be added in the first drop-down menu, and in the lower drop-down menu whether to append it or prepend it to the currently selected unit in the flowchart.

<img src="/images/new-units.png"/>

# Opening the Unit Editor

Clicking on each unit box component of the flowchart allows the user to open the corresponding Unit Editor interface, and to inspect directly all the various input parameters and input script templates of the underlying unit elementary computation. The user is referred to [this part](../unit-editor.md) of the documentation for a detailed description of this Unit Editor interface.
