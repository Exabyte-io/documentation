# Units Flowchart

At the bottom of the  "Overview" tab page within the Subworkflow Editor interface, under the section titled "Units", the user can inspect the **units flowchart** offering a graphical representation of the subworkflow under consideration. Each unit included in this flowchart represents per se a distinct **elementary unit computation**, which can be mainly of **logical** or **executing** nature. The former category is further subdivided into **assignment**, **condition** and **assertion** elementary unit types. The general concept of unit, and all its various different types, is narrated further [in its dedicated page](../../workflows/data/units.md).

An example of elementary units flowchart at the bottom of an "Overview" tab, concerning a band structure calculation implemented with the Quantum Espresso DFT application, is depicted in the image below:  

<img src="/images/units-flowchart.png"/>

# Unit boxes in the flowchart

In the above image, the user can notice that each unit box has a number indicating its order within the overall flowchart sequence on its top-left corner. Moreover, the type of the unit is itself labelled on the bottom-left corner of each box (for example "E" for execution unit). At the top-right corner, an "X" button is offered to delete altogether the corresponding unit from the flowchart sequence. 

Each unit box is clearly labelled with the technical name of the elementary computation that it implements, placed next to the general logo for elementary units <i class="zmdi zmdi-circle-o zmdi-hc-border"></i>. For example, "pw_scf" is the label for a ground-state "scf" energy calculation in DFT performed with the "pw" code, which is part of the Quantum Espresso distribution. 

Finally, new elementary units can be added to this overall flowchart by clicking on the final empty unit box labelled with a "plus" sign <i class="zmdi zmdi-plus zmdi-hc-border"></i>. THe following dialog will open, offering the user the possibility to choose the type of elementary unit that needs to be added in the first drop-down menu, and in the lower drop-down menu whether to append it or prepend it to the currently selected unit in the flowchart:

<img src="/images/new-units.png"/>

# Opening the Unit Editor

Clicking on each unit box component of the flowchart allows the user to open the corresponding Unit Editor interface, and to inspect directly all the various input parameters and input script templates of the underlying unit elementary computation. The user is referred to [this part](../unit-editor.md) of the documentation for a detailed description of this Unit Editor interface.

# Workflows and Subworkflows intended as units

Even the more general subworkflows and overall workflows can themselves be considered to be types of units, albeit of a more complex nature than the aforementioned elementary units displayed in the units flowchart. In fact, a valid interpretation of the concept of subworkflow is to think of it as the smallest possible combination of elementary units. 

Elementary units can themselves be introduced as components in a flowchart of subworkflows, such as the one displayed on the [left-hand sidebar](../sidebar.md) of the Worflows Designer interface, although with some restrictions. In particular, a logical flowchart of subworkflows may contain all types of elementary units except for those of execution type. A sequence of general workflows can also be further combined together with elementary units, besides the subworkflow components themselves, but such elementary units can be of logical type only. 







 


