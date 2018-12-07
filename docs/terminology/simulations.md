<!-- by TB -->

This page explains the basic concepts that are used within Exabyte.io when referring to simulations.

# Introduction

Characteristic properties of materials can be obtained either in experiment, or from pure analytical standpoint, or via the application of computational techniques, or **simulations**. This last case is what we employ at exabyte.io.

- **Simulation** is an application of a computational model or technique aimed at extracting a specific property of materials.

There are three main entities that we deal with.

- **Material**: a combination of chemical elements in a particular geometric arrangement, that can be *uniquely* defined by descriptive properties (eg. crystal lattice and basis) and has *characteristic* properties (eg. band gap, formation energy)

- **Model**: an entity that contains scientifically valuable information about the approximations that can be used to calculate characteristic properties of a material; contains multiple *Methods* or numerical implementation of the Model

    !!! note "Example Model and Method"
        Density Functional Theory (DFT) [[1](#links)] is an example of a model, and pseudopotential planewave method [[2](#links)] is an example method. Besides planewave pseudopotential method, DFT can be implemented using local orbitals [[3](#links)] and/or full-potential calculations [[4](#links)].

- **Compute**: or "compute platform" an entity that contains information about the computation that makes the application of the Model (and subsequently Method) possible

More explanation follows.


# Material

## Descriptive properties

Descriptive properties has information required to uniquely define a material in a way that prevent duplicates. To identify a material one must know its geometrical and elemental composition. Every material can be periodic in either 3D (crystals), 2D (surface/film), 1D (polymer) or non-periodic (molecule, amorphous solids). For the purpose of this explanation, we will consider 3D periodic case only, as all the others can be approximated by it in practice.

Every 3D periodic structure has a minimal unit of repetition, which is called a Unit cell [[5](#links)]. Unit cell is repeated on a crystal lattice, or simply **lattice**, that is periodic. Material's composition inside the unit cell is called crystal basis, or simply **basis**. Thus, the information about lattice and basis fully describes a material.

!!! note "Note about symmetry"
    Since multiple crystal lattice and basis combinations can represent the same material (eg. primitive vs conventional cells, translations and rotations or basis coordinates) we let users store arbitrary representation at their will, but only store one "standardized" entry inside [Materials Bank](#materials-bank)

## Characteristic properties

Characteristic properties, or **characteristics**, contains parameters that reflect on physical properties of materials that are relevant for the applications purposes. Example characteristic properties are: resistivity, electron mobility, electronic band gap, formation energy, bulk modulus, elasticity, and many others.

Characteristics are obtained as a result of simulations.


# Model

Within our product multiple entities related to model and method are used.

- Model
- Method
- Unit
- Workflow
- Job


## Method, Workflow, Units

In order to better understand the difference between Model, Method and Simulation, let's use a travel analogy.

1. When you set out to travel from San Francisco to New York, you know your destination, by analogy a specific address in New York would be a **characteristic** that you'd like to obtain

2. Then you choose the way you'd like to travel between a flight, a train ride, car ride or shipping, by analogy after choosing characteristic property of interest you choose the **model**

3. When you board a plane in the airport, or sit into a car, you henceforth choose a specific class of aircraft (jet, propeller, supersonic) or automobile (sedan, SUV, convertible), by analogy after choosing a model you would need to choose a specific computational implementation of the model or **method**

    Thus the process of traveling from San Francisco to New York by analogy would be the **simulation** using a model, and a corresponding method contained within it, employed to extract a specific characteristic property.

    !!! note "Simulation Engines"
        Just like there are multiple airplane manufacturers, there are many **simulation engines** (or software applications) that implement specific model(s) and method(s).

4. The plane could take multiple routes and reach multiple intermediate destinations along the way, by analogy a method can be realized through multiple **workflows** that contain specifically arranged **units**

Model, Method, Workflow and Units are nested properties, meaning that the information about units is stored within workflow, workflow in turn is stored within method and method is contained inside a model.

# Compute

## Jobs

**Job** is an entity that represents the computation employed during the simulation, and the simplest entity that has accounting set up for. Job contains the information about Model/Method/Workflow/Units.

## Projects

Jobs are organized into **Projects** for convenience. One can think about projects as collections of jobs in the same manner as a file system directory is a collection of files.

## Job Properties

- Title
- Type: a brief description of a workflow that this job is using
- Created At: date and time of job creation
- Status: one of the statuses explained below
- Owner: account that created this job (by default)
- Actions: available actions applicable to this job - example: clone, delete

## Job Statuses

| Label    |      Meaning  |
|----------|:--------------|
<span class="">pre-submission</span> | job is created and saved in database
<span class="">submitted</span> | job is scheduled for execution
<span class="">active</span> | job is currently running
<span class="">finished</span> | job finished successfully
<span class="">error</span> | something went wrong with job execution
<span class="">timeout</span> | job exceeded allocated walltime
<span class="">terminated</span> | job is terminated by user

## Links

1. [Density Functional Theory, Wikipedia](https://en.wikipedia.org/wiki/Density_functional_theory)
1. [Planewave pseudopotential method, presentation](https://www.archer.ac.uk/training/course-material/2014/04/PMMP_UCL/Slides/castep_1.pdf)
1. [Basis sets in quantum chemistry, presentation](http://vergil.chemistry.gatech.edu/courses/chem6485/pdf/basis-sets.pdf)
1. [Full-potential local orbital approach, presentation](http://www.fplo.de/download/Richter-1.pdf)
1. [Crystal Structure, Wikipedia](https://en.wikipedia.org/wiki/Crystal_structure)
