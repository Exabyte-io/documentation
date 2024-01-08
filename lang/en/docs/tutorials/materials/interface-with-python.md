# Create an Interface with Python Transformation

In this tutorial, you will learn how to create an interface between two materials using the Python Transformation feature. Specifically, we will explore the creation of an interface between Graphene and Ni(111).

## Open Materials Designer

We start with [opening](../../entities-general/actions/create.md) an instance of the [Materials Designer Interface](../../materials-designer/overview.md) for creating and designing new [Materials structures](../../materials/overview.md) on our platform.

## Import Materials from Standata

In order to use Graphene and Ni, the user should first [import](../../materials-designer/header-menu/input-output/import.md) sample crystalline structures of the two respective materials into the current Materials Designer session, from the account-owned [collection](../../accounts/collections.md) of materials.

In this example, we will import Graphene and Ni from Standata.

Open the 'Import from Standata' dialog by going to `Input/Output` > `Import from Standata`.

- Select 'Graphene' and 'Ni' from the materials list.
- Click 'Submit' to import these materials into the Materials Designer session.

Default Material Silicon should be removed from the session.

## Use Python Transformation Dialog

Navigate to `Advanced` > `Python Transformation` from the main interface.

- Choose the transformation titled “Place a 2D materials Layer on a Surface”.
- Ensure 'Ni' is set as the substrate and 'Graphene' as the layer within the transformation settings.

In the Python code area:

- Set the substrate index and layer index corresponding to the Selected Materials. In this example, the substrate (Ni) should be at index 0 and the layer (Graphene) at index 1.
- Customize the **`SETTINGS`** for your specific use case, including:
    - Miller indices for the substrate and layer, the default value is (1,1,1) for substrate and (0,0,1) for 2D layer.
    - Vacuum space and number of layers, we can leave it at default values.
    - The distance between the substrate and the layer in Angstroms.
    - Superlattice matrices which should be precalculated for a good lattice match. For Graphene on Ni(111) [[1,1], [1,1]] already provides a good match.
    - Flag **`scale_layer_to_fit`** scales 2D layer superlattice and basis to fit the superlattice of substrate. This is useful when the layer is not a perfect match to the substrate. In this example, we will leave it at default value of `False`. 

- Click `Run All` to process the transformation.
- The strain matrix will appear in the output, providing insight into the lattice deformation.
- `Output Materials` will update with the newly created structure.
- Review the resulting strain matrix, if satisfied, submit the form to add the interface to your materials collection.

## **Key Considerations**

- The user is responsible for calculating the appropriate superlattice matrices to ensure realistic interfaces.
- Excessive straining during the scaling of the layer can result in unrealistic deformations, so use **`scale_layer_to_fit`** cautiously.
- Verify the final structure using the Orthographic camera in the 3D Viewer to ensure proper alignment and centrality of the layer over the substrate.
