# Entity Explorer Interface

The Explorer Interface is composed of the following subcomponents: 

# Entity Items List

The  "Entity Items List" displays the contents of the corresponding [Account-owned entity collection](/accounts/collections.md), in a user-readable way. Moreover, it allows users to execute [actions](/entities-general/actions/overview.md) on multiple entities at once. 

This component is illustrated below for the case of Materials.

<img src="/images/materials-list.png" >


# Sub-header

The image below shows the location of the sub-header, also present at the bottom of the interface.

<img src="/images/sub-header.png"/>


## Columns Selector 

The user may customize which entity properties to display under each column. This is done through the  drop-down button labelled with three horizontal dots.

The table of displayed properties can be scrolled horizontally, by toggling the button labelled with a pair of triangular brackets.  

The image below shows the location of both buttons within the sub-header. Viewable materials properties are also shown under the drop-down menu, as an example.

<img src="/images/properties-dropdown.png"/>

## Toggle Reactive Updates

By default, the information displayed under the Entity Items List is updated automatically. We refer to this feature as "reactive" updates. Constant updating can occasionally cause the platform interface to slow down and become un-responsive, such as may be the case when a large number of Jobs is being executed simultaneously. The user may therefore wish to "pause" the reactive updates, and this can be accomplished through the "Toggle Reactive Updates" button <i class="zmdi zmdi-pause-circle-outline zmdi-hc-border"></i>.

Once paused, this button appears under the "play" label <i class="zmdi zmdi-play-circle zmdi-hc-border"></i>. Reactive updates can be resumed by clicking it a second time. Alternatively, updating can be triggered manually through the neighboring "Trigger Update" button <i class="zmdi zmdi-rotate-left zmdi-hc-border"></i>.

## Pagination of Entity Items List

Finally, selection and pagination of the entity items list can be customized.

Firstly, the number of entity items to be shown under each page, out of their total number, can be selected. This is done from the drop-down menu emphasized in the image below, under the section labelled "Results per Page".

<img src="/images/number-items.png"/>

The above menu can also be used to navigate between the pages themselves, under the section labelled "Pages". If numerous pages are present, then only the ten closest to the one being currently viewed are shown.

Secondly, the left-hand checkbox allows all listed entity items to be selected simultaneously. Their total number is also displayed at all times.

# Action-related Components

## Actions Toolbar

The Actions Toolbar allows users to execute [actions](../actions/overview.md) on multiple selected Entities at once. Entities can be [selected](../actions/select.md) using the corresponding checkboxes to the left of each entry line. 

## Actions Dropdown

The actions Dropdown menu, accessible under the three-dotted button at the right-end of each entry line, allows one to execute the above-mentioned actions on that specific entry only. The set of allowed actions this time is filtered per each entry according to its [type](/entities-general/overview.md) and [permissions](/entities-general/permissions.md).

## Visuals

The location of both the actions toolbar and dropdown menus, within the Explorer interface, is clarified in the panels emphasized in the image below.

<img src="/images/workflow-actions-menus.png"/>

# Search Bar

Finally, a Search Bar  <i class="zmdi zmdi-search zmdi-hc-border"></i> is also present in the main header, as highlighted in the image below. Users can search through the items listed in the entity collection following [this procedure](../actions/search.md).

<img src="/images/search-bar-explorer.png"/>

## Advanced Search

Some entities offer the possibility to perform "Advanced" searches, such as in the case of [Materials](/entities-general/actions/advanced-search.md). The appearance of the search bar might as a result expand below the header, as shown in the highlighted portion below.

<img src="/images/search-advanced-explorer.png"/>

# Links

Documentation pages presenting entity-specific aspects of the Explorer Interface are available for [Materials](/materials/ui/explorer.md), [Workflows](/workflows/ui/explorer.md) and [Jobs](/jobs/ui/explorer.md) respectively.
