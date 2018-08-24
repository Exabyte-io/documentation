We employ Exabyte Data Convention (EDC) in order to organize and process data. A subset of it is given in this page. 

# Definitions

In a broad sense we consider **Material** to be the physical (chemical, biological) system(s) under investigation, and **Workflow** to be the process of probing (measuring, modeling/simulating) such system.

The diagram illustrates the general relationship between the terms in a visual manner:

![Simulation Diagram](/images/simulation-job-wokflow-unit-explained.png "Simulation Diagram")

> Other terms shown above (eg. "Job", "Unit") are explained elsewhere in this documentation. 

# Classification

We consider the general practices for managing data related to materials RnD and identify the categories and relationships between them. 

## By domain

First we idenity the domain of the data:

- **materials**: information uniquely associated with a certain material
- **workflows**: information about a routine (eg. computational algorithm or experimental equipment) used to extract the data
- **other**: any other information

> NOTE: we postulate that it is generally possible to disentangle the data about materials from the data about the measurement system that extracts the properties of such materials. "Other" category exists for the edge cases where such distinction is problematic.

## By source

We further classify data into 3 main subtypes by source:

- **experimental**: obtained on experimental equipment
- **model**: obtained using modeling (computational or analytical)
- **other**: data that cannot be classified according to any of the above

## By publication status

When the data is first obtained it can be raw, or unprocessed. The opposite is when the data is assembled for a peer-reviewed publication and passed multiple filter channels:
 
- **raw**: directly obtained from the source
- **published**: published in a peer-reviewed journal or analogs
 

# Properties

A property is a single point of information about a system in hand. Below are subclasses of properties.

## By data type

We initially subdivide properties by its relation to the application / execution of a workflow into:

- **scalar**: can be expressed as a single value with an associated measurement units
- **non-scalar**: can not be expressed as above

> NOTE: non-scalar properties may be further subdivided into 1-dimensional arrays, matrices and tensors, for example 
 
## By relation to workflow

We initially subdivide properties by its relation to the application / execution of a workflow into:

- **descriptive properties**: available before executing a *workflow*
- **characteristics**: results or outcomes of the *workflow* application

> EXAMPLE: 
> 1. For atomistic simulations a descriptive property can be the initial structural information (eg. POSCAR, CIF file) and a characteristic property can be electronic conductivity.
> 2. Similarly, for experimental measurement of a descriptive property is the initial information about a sample (eg. percentage of mixed compounds by mass, other relevant conditions) and a characteristic property is what measured as outcome.

> NOTE: workflows can be used in a recursive manner to extract properties of workflow, for example when a workflow is used to train a machine learning model its result is in turn a workflow.  

## By relation to uniqueness

In order to organize the data we must identify materials, and we do so by considering **Identifiers**, a special subset of *Descriptive* properties that helps associating each material with its **exabyteId**. 

> EXAMPLE (Materials):
> 1. For atomistic simulations the identifiers can be directly constructed from the atomistic structure of material(s).
> 2. At the same time, the atomistic structure may be unavailable in experimental findings or for existing datasets, hence we leave room for custom identifiers that can be mapped to *exabyteIds*.

As the example above demonstrates, unique identifiers can be dependent on the source of data.  

## By physical meaning

For non-experimental data it could happen that although the property can be extracted and its value is clearly defined, the value does not hold a physical meaning beyond the extent of the model applied. We call such property **Auxiliary**. Otherwise, a physical meaning is assumed.

> EXAMPLE:
> 1. For atomistic simulations done using planewave pseudopotential method we can extract the Fermi energy and its definition is clear, however there is no physical meaning to its value, as it is heavily dependent on the pseudization scheme.
> 2. Conversely, in the above scenario the electronic band gap, or the difference between electronic energies right below the Fermi level and right above it has physical meaning and can be directly compared with experimental measurements. 


## Summary

Generally, properties for both Materials and Workflows can be assigned the following classification:

|  By data type | By relation to Workflow  | By Uniqueness   | By Physical Meaning      |
|:-------------:|:------------------------:|:---------------:|:------------------------:|
| Scalar        | Descriptive              | Identifier      | (default, non-auxiliary) |
| Non-scalar    | Characteristic           | Non-identifier  | Auxiliary                |

# Jobs

We use "Job" as a "container" entity to organize the data and track resource allocation. The terminology and naming is common for distributed resource allocation management. A job in the computational sense represents the simplest entity that has accounting set up for. More information about Jobs is [here](/workflows/data/jobs.md). 
