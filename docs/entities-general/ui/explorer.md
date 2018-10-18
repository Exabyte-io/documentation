# Entity Explorer Interface

The Explorer Interface is composed of the following subcomponents: 

# Entity Items List

The  "Entity Items List" component of the Explorer interface represents a list displaying the contents of the corresponding [Account-owned Entity Collections](/accounts/collections.md), in a user-readable way. This Entity Items List moreover allows users to execute actions on multiple Entities at once. 

This component is illustrated below for the example entity case of Materials:

<img src="/images/materials-list.png" >


# Sub-header

The image below shows the location of the sub-header within the Explorer Interface (the same sub-header is also present at the bottom of the interface):

<img src="/images/sub-header.png"/>


## Columns Selector 

The columns of the aforementioned Entity Items List can be customized through the  drop-down menu in the sub-header labelled with three horizontal dots. Once the menu is opened, the user may choose which entity properties to display under each column of the list by selecting the appropriate options.

Next to this menu button, the possibility to scroll the table of displayed properties horizontally is also offered, under the button labelled with a pair of triangular brackets which toggles such a horizontal scroll functionality.  

The image below shows the location of these two buttons within the sub-header. An example of Materials properties, which can be selected for viewing under the Items List, is also shown under the drop-down menu:

<img src="/images/properties-dropdown.png"/>

## Toggle Reactive Updates

By default, the information displayed under the Entity Items List is updated automatically and in real time, that is it updated in a "reactive" fashion. This constant updating can occasionally cause the platform interface to significantly slow down and become un-responsive, such as it may be the case when a large number of Jobs is being executed simultaneously. They user may therefore wish to "pause" the reactive updates, and this can be accomplished through the "Toggle Reactive Updates" button <i class="zmdi zmdi-pause-circle-outline zmdi-hc-border"></i> present in the sub-header.

Once paused, the reactive updates can be resumed by clicking on the "Toggle Reactive Updates" button a second time, which after pausing appears under the "play" label <i class="zmdi zmdi-play-circle zmdi-hc-border"></i>. Alternatively, the updating of the information contained in the Entity Items List can be triggered manually, following the pausing of reactive updates, through the neighboring "Trigger Update" button <i class="zmdi zmdi-rotate-left zmdi-hc-border"></i>.

## Pagination of Entity Items List

Finally, on the left-hand side of the sub-header, further selection and viewing functionality is offered with regards to the entity list items.

Firstly, the number of entity items to be shown under each page of the Entity Items List, out of their total number contained in the Account-owned Entity Collection, can be selected from the corresponding drop-down menu emphasized in the example below, under the section labelled "Results per Page":

<img src="/images/number-items.png"/>

The above drop-down menu can also be used to navigate between the Entity List pages themselves, under the section of the menu labelled "Pages". If numerous pages are present in the Entity List, then this section will only show the ten closest pages to the one being currently viewed.

Secondly, the checkbox on the very left allows all listed entity items to be selected simultaneously. The total number of currently selected entity items is displayed at all times to the right of the above-mentioned page drop-down.

# Action-related Components

## Actions Toolbar

The Actions Toolbar allows users to execute [actions](../actions/overview.md) on multiple selected Entities at once. Entities can be selected using the corresponding checkboxes to the left of each entry line. 

## Actions Dropdown

The actions Dropdown menu, accessible under the three-dotted button at the right-end of each entry line, allows one to execute the above-mentioned actions on that specific entry only. The set of allowed actions this time is filtered per each entry according to its type and permissions.

## Visuals

The location of both the toolbar and dropdown menus containing the action buttons, within the Explorer interface, is further clarified in the panels emphasized in the image below:

<img src="/images/workflow-actions-menus.png"/>

# Search Bar

Finally, a Search Bar  <i class="zmdi zmdi-search zmdi-hc-border"></i> is also present in the main header of the Explorer Interface, to the left of the Actions Toolbar as highlighted in the image below. This Search Bar allows the user to search through the items listed in the entity collection, which can be done following [this procedure](../actions/search.md).

<img src="/images/search-bar-explorer.png"/>

## Advanced Search

Some entities offer the possibility to perform "Advanced" type of searches, such as is the case for [Materials](/materials/actions/advanced-search.md). In this case, the appearance of this search bar might expand below the header of the Explorer Interface, such as shown in the highlighted portion below:

<img src="/images/search-advanced-explorer.png"/>

# Links

Documentation pages presenting the various entity-specific aspects of the Explorer Interface are available for [Materials](/materials/ui/explorer.md), [Workflows](/workflows/ui/explorer.md) and [Jobs](/jobs/ui/explorer.md) respectively.



