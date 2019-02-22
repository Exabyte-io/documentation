# Interpolated Set

**Interpolated Sets** are necessary for the calculation of the energy profile and activation barrier for the multi-dimensional energy space of chemical reactions via the [Nudged Elastic Bands (NEB) method](../../../tutorials/dft/chemical/neb.md).

The NEB method is centred around the initial and final configurations (structures) for the chemical reaction under investigation. Multiple molecular structures, referred to as **images**, of the system being considered need to be generated in between these initial and final configurations, by varying a **one-dimensional reaction "coordinate"** from its initial to final value. This set of images taken together constitutes the interpolated set for the chemical reaction.

## Animation

In the animation below, we generate an interpolated set with 5 intermediate images from a pair of initial and final structures.

<img data-gifffer="/images/materials-designer/generate-interpolated-set.gif" />
