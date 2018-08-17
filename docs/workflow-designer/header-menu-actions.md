# Header Menu Actions

At the top of the Workflow Designer interface, users can find a header menu which provides the general functionality of the interface, such as changing the name of the workflow or saving it to the account-owned workflows collection. 

# Modifying the name of the workflow

The initial default name of a newly-created workflow is always "Empty Workflow", visible at the left-end of the header menu bar next to the general logo for workflows <i class="zmdi zmdi-dot-circle zmdi-hc-border"></i> used throughout the Exabyte platform. To change this name to a more memorable form, the user can edit it appropriately after clicking on it. 

Immediately below this general name for the workflow under consideration, a reminder of the computational engine being employed as part of the workflow is also displayed for convenience, under the label "applications". This engine defaults to the Quantum Espresso code (referenced simply as "espresso" in this notification).  

# Inserting a description of the workflow

The user can add a general description of the workflow's features and applications for reference purposes by clicking on the "information"  button <i class="zmdi zmdi-info-outline zmdi-hc-border"></i> towards the right-end of the header menu. A text dialog will open, where the workflow description can be entered in the Markdown scripting language [[1](#links)]. 

If no advanced text structuring or formatting needs to be performed as part of this workflow description, then plain text can also be entered and no previous knowledge of the Markdown syntax is therefore required. 

Please click on `OK` once all required text has been entered and needs to be saved, or `Cancel` to revert.

# Saving the workflow

The workflow under consideration can be saved at any time, following any changes made to it, to the account-owned collection of workflows. This save can be accomplished via either of two alternative buttons, both located on the right-hand side of the header menu.  The user can either click directly on the button labelled with a tick-mark <i class="zmdi zmdi-check zmdi-hc-border"></i> to perform a direct save and be re-directed to the workflows collection page, or alternatively the same action can be executed via the `Save` option located under the neighbouring button labelled with three vertical dots, which leaves the user in the current Workflow Designer page.

In either case, once the saving operation is completed, the current workflow becomes recoverable in the account-owned collection after the Workflow Designer interface is exited. 

# Perform a variable-cell structure relaxation

## What is a structural relaxation?

It is often desirable, before commencing any other calculation on a particular material structure of interest, to perform a "Variable-cell Relaxation" calculation as the starting initial step of a new workflow. This helps to ensure that the initial crystalline structure is fully relaxed and optimized (within some approximate tolerance criteria), and that accurate and realistic property calculations can therefore be subsequently executed on it throughout the rest of the workflow. 

The variable-cell relaxation calculation bears its name from the fact that the material's unit cell is allowed to undergo a series of sequential small structural changes in terms of its lattice parameters and atomic positions, in order to become fully optimized by the time the calculation is terminated according to the various criteria outlined below.  

## Equilibrium condition on the internal stress tensor

By optimized, it is generally meant that the internal stress tensor components of the material should match the externally applied pressure as closely as possible, which for a material under equilibrium conditions corresponds to the ambient atmospheric pressure (the default choice for a new workflow creation). This ambient pressure is in fact typically approximated as exactly zero in DFT ab-initio calculations, since it is normally considered to be negligible compared to the usual pressures of at least order kbar encountered in such calculations, necessary to perceptibly distort any solid-state crystal structure. 

## Equilibrium condition on the inter-atomic forces

Secondly, a relaxation calculation ensures that the inter-atomic forces within the crystal structure under consideration also become negligibly small. This aspect, together with the above-mentioned pressure criterion, contributes to stabilizing the overall structure as much as possible and to therefore minimize its potential energy.    

## Execution of the Variable-cell Relaxation calculation

The user can add such a variable-cell relaxation calculation as the first step in a newly-created workflow by clicking on the `Relaxation` option under the button labelled with three vertical dots located at the right-hand side of the header menu of the Workflow Designer interface. 

Performing such an initial relaxation at the beginning of any type of workflow is in general a recommended practice, since having a fully-optimized crystal structure as the starting point will ensure more reliable results throughout the course of the execution of the rest of the workflow tasks. The user is advised that not even the pre-defined crystal structures which can be imported directly from centralized databases, such as the [Materials Bank](../materials/bank.md) or the [Material Project](../materials/import.md) repositories reachable on the Exabyte platform, are always guaranteed to be fully pre-relaxed and pre-optimized.  

Once the Relaxation calculation has been selected and added to the beginning of the current workflow, a tick <i class="zmdi zmdi-check zmdi-hc-border"></i> will appear next to the previously-clicked `Relaxation` option to remind the user about this inclusion. The "Variable-cell Relaxation" calculation will furthermore be inserted as a subworkflow module at the start of the flowchart portraying the overall workflow on the left-hand sidebar of the Designer interface, as explained in its respective [documentation page](sidebar-items.md). 

# Links

1. [Markdown syntax summary, Website](https://daringfireball.net/projects/markdown/syntax)
