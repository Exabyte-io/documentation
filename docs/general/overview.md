# Types of Entities

The user interface of the platform contains three main distinct classes of **Entities**, each recognizable by its unique symbol illustrated next to each entry in the list below:

| Entity    |  Icon      | Details        | 
| :-------- |:----------- |:------------- |
| Materials | <i class="zmdi zmdi-widgets"></i>    | Hold information about individual materials |
| Workflows | <i class="zmdi zmdi-dot-circle"></i> | Contain logical set of computational operations, applicable to multiple materials |
| Jobs      | <i class="zmdi zmdi-file"></i> | Represent computational tasks on a particular material-workflow combination to produce the corresponding properties and output files as results |

Each one of the above has a dedicated tab within the user interface, as depicted in the image below:

<img src="/images/entity-classes.png" > 

# Common actions

Entities share a number of equivalent attributes and actions in the user interface. Numerous simple actions, such as changing the item's name or adding descriptive metadata text to it, are performed in the same manner. Click on the links below to access the documentation pages associated with each corresponding type of action:

## [Modify Name](actions/name.md)

The name of each entity can be changed according to [these instructions](actions/name.md).

## [Edit Metadata](actions/metadata.md)

Each entity can be adorned with descriptive metadata, in the form of text, tags and other formats, for ease of referencing and retrieval when performing general searches. We explain how to add such metadata [here](actions/metadata.md).

## [Set Default](actions/set-default.md)

In each account-owned collection, any entry can be assigned the "Default" status as described [here](actions/set-default.md).

## [Delete](actions/delete.md)

The user can delete an Entity by following the procedure outlined [here](actions/delete.md).

## [Clone / Copy](actions/clone.md)

Each Entity can also be cloned or copied following [these instructions](actions/clone.md).

## [Open](actions/open-edit.md)

Opening an entry corresponding to a particular Entity in a the list in order to edit its content can be achieved [as follows](actions/open-edit.md).

## [Search](actions/search.md)

The user can perform general searches to retrieve particular Entities of interest through [this procedure](actions/search.md).

<hr>

# Common Interface Components

There are interface components, and some of their respective sub-components, which are common to all entity types, and these include the following: 

## 1. Designer

The Designer component allows user to Edit or "Design" new Entities. Its sub-components may include "Header Menu", "Items List Sidebar", and "Source Editor". In the case of Materials for example, their Designer interface has the following general appearance, where the instances of the above interface sub-components have been labelled correspondingly:

<img src="/images/materials-designer-initial.png" >

## 2. Explorer

The Explorer (or Entity List) component represents a list or Table and allows users to view and execute actions on multiple Entities at once. This interface component is illustrated below (named "General Items List") for the example entity case of Materials:

<img src="/images/materials-list.png" >

### Actions Toolbar

Actions Toolbar allows users to execute actions on multiple Entities at once. Entities can be selected using the corresponding checkboxes on each entry line.

### Actions Dropdown

The actions Dropdown allows one to execute the actions on a specific entry. The set of allowed actions is filtered per each entry according to its type and permissions.

### Visuals

The location of both the toolbar and dropdown menus containing the action buttons within the Explorer interface is further clarified in the panels emphasized in the image below:

<img src="/images/workflow-actions-menus.png"/>



