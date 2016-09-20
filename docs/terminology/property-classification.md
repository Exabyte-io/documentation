<!-- by MH -->

We define a "characteristic" property as any property that describes the physical nature of the material.

One potential way to break down characteristic properties is by their character such as electronic, mechnical, chemical, & vibrational related properties.  Any choice of classification is somewhat arbitrary and leads to some overlap but we think it serves as a good guide for the users and developers to associate similar properties and focus on a modular software development to enable reuse of tools and properties.



We subdivide all properties into:

- [**Core-Properties**]: Calculated during the application of a Method independent of Simulation Engine, and are unable (too bulky) to provide useful information without further processing.    For a moving set of atoms - coordinates of all atoms and their velocities would be an example of core properties, however without additional processing this information is overwhelming and marginally useful.

- [**Principal-Properties**]:  Obtained directly by applying a 1-shot (1-unit) Method implemented within a Simulation Engine.  For a moving set of atoms - their temperature would be an example Principal property, as it is always calculated by virtually all simulation engines.

- [**Derived-Properties**]:
Derived Principal   Obtained from Principal through a complex workflow and, potentially, additional processing (or through multiple application).   For a moving set of atoms - diffusion coefficient is an example of a derived property that requires calculation of temperature at multiple time steps.
Derived

# Derived Properties
We further subdivide all derived properties into:

- **Electronic Properties**
    - Band Structure
    - Band Gap
    - Density of States and Partial DOS
    - Fermi surface

- **Chemical Properties**
    - Formation energy at 0K

- **Vibrational Properties**
    - Zero Point Energy

