# Overview of our Product

We summarize here the basic concepts that are used throughout Exabyte.io when referring to simulations.

## Introduction

Useful properties of materials can be obtained either via experiments, from a pure analytical standpoint, or via the application of computational techniques, otherwise referred to as **simulations**. This latter case is what we employ at exabyte.io.

- **Simulation** is an application of a computational model or technique aimed at extracting a specific [property](../properties/overview.md) of [materials](../materials/overview.md).

There are three main concepts that we deal with:

- **Materials**: a combination of chemical elements in a particular geometric arrangement, that can be *uniquely* defined by a set of [descriptive properties](../properties/classification/overview.md) (eg. crystal lattice and basis), and has certain [characteristic properties](../properties/classification/overview.md) that can be computed upon it (eg. band gap, formation energy etc.)

- **Models**: a [theory](../models/overview.md) that provides scientific insight on how to calculate the characteristic properties of a material; it can be applied via multiple possible **Methods**, or [numerical implementations](../methods/overview.md) of the Model. In practice, methods are enacted on our platform via the creation of **[Workflow Computations](../workflows/overview.md)** to be applied on the material.

!!!note "Example Model and Method"
    **Density Functional Theory (DFT)** [^1] is an [example of a model](../models-directory/dft/overview.md), and its **plane-wave pseudopotential formulation** [^2] is an [example of method](../methods-directory/pseudopotential/overview.md). Besides the plane-wave pseudopotential method, DFT can be implemented for example using local orbitals [^3] and/or full-potential calculations [^4].

- **Jobs**: an [entity](../jobs/overview.md) that contains information about the computation that makes the application of the Model (and subsequently Method) upon the material under investigation possible.

More explanation follows for each of the above concepts.

## Material

## Descriptive properties

Descriptive properties has information required to uniquely define a material in a way that prevent duplicates. To identify a material one must know its [geometrical](../properties-directory/structural/lattice.md) and [elemental composition](../properties-directory/structural/basis.md). Every material can be periodic in either 3D (crystals), 2D (surface/film), 1D (polymer) or non-periodic (molecule, amorphous solids). For the purpose of this explanation, we will consider the 3D periodic case only, as all the others can be approximated through it in practice.

Every 3D periodic structure has a minimal unit of repetition, which is called a [Unit cell](../properties-directory/structural/lattice.md). Unit cell is repeated on a crystal [lattice](../properties-directory/structural/lattice.md), which is periodic. Material's composition inside the unit cell is called the [crystal basis](../properties-directory/structural/basis.md). Thus, the information about lattice and basis combined together fully describe the underlying [crystal structure](../properties-directory/structural/final-structure.md) of the material.

!!! note "Note about symmetry"
    Since multiple crystal lattice and basis combinations can represent the same material (eg. primitive vs conventional cells, translations and rotations or basis coordinates), we let users store arbitrary representation at their will, but we only store one "standardized" entry inside [Materials Bank](../materials/bank.md)

### Characteristic properties

Characteristic properties contain parameters that reflect on physical properties of materials that are relevant for the applications purposes. Example characteristic properties are: resistivity, electron mobility, electronic band gap, formation energy, bulk modulus, elasticity, and many others.

Characteristic properties are always obtained as a result of simulations.

## Model

Within our platform, multiple component concepts comprised within a model are employed:

- [Model](../models/overview.md)
- [Method](../methods/overview.md)
- [Workflow](../workflows/overview.md)
- [Subworkflow](../workflows/components/subworkflows.md)
- [Unit](../workflows/components/units.md)

### Components

In order to better understand the difference between Model, Method and Simulation, let us use a travel analogy:

1. When you set out to travel from San Francisco to New York, you know your destination. Therefore, by analogy, a specific address in New York would be a **characteristic property** that you would like to reach (obtain).

2. Then, you choose the way you would like to travel between a flight, a train ride, car ride or shipping. By analogy, after choosing the above-mentioned characteristic property of interest (the address), you choose the **model**.

3. When you board a plane in the airport, or sit into a car, you henceforth choose a specific class of aircraft (jet, propeller, supersonic) or automobile (sedan, SUV, convertible). By analogy, after choosing a model, you would need to choose a specific computational implementation of the model, or the **method**.

4. The plane could take multiple routes, and reach multiple intermediate destinations along the way. By analogy, a method can be realized through multiple **workflows** that contain specifically arranged **units**.

Thus, the process of traveling from San Francisco to New York by analogy would be the **simulation** using a model, and a corresponding method contained within it, employed to extract a specific characteristic property.

!!!note "Simulation Engines"
    Just like there are multiple airplane manufacturers, there are many **simulation engines** (or [software applications](../software/overview.md)) that implement specific model(s) and method(s).

Models, Methods, Workflows, Subworkflows and Units are **nested properties**: the information about units is stored within subworkflows, subworkflows in turn is stored within workflows, workflows within methods, and finally methods is contained inside a model.

## Jobs

A [simulation Job](../jobs/overview.md) is an [entity](../entities-general/overview.md) that represents the computation employed during the simulation, and the simplest entity that has [accounting](../accounts/overview.md) set up for. Jobs contain the information about the aforementioned Model/Method/Workflow/Units, and can be under any of the following possible [statuses](../jobs/status.md).

### Projects

Jobs are organized into [Projects](../jobs/projects.md) for convenience. One can think about projects as collections of jobs, in the same manner as a file system directory is a collection of files.

## Links

[^1]: [Density Functional Theory, Wikipedia](https://en.wikipedia.org/wiki/Density_functional_theory)
[^2]: [Planewave pseudopotential method, presentation](https://www.archer.ac.uk/training/course-material/2014/04/PMMP_UCL/Slides/castep_1.pdf)
[^3]: [Basis sets in quantum chemistry, presentation](http://vergil.chemistry.gatech.edu/courses/chem6485/pdf/basis-sets.pdf)
[^4]: [Full-potential local orbital approach, presentation](http://www.fplo.de/download/Richter-1.pdf)
