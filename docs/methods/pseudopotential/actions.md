# Pseudopotential Subtypes

For the moment, up to three distinct **subtypes** of pseudopotentials (in the context of the DFT theoretical model [[1](#links)]) are supported as part of the Subworkflow Editor, under the corresponding "Subtype" drop-down menu in the "Method" section of the "Overview" tab: 

- Ultra-Soft (US)
- Norm-Conserving (NC) 
- Projector-Augmented Wave (PAW) 

The particular choice of pseudopotential subtype is normally best left to the discretion of the user, depending on his own personal experience with testing the different types on each particular chemical composition of a crystal. However neophyte users with little previous experience in operating first-principles DFT codes will most likely find that the Ultra-Soft pseudopotentials generally constitute a reliable choice for most intent and purposes, whilst normally requiring the least computationally expensive input parameters for defining the precision of the calculation. 

# Default Pseudopotential Files

The subsection labelled "Pseudopotentials" inside the Method section allows the user to choose which particular pseudopotential file to implement as part of the current subworkflow computations. A default pseudopotential for the material under consideration (crystalline silicon by default, unless this original default material was changed by the user) is always included in any subworkflow that is to be applied to this material.

A comprehensive set of default pseudopotentials for most elements in the periodic table is already included and made available for user selection on the Subworkflow Editor interface. For the Quantum Espresso application, only the Ultra-Soft pseudopotential subtype can be selected as part of this default set for the moment, whereas for the VASP application many different flavors of PAW pseudopotentials are available. 

More pseudopotential files can be downloaded from the respective websites of these applications, and then uploaded directly to the Subworkflow Editor, in order to expand the default set. This can be achieved following the procedure outlined below.

# Uploading Custom Pseudopotential Files

By expanding the subsection labelled "Pseudopotentials" (with the help of the "plus' button <i class="zmdi zmdi-plus zmdi-hc-border"></i> to its left), and then clicking on the `Upload` button  <i class="zmdi zmdi-upload zmdi-hc-border"></i> on the right-hand side, the user can moreover upload a custom or downloaded pseudopotential file of his choice directly from his local hard drive to the Subworkflow Editor. First however, all the necessary categorization information about this new pseudopotential being uploaded have to be specified from the list of drop-down menus in the resulting dialog. An example of this dialog's appearance is shown below:

 <img src="/images/pp-upload.png"/>
 
Once the desired file has been uploaded to the Subworkflow Editor via the `Choose File` option at the bottom of this dialog, the `Save` button can then be pressed to save this file to the account-owned collection of pseudopotentials.

# Filtering the list of available Pseudopotentials

In this expanded "Pseudopotentials" subsection, the user will furthermore see a first editable "filtering" text bar where text or comma-separated regular expressions (such as the examples shown on the bar itself) may be typed to search and filter pseudopotentials out of the default or user-uploaded sets. 

The resulting filtered list of available pseudopotentials will then become visible by clicking on the other text bar just below this filtering bar, and next to the current material's chemical symbol. Any pseudopotential item out of this filtered list can be clicked upon for selection. If no match is found, the default pseudopotential for the particular element under consideration will be employed.

## Regular Expressions

A general review on the syntax employed by regular expressions for performing general searches can be found in Ref. [[2](#links)].

Otherwise, the use of regular expressions is best illustrated by way of a specific example. Consider the following regular expression for searching for a particular VASP pseudopotential:

```
(?=[5].[4])(?=.*/GW/)(?!.*/AE/)
```

This expression first searches for pseudopotentials released under version 5.4 of VASP. It then searches for all pseudopotential files of type "GW", and therefore included in the corresponding GW folder, but at the same time excludes those of type "AE" (all-electron). 

This particular regular expression operation applied to the available set of VASP pseudopotentials is demonstrated in the animation below:

<img data-gifffer="/images/regular-expression.gif" />
 
# Links

1. [Wikipedia Pseudopotential, Website](https://en.wikipedia.org/wiki/Pseudopotential)
2. [Wikipedia Regular expression, Website](https://en.wikipedia.org/wiki/Regular_expression)

