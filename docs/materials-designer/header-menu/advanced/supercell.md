# Supercells

A material has a crystal structure associated with it and the latter is described by a unit cell. There are an infinite number of unit cells U with different shapes and sizes which can describe the same crystal. The supercell S of unit cell U is defined as a cell which describes the same crystal, but has larger volume than cell U [[1](#links)].

Some examples of different supercells for the same underlying 2D cubic crystal are shown in the figure below. The relatively large size of such supercells has to be compared to the smaller surface area of the most basic unit cell of this crystal containing just one lattice point, two examples of which are shown towards the centre of the figure and at the top-left corner. Both diagonal and non-diagonal supercells are included in this picture to reflect the general scope of the supercell definition.

<img src="/images/2d_supercell_example.svg"/>

# Why are supercells useful?

There are many instances where the construction of supercells allows useful properties of the crystal to be ascertained, which could not otherwise be determined by looking just at the initial cell.

In particular, there are many instances of methods in computational materials science for determining crystal structure properties which rely on small perturbations of supercell structures away from their original equilibrium configurations. For example, during phonon calculations by the small displacement method, phonon frequencies in crystals are calculated using finite force values computed on slightly displaced atoms in a supercell of the original structure.
 
Another case for appreciating the usefulness of supercells in solid-state physics is the way the conventional cells of body-centered (bcc) or face-centered (fcc) cubic crystals, containing two atoms and four atoms respectively, reflect much more intuitively the overall symmetry of such crystals, especially when compared to the un-symmetric trapezoidal appearance of their basic one-atom primitive unit cells. The figure below illustrates the starkness of such contrast for the example of an fcc lattice. In this image, the volume marked in red represents the oddly-shaped primitive unit cell, whereas the over-arching cubic supercell framework on the other hand exhibits the full face-centred cubic symmetry from which the corresponding crystal structure gets its name:

<img src="/images/TGa4T.png"/>

Similarly to the above examples of fcc and bcc lattices, there are in fact many other instances where supercells afford for a more inherent visualization of the long-range symmetric order of crystal structures. 

Finally, supercells are also commonly used in computational models of crystal defects, in order to allow for the use of periodic boundary conditions.

# How are supercells defined?

The basis vectors of unit cell U $({\vec {a}},{\vec {b}},{\vec {c}})$  can be transformed to basis vectors of supercell S $({\vec {a}}',{\vec {b}}',{\vec {c}}')$ by way of the following linear transformation:

$$
{\displaystyle {\begin{pmatrix}{\vec {a}}'&{\vec {b}}'&{\vec {c}}'\\\end{pmatrix}}={\begin{pmatrix}{\vec {a}}&{\vec {b}}&{\vec {c}}\\\end{pmatrix}}{\hat {P}}={\begin{pmatrix}{\vec {a}}&{\vec {b}}&{\vec {c}}\\\end{pmatrix}}{\begin{pmatrix}P_{11}&P_{12}&P_{13}\\P_{21}&P_{22}&P_{23}\\P_{31}&P_{32}&P_{33}\\\end{pmatrix}}} 
$$

where ${\hat {P}}$ is the corresponding linear transformation matrix. All items $P_{ij}$ should be integer numbers and $\det({\hat {P}})>1$ (with $\det({\hat {P}})=1$ the transformation preserves the volume of the original unit cell). For example, the matrix

$$
{\displaystyle P_{P\rightarrow I}={\begin{pmatrix}0&1&1\\1&0&1\\1&1&0\\\end{pmatrix}}}
$$

transforms the primitive cell of a body-centered cubic lattice to its fully-symmetric conventional unit cell. Another particular case of the transformation is a diagonal form $P_{i\neq j}=0$ of the matrix. This type of transformations is referred to as diagonal supercell expansion, and can be interpreted as a simple repetition of the initial cell over its crystallographic axes.

# Generating Supercells

Click on the `Supercell` option in the `Advanced` menu. The "Generate supercell" overlay highlighted in the image below will allow you to set parameters of the supercell transformation matrix.  

<img src="/images/generate-supercell.png"/>

When finished setting up the transformation matrix, click on `Submit` and both the crystal data in the central panel of the Materials Designer interface and the 3D representation of the structure on the right-hand viewer will update accordingly to reflect the newly-generated supercell.

# Animation

Click on the animation below to see the above in action. In this example, we generate a 2x2x2 supercell of a cubic structure by inserting the diagonal elements of the corresponding transformation matrix, whilst leaving the off-diagonal elements to zero. In this way the corresponding diagonal supercell expansion is achieved. 

<img data-gifffer="/images/CreateMaterialSupercell.gif" />

# Links

1. [Wikipedia Supercells, Website](https://en.wikipedia.org/wiki/Supercell_(crystal))
