# Header Menu Actions

At the top of the Workflow Designer interface, users can find a header menu which provides the general functionality of the interface, such as changing the name of the workflow or saving it to the account-owned workflows collection. 

# Modifying the name of the workflow

The initial default name of a newly-created workflow is always "Empty Workflow", visible at the left-end of the header menu bar next to the general logo for workflows <i class="zmdi zmdi-dot-circle zmdi-hc-border"></i> used throughout the Exabyte platform. Instructions on how this name can be changed are found [in this page](../general/actions/name.md). 

Immediately below this general name for the workflow under consideration, a reminder of the computational engine being employed as part of the workflow is also displayed for convenience, under the label "applications". This engine defaults to the Quantum Espresso code (referenced simply as "espresso" in this notification).  

# Inserting descriptions of the workflow

## Markdown description

The user can add a general description of the workflow's features and applications for reference purposes by clicking on the "information"  button <i class="zmdi zmdi-info-outline zmdi-hc-border"></i> towards the right-end of the header menu. A text dialog will open, where the workflow description can be entered in the Markdown scripting language according to the guidelines presented [here](../general/actions/metadata.md). 

Please click on `OK` once all required text has been entered and needs to be saved, or `Cancel` to revert.

## Tags

The user can furthermore add descriptive tags to the workflow under consideration, following the general tag philosophy presented [here](../general/actions/metadata.md). In order to add tags, first the Workflows Designer page has to be scrolled down to the bottom, where the user will see a text line field labelled "Tags:". 

# Saving the workflow

The workflow under consideration can be saved at any time to the account-owned collection of workflows, following any changes made to it and any descriptive text and tags added to it. This save can be accomplished via either of two alternative buttons, both located on the right-hand side of the header menu.  The user can either click directly on the button labelled with a tick-mark <i class="zmdi zmdi-check zmdi-hc-border"></i> to perform a direct save, and be subsequently re-directed to the workflows collection page, or alternatively the same action can be executed via the `Save` option located under the neighbouring drop-down menu button labelled with three vertical dots, which leaves the user in the current Workflow Designer page.

In either case, once the saving operation is completed, the current workflow becomes recoverable in the account-owned collection after the Workflow Designer interface is exited. 

# Adding a Modifier

The header menu bar of the Workflows Designer interface finally gives the user the possibility to include a **Modifier**, in the form of a subworkflow calculation, inside the existing flowchart structure of the workflow under consideration. 

For example, to perform an initial variable-cell relaxation calculation on the current material sample using DFT techniques, the user can proceed via the `Relaxation` option under the three-dotted drop-down menu icon. This particular type of Modifier is comprehensively reviewed in its [dedicated documentation page](../workflows/modifiers/structural-relaxation.md).

The location of this drop-down menu under the three-dotted icon within the overall Workflow Designer interface is highlighted below:

<img src="/images/modifier-menu.png/" >


