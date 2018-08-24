# Header Menu Actions

At the top of the Workflow Designer interface, users can find a header menu. This page explains the actions that it allows for. 

# Name

The initial name of a newly-created workflow is "Empty Workflow". It is visible at the left-end of the header menu bar next to the workflows icon <i class="zmdi zmdi-dot-circle zmdi-hc-border"></i>. Instructions on how this name can be changed are provided [here](/general/actions/name.md). Immediately below this general name for the workflow under consideration, a list of the computational engines employed in the workflow displayed under the label "applications".  

# Description

The user can add a general description of the workflow's features and applications for reference purposes by clicking on the "information" button <i class="zmdi zmdi-info-outline zmdi-hc-border"></i> towards the right-end of the header menu. A text dialog will open, where the workflow description can be entered in the Markdown scripting language according to the guidelines presented [here](../general/actions/metadata.md). 

Please click on `OK` once all required text has been entered and needs to be saved, or `Cancel` to revert.

# Saving the workflow

The workflow under consideration can be saved at any time following the changes made to it. Until this is done the changes are NOT permanently saved so refreshing the page will remove them, for example. 

The Save operation can be accomplished via either of two alternative buttons, both located on the right-hand side of the header menu. The user can either click directly on the button labelled with a tick-mark <i class="zmdi zmdi-check zmdi-hc-border"></i> to perform a direct save, and be subsequently re-directed to the workflows collection page, or alternatively the same action can be executed *without the redirect* via the `Save` option located under the neighbouring drop-down menu button labelled with three vertical dots.

# Inserting Add-ons

The header menu bar of the Workflows Designer interface finally gives the user the possibility to include a **Add-ons**, in the form of an additional subworkflow. 

For example, when considering a Density Functional Theory calculations, in order to perform an initial variable-cell relaxation on the current material, the user can choose via the `Relaxation` option under the three-dotted drop-down menu icon. This particular type of Modifier is comprehensively reviewed in its [corresponding documentation page](/workflows/addons/structural-relaxation.md).

The location of this drop-down menu is highlighted below:

<img src="/images/modifier-menu.png/" >

# Metadata

The user can furthermore add descriptive `tags` to the workflow under consideration, following the general tag philosophy presented [here](../general/actions/metadata.md). In order to add tags, first the Workflows Designer page has to be scrolled down to the bottom, where the user will see a text line field labelled "Tags:".

!!!warning "Tags are not part of the Header"
    Although we include its explanation in this page, the "Tags" section is not part of the header. The Workflows Designer page has to be scrolled down to the bottom to view it.
