# Stress Tensor

The stress tensor ${\boldsymbol {\sigma }}$ [^1] is a [Physical](../../properties/classification/general.md) property. It is a second-rank **tensor**, representable as a **Matrix**, which consists of nine components $\sigma _{ij}$ that completely define the state of stress at a point inside a deformed material. 

$$
{\boldsymbol  {\sigma }}=\left[{{\begin{matrix}\sigma _{{xx}}&\sigma _{{xy}}&\sigma _{{xz}}\\\sigma _{{yx}}&\sigma _{{yy}}&\sigma _{{yz}}\\\sigma _{{zx}}&\sigma _{{zy}}&\sigma _{{zz}}\\\end{matrix}}}\right]
$$

The image below offers an explanation of the directions in which each shear and normal stress component expressed above acts upon, relative to a Cartesian coordinate system.

![Stress Tensor](/images/Properties/Components_of_Stress_Tensor.png "Stress Tensor")

## Computation

Under the [Results Tab](../../jobs/ui/results-tab.md) of [Job Viewer](../../jobs/ui/viewer.md), the components of the stress tensor are presented as follows, expressed in units of kilobars (kbar).

![Stress Tensor](/images/Properties/stress-tensor.png "Stress Tensor")

## Schema and Example 

The JSON schema and an example representation for this property can be found [here](../../properties/data/list.md#stress-tensor).

## Links

[^1]: [Wikipedia Cauchy stress tensor, Website](https://en.wikipedia.org/wiki/Cauchy_stress_tensor)
