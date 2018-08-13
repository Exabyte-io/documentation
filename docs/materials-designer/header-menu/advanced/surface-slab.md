# Surface / slab

Single layer materials, sometimes referred to as 2D Materials, are crystalline materials consisting of a single layer (or surface) of atoms [[1](#links)]. Since the isolation of graphene, a single layer of graphite, in 2004, a large amount of research has been directed at isolating other 2D materials. This research effort was primarily motivated by their inherently interesting characteristics, and their potentially broad range of applications such as in photovoltaics, semiconductors, electrodes and water purification.

Since the discovery of the first 2D material, graphene, in 2004, about 700 2D materials have been predicted to be stable and many remain to be synthesized in the laboratory. The global market for 2D materials is expected to reach US$390 million by 2025, mostly thanks to the continued evolution and development of the technological applications of graphene within a widespread market ranging from semiconductors and electronics, to batteries and composites.

Crystal surfaces can furthermore be stacked on top of each other to form slabs which, despite being fully three-dimensional structures, maintain a vertical dimension which is typically smaller in size than the axes defining the basal plane.  

# How crystal surfaces can be defined with Miller indices
 
Crystal surfaces are primarily defined in terms of their Miller indices [[2](#links)], as conventionally done when describing planar features in crystals. A short review of Miller index notation for labelling crystal planes is offered in the remainder of this section of the documentation for the sake of completeness, and it is to be referred to at the reader's discretion based on his previous knowledge of crystallographic principles. 

Miller indices are essentially a set of three integer numbers, conventionally expressed in the form $(hkl)$, which constitute a convenient shorthand notation to refer to an entire family of lattice planes in a crystal. In particular, a generic set of Miller indices $(hkl)$ denotes the family of planes orthogonal to $h\mathbf {b_{1}} +k\mathbf {b_{2}} +\ell \mathbf {b_{3}}$, where $\mathbf {b_{i}}$ are the basis of the *reciprocal* lattice vectors. However, it is important to caution that the so-defined plane is not always orthogonal to the linear combination of *direct* lattice vectors $h\mathbf {a_{1}} +k\mathbf {a_{2}} +\ell \mathbf {a_{3}}$, since the reciprocal lattice vectors need not be mutually orthogonal.  

It is furthermore normally convenient to divide the Miller indices by their minimum common denominator. 

Some examples of planes with different Miller index labels in cubic crystals are depicted below for reference and illustration purposes:

<img src="/images/Miller_Indices_Felix_Kling.svg"/>

# Accessing the Surface / slab generator

By clicking on the `Surface / slab` option in the `Advanced` menu, the surface/slab generator built into the Materials Designer interface can be accessed. The user should expect to encounter the following dialog, where all numerical text fields can be edited manually:

<img src="/images/surface-slab-generator.png"/>

# Constructing surfaces and slabs 

## Miller indices $(hkl)$

Surfaces and slabs (layers of surfaces stacked on top of each other) can easily be designed and generated upon entering their relevant information in the above dialog. In particular, the user has to start by entering the Miller indices $(hkl)$ of the corresponding crystal plane, following the conventions outlined in the previous sections of this documentation page. This information will section the original crystal structure selected in the left-hand items list sidebar of the Materials Designer interface across the desired plane. 

## Thickness in number of layers

If a simple 2D crystalline surface is all that needs to be generated, then the thickness of the surface (in terms of number of atomic layers stacked on top of each other) can be kept to one. Otherwise, any desired "thickness in layers" greater than unity can be entered, and the resulting structure will no longer be a 2D surface but a slab with a finite (but usually relatively small) thickness.  

## Vacuum ratio

The vacuum ratio is defined as the ratio of the vertical size (along the z direction conventionally) of the unit cell in a slab which is occupied by vacuum, as opposed to being occupied by layers composed of matter (atoms). This essentially gives a measure of the separation distance between atomic layers in a slab, measured as a fraction (from zero to one) of the total height of the corresponding unit cell. Therefore the higher the value that this vacuum ratio is set to, the larger the resulting empty distance separating the atomic layers in the slab.  

## Supercell dimensions in x and y

As we mentioned in the previous paragraph, the vertical dimension of a slab or surface structure is normally taken to lie along the z direction. This leaves the basal plane of such structures to lie on the x-y plane of the overall Cartesian coordinate system. 
 
The number of times the crystal unit cell is repeated in both of these x and y basal dimensions is defined in the last two "Supercell dimension" fields of the surface / slab generator dialog. Setting these two numbers to be significantly larger than the aforementioned "thickness in layers" parameter allows for the construction of slabs which are much wider in terms of their surface area than they are thick, as it is typically the case with such structures.  

# Generating the surface / slab

Click on "Submit" at the bottom of the surface / slab generator dialog once all the above information has been entered, and the corresponding surface or slab structure will appear in the 3D graphical viewer of the Materials Designer interface. 

# Animation

# Links

1. [Wikipedia Two-dimensional materials, Website](https://en.wikipedia.org/wiki/Two-dimensional_materials)
2. [Wikipedia Miller Indices, Website](https://en.wikipedia.org/wiki/Miller_index)
