# Overview of our Product

We summarize here the basic concepts that are used throughout Exabyte.io when referring to simulations.

## Introduction

Useful properties of materials can be obtained either via experiments, from a pure analytical standpoint, or via the application of computational techniques, otherwise referred to as **simulations**. This latter case is what we employ at exabyte.io.

- **Simulation** is an application of a computational model or technique aimed at extracting a specific [property](../properties/overview.md) of [materials](../materials/overview.md).

There are three main concepts that we deal with:

- **Materials**: a combination of chemical elements in a particular geometric arrangement, that can be *uniquely* defined by a set of [descriptive properties](../properties/classification/overview.md) (eg. crystal lattice and basis), and has certain [characteristic properties](../properties/classification/overview.md) that can be computed upon it (eg. band gap, formation energy etc.)

- **Models**: a [theory](../models/overview.md) that provides scientific insight on how to calculate the characteristic properties of a material; it can be applied via multiple possible **Methods**, or [numerical implementations](../methods/overview.md) of the Model. In practice, methods are enacted on our platform via the creation of **[Workflow Computations](../workflows/overview.md)** to be applied on the material.

!!!note "Example Model and Method"
    **Density Functional Theory (DFT)** is an [example of a model](../models-directory/dft/overview.md), and its **plane-wave pseudopotential formulation** is an [example of method](../methods-directory/pseudopotential/overview.md). Detailed theoretical reviews of such concepts can be found in the references listed [herein](../models-directory/dft/references.md).

- **Jobs**: an [entity](../jobs/overview.md) that contains information about the computation that makes the application of the Model (and subsequently Method) upon the material under investigation possible.

More explanation follows for each of the above concepts.

## Properties

We introduce the classification schemes of material properties, such as structural, electronic and thermodynamic properties, [in this section of the documentation](../properties/classification/overview.md).

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
