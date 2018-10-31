# Method

A theoretical [model](/models/overview.md) may have multiple computational **Methods**, or implementations. Since a method is a numerical property, it always has a certain precision. A method is implemented inside a **simulation engine** (or [application](/software/overview.md)), and each application can itself implement one or more methods.

!!! note "Example Model & Method"
    If we use Newtonian mechanics as Model, then the Method would be the algorithmic implementation of calculating the multiple between m and a in the `F = ma` equation.
    
# Method Properties

Methods in particular consist in the following two elements in the context of the computational aspects of a subworkflow calculation: 

- The **type** of **inter-atomic potential** modeling the various atomic interactions in the crystal structure under investigation. Please consult [this page](pseudopotential/actions.md) for a review of the available pseudopotential **subtypes** within the theoretical context of the DFT model.

- The **cutoff** parameters in both the plane-wave and charge density expansions, again in the context of the DFT theory model, as explained [here](pseudopotential/parameters.md).
