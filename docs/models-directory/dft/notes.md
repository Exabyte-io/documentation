# Special Notes 

We list in the present page some special notices concerning the [parameters](parameters.md) underlying the [Density Functional Theory model](overview.md).

## Accuracy Limits of the Generalized Gradient Approximation

### Electronic Band Gap

When computations of the [Electronic Band Gap](../../properties-directory/non-scalar/band-gaps.md) are executed through [Density Functional Theory](../../models-directory/dft/overview.md), operated in conjunction with the [Generalized Gradient Approximation](parameters.md#subtype) (GGA), a systematic **under-estimation of the band gap** is to be expected. This is a well-known shortcoming of the GGA technique, and should be taken into account when following the [procedure](../../tutorials/dft/electronic/band-gap.md) for calculating the band-gap of semiconducting materials. 

Further modifications to the input files and settings to correctly predict the band gap are possible, but lie beyond the scope of the present discussion.
