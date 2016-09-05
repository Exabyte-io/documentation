<!-- by MM -->

<!-- TODO: add input files and structures for the materials and use cases studied -->

This page contains benchmarks for three usage scenarios considered:

- high-throughput calculations
- distributed memory calculations
- performance within one compute-node

## High-throughput scalability study

### Overview

A team of researchers from a public enterprise company used exabyte.io to study equilibrium geometries and formation energies for a set of promising metallic alloys. The team employed quantum mechanical modeling approaches based on density functional theory and vast compute power available on public cloud. During a single run researchers were able to scale to 10,656 CPUs within a few minutes from the start, and obtain accurate results for 296 compounds that represent ternary metallic alloys within 36 hours. The purpose of this study was to estimate the extent to which compute resources can be efficiently scaled while sustaining a constant level of performance.

### Model and Method

Plane-wave Pseudopotential Density Functional Theory formalism as implemented in Vienna Ab-initio Simulation Package (VASP) at version 5.3.5 with a corresponding set of atomic pseudo-potentials was employed in this run.

### Results

High-performance computing resources were assembled on-demand using the infrastructure available at one of the public cloud vendors. For the first run, a total of 296 tasks (one-per-material) were submitted to exabyte.io cloud-scale resource-management system. Within 7 minutes after submission 296 compute nodes with 10,656 cores total were provisioned, configured and had compute tasks running on them.

![High-Throughput Scalability](../images/HighThroughputScalability.png "High-Throughput Scalability")

All tasks were finished within 38 hours from the start, with the shortest ones taking about 2 hours. The size of compute system was dynamically scaled with the number of active calculations. The total cost of the calculation was within a few thousand dollars (for comparison - the cost of buying 10,000 CPU can be estimated at several million dollars).


### Conclusion

A "real-world" example high-throughput materials discovery run scaling to nearly 300 materials (each with an advanced geometrical configuration involving 24 atoms inside a crystal unit cell) and nearly 11 thousand CPU was successfully attempted by an enterprise customer. Without large upfront expenditures and while using familiar environments and tools, they were able to quickly obtain the necessary data about the formation energies of metallic alloys. This data is now being used by the customer to guide their experimental search for better alloys. The scale of this run was, however, is far from the limit on the resources available at exabyte.io, and we have internal data in possession that shows significantly higher scale reached by our engineering team in development (contact us in case you would like to learn more).


## Distributed memory calculations

### Overview

The purpose of this study was to estimate the extent to which a calculation for a single materials can be efficiently scaled.


### Model and Method

Vienna Ab-initio Simulation Package (VASP) at version 5.3.5 with a corresponding set of atomic pseudo-potentials, and Quantum ESPRESSO (QE) at version 5.2.1 with a set of pseudo-potentials as explained below were employed for this study.

Two basic parallelization schemes were attempted:

* parallelization over the electronic bands for large-unit-cell materials (further referred to as ELB)
* parallelization over the sampling points in reciprocal space, or k-points (further referred to as  KPT)

Compute nodes with a total of 36 CPU per node were used. Number of cores per node (PPN) and total number of nodes (NODES) were used to distinguish between parallelization levels.

### Results

#### VASP-ELB

Material: "Ba25 Bi15 O54" with a supercell containing 188 atoms

![Distributed Memory Calculations VASP ELB](../images/DistributedMemoryCalculationsVASPELB.png "Distributed Memory Calculations VASP ELB")

#### VASP-KPT

Material: "Li8 V8 Mo8" with a unit cell containing 24 atoms

![Distributed Memory Calculations VASP KPT](../images/DistributedMemoryCalculationsVASPKPT.png "Distributed Memory Calculations VASP KPT")

#### QE-ELB

Material: Aluminum surface containing 112 atoms

![Distributed Memory Calculations QE ELB](../images/DistributedMemoryCalculationsQEELB.png "Distributed Memory Calculations QE ELB")

#### QE-KPT

Material: FeSe monolayer with 4 atoms

![Distributed Memory Calculations QE KPT](../images/DistributedMemoryCalculationsQEKPT.png "Distributed Memory Calculations QE KOT")


### Conclusions

* VASP and QE were studied for scalability for a single material - single calculation,
* K-point sampling based parallelization appears to be feasible and scales efficiently up to 16 nodes,
* Parallelization over the electronic bands for the cases studied shows efficient scalability up to 4 nodes for VASP, for QE an adjustment of parallelization parameters is necessary to reach efficient parallelization over electronic bands.

## Cloud vendors performance comparison

Exabyte.io utilizes multiple cloud vendors resources to provide users with a large scale computing infrastructure. Since Each cloud provider uses a specific type of resources, applications performance vary on different cloud vendors. We ran the same calculation on four cloud providers, AWS, Rackspace, SoftLayer and Microsoft Azure and got the following result.

|Provider  |CPU                                      |Memory (GB) |Disk (GB) |Bandwidth (Gbps) |Runtime (sec)|
|:---------|:---------------------------------------:|:---------:|:-------:|:--------------:|:---------------:|
|AWS       |36 cores, Intel Xeon E5-2666-v3, 2.90GHz |60         |10       |10              |37.8             |
|Azure     |16 cores, Intel Xeon E5-2673-v3, 2.40GHz |32         |256      |10              |43.5             |
|Rackspace |32 cores, Intel Xeon E5-2680-v2, 2.80GHz |60         |50       |5               |49               |
|Softlayer |32 cores, Intel Xeon E5-2650-v0, 2.00GHz |64         |25       |1               |89.5             |
