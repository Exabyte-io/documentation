# Methodology

## HPL

HPL is a software package that solves a (random) dense linear system in double precision (64 bits) arithmetic on distributed-memory computers. It can thus be regarded as a portable as well as freely available implementation of the High Performance Computing Linpack Benchmark.

The algorithm used by HPL can be summarized by the following keywords: Two-dimensional block-cyclic data distribution - Right-looking variant of the LU factorization with row partial pivoting featuring multiple look-ahead depths - Recursive panel factorization with pivot search and column broadcast combined - Various virtual panel broadcast topologies - bandwidth reducing swap-broadcast algorithm - backward substitution with look-ahead of depth 1.

The HPL package provides a testing and timing program to quantify the accuracy of the obtained solution as well as the time it took to compute it. The best performance achievable by this software depends on a large variety of factors. The following shows a sample HPL.dat used for running HPL on 32 nodes on Amazon Web Services (AWS).

<details>
    <summary>**HPL.dat**</summary>
```
HPLinpack benchmark input file
Innovative Computing Laboratory, University of Tennessee
HPL.out      output file name (if any)
6            device out (6=stdout,7=stderr,file)
1            # of problems sizes (N)
456768       Ns
1            # of NBs
192          NBs
1            PMAP process mapping (0=Row-,1=Column-major)
1            # of process grids (P x Q)
32           Ps
36           Qs
16.0         threshold
1            # of panel fact
1            PFACTs (0=left, 1=Crout, 2=Right)
1            # of recursive stopping criterium
4            NBMINs (>= 1)
1            # of panels in recursion
2            NDIVs
1            # of recursive panel fact.
1            RFACTs (0=left, 1=Crout, 2=Right)
1            # of broadcast
6            BCASTs (0=1rg,1=1rM,2=2rg,3=2rM,4=Lng,5=LnM,6=Psh,7=Psh2)
1            # of lookahead depth
0            DEPTHs (>=0)
0            SWAP (0=bin-exch,1=long,2=mix)
1            swapping threshold
1            L1 in (0=transposed,1=no-transposed) form
1            U  in (0=transposed,1=no-transposed) form
0            Equilibration (0=no,1=yes)
8            memory alignment in double (> 0)
```
</details>

!!! warning "HPL optimization"
    Moderate effort has been put into the optimization of HPL benchmark for each of the cases studied. The results should be considered a quick estimate rather than exhaustive study. We expect a ~20% improvement to be possible with further optimization.


# Hardware

The specification of Amazon Web Services (AWS) and Microsoft Azure (Azure) resources are as follow:

|Provider  |CPU                                      |Memory (GB) |Disk (GB) |Bandwidth (Gbps)|
|:---------|:---------------------------------------:|:----------:|:--------:|:---------------:|
|AWS       |36 core, Intel Xeon E5-2666-v3, 2.90GHz  |60          |10        |10               |
|Azure     |16 core, Intel Xeon E5-2673-v3, 2.40GHz  |32          |256       |10               |
|Azure-IB  |16 core, Intel Xeon E5-2670-v0, 2.60GHz  |112         |382       |32               |


# Results

The maximal LINPACK performance achieved (Rmax), theoretical peak performance (Rpeak), speedup and speedup ratio (speedup / ideal speedup) are shown below. The HPL benchmark is executed on 1-32 nodes on AWS and Azure resources.

## AWS

For Amazon Web Services we study 3 different scenarios: the default hyper-threaded, non-hyperthreaded and non-hyperthreaded mode with placement group enabled. [c4.8xlrage](https://aws.amazon.com/ec2/instance-types) instance types are used.

### AWS default (AWS)

The following shows the HPL benchmark results running on AWS instances with Hyper-Threading enabled (default).

| Nodes | Cores | Rmax (TFLOPS) | Rpeak (TFLOPS) | Speedup | Ideal speedup | Speedup Ratio |
|:-----:|:-----:|:--------------:|:-------------:|:-------:|:-------------:|:-------------:|
|   1   |   36  |      0.53      |       1.63    |   1.00  |       1       |      1.00     |
|   2   |   72  |      0.98      |       3.26    |   1.85  |       2       |      0.93     |
|   4   |  144  |      1.51      |       6.53    |   2.87  |       4       |      0.72     |
|   8   |  288  |      2.90      |      13.05    |   5.50  |       8       |      0.69     |
|   16  |  576  |      5.23      |      26.10    |   9.92  |       16      |      0.62     |
|   32  |  1152 |      8.65      |      52.20    |  16.41  |       32      |      0.51     |


### AWS non-hyperthreaded (AWS-NHT)

The following shows the HPL benchmark results running with Hyper-Threading disabled to get to the turbo frequency. To do so, only 18 cores of 36 cores were used to run HPL benchmarks.

| Nodes | Cores | Rmax (TFLOPS) | Rpeak (TFLOPS) | Speedup | Ideal speedup | Speedup Ratio |
|:-----:|:-----:|:--------------:|:-------------:|:-------:|:-------------:|:-------------:|
|   1   |   18  |      0.64      |       0.82    |   1.00  |       1       |      1.00     |
|   2   |   36  |      1.14      |       1.63    |   1.77  |       2       |      0.89     |
|   4   |   72  |      1.94      |       3.26    |   3.02  |       4       |      0.76     |
|   8   |  144  |      3.51      |       6.53    |   5.47  |       8       |      0.68     |
|   16  |  288  |      5.59      |      13.05    |   8.71  |       16      |      0.54     |
|   32  |  576  |      10.68     |      26.10    |  16.65  |       32      |      0.52     |

## AWS non-hyperthreaded with placement groups (AWS-NHT-PG)

The following shows the HPL benchmark results with Hyper-Threading disabled and [placement group](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement-groups.html) enabled. A placement group is a logical grouping of instances within a single Availability Zone, recommended for applications that benefit from low network latency, high network throughput, or both.

| Nodes | Cores | Rmax (TFLOPS) | Rpeak (TFLOPS) | Speedup | Ideal speedup | Speedup Ratio |
|:-----:|:-----:|:--------------:|:-------------:|:-------:|:-------------:|:-------------:|
|   1   |   18  |      0.62      |       0.82    |   1.00  |       1       |      1.00     |
|   2   |   36  |      1.14      |       1.63    |   1.82  |       2       |      0.91     |
|   4   |   72  |      1.97      |       3.26    |   3.15  |       4       |      0.79     |
|   8   |  144  |      3.51      |       6.53    |   5.61  |       8       |      0.70     |
|   16  |  288  |      5.70      |      13.05    |   9.12  |       16      |      0.57     |
|   32  |  576  |      10.74     |      26.10    |  17.18  |       32      |      0.54     |

## Azure

For Microsoft Azure we study 2 scenarios as explained below.

### Azure default (AZ)

The following shows the HPL benchmark results running on Azure [Standard_F16](https://azure.microsoft.com/en-us/documentation/articles/virtual-machines-windows-sizes/#fs-series) VMs.

| Nodes | Cores | Rmax (TFLOPS) | Rpeak (TFLOPS) | Speedup | Ideal speedup | Speedup Ratio |
|:-----:|:-----:|:--------------:|:-------------:|:-------:|:-------------:|:-------------:|
|   1   |   16  |      0.48      |       0.6     |   1.00  |       1       |      1.00     |
|   2   |   32  |      0.87      |       1.2     |   1.82  |       2       |      0.91     |
|   4   |   64  |      1.49      |       2.4     |   3.14  |       4       |      0.78     |
|   8   |  128  |      3.04      |       4.8     |   6.38  |       8       |      0.80     |
|   16  |  256  |      5.33      |       9.6     |  11.18  |       16      |      0.70     |
|   32  |  512  |      10.53     |       19.2    |  22.11  |       32      |      0.69     |

## Azure Infiniband on A-series VMs (AZ-IB-A)

The following shows the HPL benchmark results running on Azure [Standard_A9](https://azure.microsoft.com/en-us/documentation/articles/virtual-machines-windows-sizes/#a-series) VMs using Infiniband interconnect network.

| Nodes | Cores | Rmax (TFLOPS) | Rpeak (TFLOPS) | Speedup | Ideal speedup | Speedup Ratio |
|:-----:|:-----:|:-------------:|:--------------:|:-------:|:-------------:|:-------------:|
|   1   |   16  |      0.30     |      0.65      |   1.00  |       1       |      1.00     |
|   2   |   32  |      0.58     |       1.3      |   1.95  |       2       |      0.98     |
|   4   |   64  |      1.16     |       2.6      |   3.91  |       4       |      0.98     |
|   8   |  128  |      2.25     |       5.2      |   7.56  |       8       |      0.95     |
|   16  |  256  |      4.42     |      10.4      |  14.88  |       16      |      0.93     |
|   32  |  512  |      8.59     |      20.8      |  28.94  |       32      |      0.90     |

## Azure Infiniband on H-series VMs (AZ-IB-H)

The following shows the HPL benchmark results running on Azure [Standard_H16r](https://azure.microsoft.com/en-us/documentation/articles/virtual-machines-windows-sizes/#h-series) VMs using Infiniband interconnect network.

| Nodes | Cores | Rmax (TFLOPS) | Rpeak (TFLOPS) | Speedup | Ideal speedup | Speedup Ratio |
|:-----:|:-----:|:-------------:|:--------------:|:-------:|:-------------:|:-------------:|
|   1   |   16  |      0.61     |      0.65      |   1.00  |       1       |      1.00     |
|   2   |   32  |      1.22     |       1.3      |   2.01  |       2       |      1.00     |
|   4   |   64  |      2.40     |       2.6      |   3.93  |       4       |      0.98     |
|   8   |  128  |      4.69     |       5.2      |   7.69  |       8       |      0.96     |
|   16  |  256  |      9.09     |      10.4      |  14.91  |       16      |      0.93     |
|   32  |  512  |     17.26     |      20.8      |  28.33  |       32      |      0.89     |

## NERSC Edison Supercomputer (NERSC-E)

The following shows the HPL benchmark results running on [NERSC Edison](http://www.nersc.gov/users/computational-systems/edison) supercomputer with Hyper-Threading enabled. Edison is a Cray XC30, with a peak performance of 2.57 PFLOPS, 133,824 compute cores, 357 terabytes of memory, and 7.56 petabytes of disk.

| Nodes | Cores | Rmax (TFLOPS) | Rpeak (TFLOPS) | Speedup | Ideal speedup | Speedup Ratio |
|:-----:|:-----:|:-------------:|:--------------:|:-------:|:-------------:|:-------------:|
|   1   |   48  |      0.38     |       0.9      |   1.00  |       1       |      1.00     |
|   2   |   96  |      0.73     |       1.8      |   1.91  |       2       |      0.95     |
|   4   |  192  |      1.34     |       3.6      |   3.48  |       4       |      0.87     |
|   8   |  384  |      2.79     |       7.2      |   7.27  |       8       |      0.91     |
|   16  |  768  |      5.40     |      14.4      |  14.06  |       16      |      0.88     |
|   32  |  1536 |     10.44     |      28.8      |  27.17  |       32      |      0.85     |

## RackSpace (RS)

The following shows the HPL benchmark results running on RackSpace [Compute1-60](https://www.rackspace.com/en-us/cloud/servers) VMs. Compute1-60 VM has 32 VCPUs, 60GB RAM and 5,000Mb/s bandwidth.

| Nodes | Cores | Rmax (TFLOPS) | Rpeak (TFLOPS | Speedup | Ideal speedup | Speedup Ratio |
|:-----:|:-----:|:-------------:|:-------------:|:-------:|:-------------:|:-------------:|
|   1   |   32  |      0.16     |      0.7      |   1.00  |       1       |      1.00     |
|   2   |   64  |      0.28     |      1.4      |   1.68  |       2       |      0.84     |
|   4   |  128  |      0.57     |      2.8      |   3.46  |       4       |      0.86     |
|   8   |  256  |      0.98     |      5.6      |   5.97  |       8       |      0.75     |
|   16  |  512  |      2.14     |      11.2     |  13.07  |       16      |      0.82     |
|   32  |  1024 |      3.04     |      22.4     |  18.55  |       32      |      0.58     |

## SoftLayer (SL)

The following shows the HPL benchmark results running on SoftLayer [virtual servers](http://www.softlayer.com/virtual-servers), each has 32 cores, 64 GB RAM and 1Gb/s bandwidth.

| Nodes | Cores | Rmax (TFLOPS) | Rpeak (TFLOPS | Speedup | Ideal speedup | Speedup Ratio |
|:-----:|:-----:|:-------------:|:-------------:|:-------:|:-------------:|:-------------:|
|   1   |   32  |      0.57     |     0.525     |   1.00  |       1       |      1.00     |
|   2   |   64  |      0.66     |      1.05     |   1.16  |       2       |      0.58     |
|   4   |  128  |      0.44     |      2.1      |   0.77  |       4       |      0.19     |
|   8   |  256  |      0.67     |      4.2      |   1.17  |       8       |      0.15     |
|   16  |  512  |      1.46     |      8.4      |   2.58  |       16      |      0.16     |
|   32  |  1024 |      2.46     |      16.8     |   4.33  |       32      |      0.14     |

# Speedup Ratio

Here is a comparison of speedup ratios for the scenarios described above. As it can be seen, Azure outperforms AWS because of a low latency interconnection network which facilitates more efficient scaling of HPL. In addition the results show that IB-based Azure VMs can deliver better performance than top-tier traditional high-performance computing systems like NERSC Edison, and confirm that cloud computing is becoming a viable and cost-effective alternative. SoftLayer has the least speedup ratio likely because of low speed interconnect network.

![Speedup Ratio](../images/speedup-ratio.png "Speedup Ratio")

# Performance per Core

The following visual shows a comparative plot of performance per core in GFLOPS for the scenarios described above. Although Azure shows better scaling, AWS has better performance per core for up to 16 nodes, likely because of faster processors. As it can be seen, NERSC Edison supercomputer with Hyper-Threading enabled showed the lowest performance per core, likely because of the processor type.

![Performance per Core](../images/performance-per-core.png "Performance per Core")

# Links

- [HPL](http://www.netlib.org/benchmark/hpl)

- [HPL Calculator](http://hpl-calculator.sourceforge.net)
