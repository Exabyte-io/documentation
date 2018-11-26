# Primitive Schema Types
 
### 1D Data Series 

Series is an array of arrays containing numbers or strings. It is used to store data
 
```json tab="Schema"
{!schema/primitive/math/1d_data_series.json!}
```

```json tab="Example"
{!example/primitive/math/1d_data_series.json!}
```
 
### 2D Data

Data prepared for a two-dimensional plot.


```json tab="Schema"
{!schema/primitive/math/2d_data.json!}
```

```json tab="Example"
{!example/primitive/math/2d_data.json!}
```

### 2D Plot

Two-dimensional data object, defined in conjunction with two axes.

```json tab="Schema"
{!schema/primitive/math/2d_plot.json!}
```

```json tab="Example"
{!example/primitive/math/2d_plot.json!}
```

### 3D Lattice

Holds the information about the three-dimensional periodic lattice specified through lengths and angles between lattice vectors.


```json tab="Schema"
{!schema/primitive/math/3d_lattice.json!}
```


```json tab="Example"
{!example/primitive/math/3d_lattice.json!}
```

### 3D Plane

Holds the information about a plane incline in  three-dimensions specified through the surface normal of the plane and its origin.


```json tab="Schema"
{!schema/primitive/math/3d_plane.json!}
```


```json tab="Example"
{!example/primitive/math/3d_plane.json!}
```

### 3D Tensor

A tensor which can be represented as a 3x3 matrix (for example the stress tensor).


```json tab="Schema"
{!schema/primitive/math/3d_tensor.json!}
```

```json tab="Example"
{!example/primitive/math/3d_tensor.json!}
```

### 3D Vector Basis

Three non-collinear vectors in three-dimensional space that form a basis set.
 

```json tab="Schema"
{!schema/primitive/math/3d_vector_basis.json!}
```


```json tab="Example"
{!example/primitive/math/3d_vector_basis.json!}
```

### Axis

Used for plotting. It has a label to describe the type of data on the axis and units to describe the units of the data.

```json tab="Schema"
{!schema/primitive/math/axis.json!}
```

```json tab="Example"
{!example/primitive/math/axis.json!}
```

### Point

Point is a generic data type that is expected to be used by many different aspects of the database. It is an array holding three numbers.


```json tab="Schema"
{!schema/primitive/math/point.json!}
```

```json tab="Example"
{!example/primitive/math/point.json!}
```

### Vector

Vector is a generic data type that is expected to be used by many different aspects of the database. It is an array holding three numbers.


```json tab="Schema"
{!schema/primitive/math/vector.json!}
```

```json tab="Example"
{!example/primitive/math/vector.json!}
```
