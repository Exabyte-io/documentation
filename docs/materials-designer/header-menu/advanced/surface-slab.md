# Surfaces / Slabs

Surfaces and Slabs are widely used crystallographic concepts. A general theoretical background is offered in the expandable section below for the readers unfamiliar with the topic. The rest of this documentation page explains how the surface/slab generation is implemented in the Materials Designer interface.

# Theoretical background
 
<details>
  <summary>
    Expand to view ...
  </summary>

## Miller indices

Crystal surfaces are defined in terms of their Miller indices [[1](#links)]. Miller indices are a set of three integer numbers, conventionally expressed in the form $(hkl)$, which constitutes a convenient shorthand notation to refer to an entire family of lattice planes in a crystal. In particular, a generic set of Miller indices $(hkl)$ denotes the family of planes orthogonal to $h\mathbf {b_{1}} +k\mathbf {b_{2}} +\ell \mathbf {b_{3}}$, where $\mathbf {b_{i}}$ are the basis of the *reciprocal* lattice vectors. However, it is important to caution that the so-defined plane is not always orthogonal to the linear combination of *direct* lattice vectors $h\mathbf {a_{1}} +k\mathbf {a_{2}} +\ell \mathbf {a_{3}}$, since the reciprocal lattice vectors need not be mutually orthogonal. It is therefore convenient to divide the Miller indices by their minimum common denominator. 

## Examples

Some examples of planes with different Miller index labels in cubic crystals are depicted below for reference and illustration purposes. Since the reciprocal lattice vectors are indeed mutually orthogonal in this particular cubic case, the $(hkl)$ planes can effectively be taken to be always perpendicular to the $(hkl)$ direction in the crystal relative to the conventional Cartesian coordinate system.

<img src="/images/Miller_Indices_Felix_Kling.png"/>

## Surface vs Slab

Surface represents an isolated terminal edge of an infinite crystal, whereas a Slab has a finite size and two edges. In practice, when dealing with periodic boundary conditions, a surface is modeled by a slab that is long enough for the electronic states on the edges to be completely independent of each other. 

</details>


# Accessing the Surface / Slab generator

By clicking on the `Surface / slab` option in the `Advanced` menu, the surface/slab generator can be accessed. The user should expect to encounter the following dialog:

<img src="/images/surface-slab-generator.png"/>

# Constructing surfaces and slabs 

## Miller indices $(hkl)$

Start by entering the Miller indices $(hkl)$ of the corresponding crystal plane. This information will section the selected crystal structure across the desired plane. 

## Thickness in number of layers

The desired "thickness in layers" greater than unity can be entered in this field.  

## Vacuum ratio

The vacuum ratio defines the portion of the vertical size (along the surface normal direction, "z") of the unit cell in a slab which is occupied by vacuum, as opposed to the maximum interatomic distance in this direction. The ration is thus measured as a fraction (from zero to one) of the total height of the corresponding unit cell.  

## Supercell dimensions in x and y

The vertical dimension of a slab or surface structure is normally taken to lie along the z direction. This leaves the basal plane of such structures to lie on the x-y plane of the Cartesian coordinate system. The number of times the crystal unit cell is repeated in both of these x and y basal dimensions is defined in the "Supercell dimension" fields.

> NOTE: only integer values are supported for the supercell dimensions at the moment

# Generating the surface / slab

Click "Submit" at the bottom of the generator dialog once all the above information has been entered, and the corresponding surface or slab structure will appear in the 3D graphical viewer of the Materials Designer interface.

# Animation

In the animation below, we generate a crystalline slab of pure silicon along the (001) plane, composed of three layers of atoms in terms of thickness, and with a 10x10 supercell constituting its base. The final view of the crystal structure is finally adjusted with the help of the interactive features of the 3D viewer, described [in this page](../../viewer-intro.md), to better inspect the overall appearance of the slab with regards to its size, thickness and vacuum ratio relative to the enclosing unit cell. 

<img data-gifffer="/images/CreateSurfaceSlab.gif" />


# Structural Metadata

Once a slab has been generated, and saved following the instructions outlined [in this page](../input-output/save.md), the user can retrieve the information about the settings that were used to generate the slab in the form of "metadata". Open the corresponding entry in the materials collection, and look for lines towards the bottom of the page starting with:

<details>
  <summary>
     `"metadata": ...`
  </summary> 

```json
{
    "isSlab": true,
    "h": 0,
    "k": 0,
    "l": 1,
    "thickness": 3,
    "vacuumRatio": 0.8,
    "vx": 10,
    "vy": 10,
    "bulkId": "KFpZWcCPMFW2egjau",
    "bulkExabyteId": "e3nJ9g7tLaARSA25g"
}
```
</details>


By expanding this section, the user will be able to retrieve all the relevant metadata associated with the original generation of the surface / slab. 

> NOTE: metadata is present for slabs / surfaces, and is used for performing the surface energy calculations.

<!-- TODO: add a link to a surface energy calculation tutorial above -->

# Links

1. [Wikipedia Miller Indices, Website](https://en.wikipedia.org/wiki/Miller_index)
