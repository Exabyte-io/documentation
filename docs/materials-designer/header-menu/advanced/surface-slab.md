# Surface / slab

Single layer materials, sometimes referred to as 2D Materials, are crystalline materials consisting of a single layer (or surface) of atoms [[1](#links)]. Since the original discovery and isolation of the first 2D material, graphene (a single layer of graphite) in 2004, a large amount of research has been directed at isolating other 2D materials. This research effort was primarily motivated by their inherently interesting characteristics, and their potentially broad range of technological applications such as in photovoltaics, semiconductors, electrodes and water purification.

Since the discovery of graphene, about 700 2D materials have been predicted to be stable and many remain to be synthesized in the laboratory. The global market for 2D materials is expected to reach US$390 million by 2025, mostly thanks to the continued evolution and development of the technological applications of graphene within a widespread market ranging from semiconductors and electronics, to batteries and composites.

Crystal surfaces can furthermore be stacked on top of each other to form slabs which, despite being fully three-dimensional structures, maintain a vertical dimension which is typically smaller in size than the axes defining their basal plane.  

# Theoretical background
 
Crystal surfaces are primarily defined in terms of their Miller indices [[2](#links)], as conventionally done when describing planar features in crystals. A short review of Miller index notation for labelling crystal planes is offered in the expandable section below for the sake of completeness, and it is to be referred to at the reader's discretion based on his previous knowledge of crystallographic principles. 

<details>
  <summary>
    Expand to view ...
  </summary>


Miller indices are essentially a set of three integer numbers, conventionally expressed in the form $(hkl)$, which constitute a convenient shorthand notation to refer to an entire family of lattice planes in a crystal. In particular, a generic set of Miller indices $(hkl)$ denotes the family of planes orthogonal to $h\mathbf {b_{1}} +k\mathbf {b_{2}} +\ell \mathbf {b_{3}}$, where $\mathbf {b_{i}}$ are the basis of the *reciprocal* lattice vectors. However, it is important to caution that the so-defined plane is not always orthogonal to the linear combination of *direct* lattice vectors $h\mathbf {a_{1}} +k\mathbf {a_{2}} +\ell \mathbf {a_{3}}$, since the reciprocal lattice vectors need not be mutually orthogonal.  

It is furthermore normally convenient to divide the Miller indices by their minimum common denominator. 

Some examples of planes with different Miller index labels in cubic crystals are depicted below for reference and illustration purposes. Since the reciprocal lattice vectors are indeed mutually orthogonal in this particular cubic case, the $(hkl)$ planes can effectively be taken to be always perpendicular to the $(hkl)$ direction in the crystal relative to the conventional Cartesian coordinate system.

<img src="/images/Miller_Indices_Felix_Kling.png"/>

</details>


# Accessing the Surface / slab generator

By clicking on the `Surface / slab` option in the `Advanced` menu, the surface/slab generator built into the Materials Designer interface can be accessed. The user should expect to encounter the following dialog, where all numerical text fields can be edited manually:

<img src="/images/surface-slab-generator.png"/>

# Constructing surfaces and slabs 

## Miller indices $(hkl)$

Surfaces and slabs (layers of surfaces stacked on top of each other) can easily be designed and generated upon entering their relevant information in the above dialog. In particular, the user has to start by entering the Miller indices $(hkl)$ of the corresponding crystal plane. This information will section the selected crystal structure across the desired plane. 

## Thickness in number of layers

If a simple 2D crystalline surface is all that needs to be generated, then the thickness of the surface (in terms of number of atomic layers stacked on top of each other) can be kept to one. Otherwise, any desired "thickness in layers" greater than unity can be entered, and the resulting structure will no longer be a 2D surface but a slab with a finite (but usually relatively small) thickness.  

## Vacuum ratio

The vacuum ratio defines the portion of the vertical size (along the z direction conventionally) of the unit cell in a slab which is occupied by vacuum, as opposed to being occupied by layers composed of matter (atoms). It is measured as a fraction (from zero to one) of the total height of the corresponding unit cell.  

## Supercell dimensions in x and y

As we mentioned in the previous paragraph, the vertical dimension of a slab or surface structure is normally taken to lie along the z direction. This leaves the basal plane of such structures to lie on the x-y plane of the overall Cartesian coordinate system. 
 
The number of times the crystal unit cell is repeated in both of these x and y basal dimensions is defined in the last two "Supercell dimension" fields of the surface / slab generator dialog. Setting these two numbers to be significantly larger than the aforementioned "thickness in layers" parameter allows for the construction of slabs which are wider in terms of their surface area than they are thick, as it is typically the case with such structures.  

# Generating the surface / slab

Click on "Submit" at the bottom of the surface / slab generator dialog once all the above information has been entered, and the corresponding surface or slab structure will appear in the 3D graphical viewer of the Materials Designer interface. 

# Animation

In the animation below, we generate a crystalline slab of pure silicon along the (001) plane, composed of three layers of atoms in terms of thickness, and with a 10x10 supercell constituting its base. The final view of the crystal structure is finally adjusted with the help of the interactive features of the 3D viewer, described [in this page](../../viewer-intro.md), to better inspect the overall appearance of the slab with regards to its size, thickness and vacuum ratio relative to the enclosing unit cell. 

<img data-gifffer="/images/CreateSurfaceSlab.gif" />


# Structure Metadata

Once a surface or slab has been generated, and saved into the account-owned collection of materials following the instructions outlined [in this page](../input-output/save.md), the user can retrieve information about the settings that were used to generate the surface or slab with Materials Designer in the form of "metadata". Simply click on the corresponding entry in the materials collection, and look for lines towards the bottom of the page starting with:

<details>
  <summary>
     `"metadata":{`
  </summary>

```
"isSlab":true
"h":0
"k":0
"l":1
"thickness":3
"vacuumRatio":0.8
"vx":10
"vy":10
"bulkId":"KFpZWcCPMFW2egjau"
"bulkExabyteId":"e3nJ9g7tLaARSA25g"
}
```
</details>


By expanding this section, the user will be able to retrieve all the relevant metadata associated with the original generation of the surface / slab. Notice that this feature is exclusive to slabs and surfaces, since this metadata is only required for performing surface energy calculations.

# Links

1. [Wikipedia Two-dimensional materials, Website](https://en.wikipedia.org/wiki/Two-dimensional_materials)
2. [Wikipedia Miller Indices, Website](https://en.wikipedia.org/wiki/Miller_index)
