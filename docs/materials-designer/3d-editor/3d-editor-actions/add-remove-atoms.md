## Inject / Delete Atoms

Instead of having to manually edit the total number of atoms in the crystal structure [basis editor](../source-editor/basis.md), it is possible to place or delete individual atoms at desired locations within the crystal structure directly in the graphical viewer. Alternatively, the functionality can be toggled by `I` key.

### Delete

Hover over an atom to see it highlighted. Righ-click on it to delete. The text of the crystal basis will adjust accordingly.

### Inject

Right click inside the unit cell will inject an atom at the cursor position. We assign the default offset from the view such that the atom is created inside the unit cell. This assumes the default view position and can, however, be affected by zoom, so this features should be used with caution.
 
<img data-gifffer="/images/materials-designer/ViewerEditInject.gif" />
