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

The specification of Amazon Web Services (AWS) and Microsoft Azure (Azure) resources are as follow:

|Provider  |CPU                                      |Memory (GB) |Disk (GB) |Bandwidth (Gbps)|
|:---------|:---------------------------------------:|:----------:|:--------:|:---------------:|
|AWS       |36 core, Intel Xeon E5-2666-v3, 2.90GHz  |60          |10        |10               |
|Azure     |16 core, Intel Xeon E5-2673-v3, 2.40GHz  |32          |256       |10               |
|Azure-IB  |16 core, Intel Xeon E5-2670-v0, 2.60GHz  |112         |382       |32               |


# Results

The maximal LINPACK performance achieved (Rmax), theoretical peak performance (Rpeak), speedup and speedup ratio (speedup / ideal speedup) are shown below. The HPL benchmark is executed on 1-32 nodes on AWS and Azure resources.

## AWS

The following shows the HPL benchmark results running on AWS [c4.8xlrage](https://aws.amazon.com/ec2/instance-types) instances with Hyper-Threading disabled to get to the turbo frequency. To do so, only 18 cores of 36 cores were used to run HPL benchmarks.

| Nodes | Cores | Rmax (TFLOPS) | Rpeak (TFLOPS) | Speedup | Ideal speedup | Speedup Ratio |
|:-----:|:-----:|:--------------:|:-------------:|:-------:|:-------------:|:-------------:|
|   1   |   18  |      0.64      |       0.82    |   1.00  |       1       |      1.00     |
|   2   |   36  |      1.14      |       1.63    |   1.77  |       2       |      0.89     |
|   4   |   72  |      1.94      |       3.26    |   3.02  |       4       |      0.76     |
|   8   |  144  |      3.51      |       6.53    |   5.47  |       8       |      0.68     |
|   16  |  288  |      5.59      |      13.05    |   8.71  |       16      |      0.54     |
|   32  |  576  |      10.68     |      26.10    |  16.65  |       32      |      0.52     |

## AWS-HT

The following shows the HPL benchmark results running on AWS [c4.8xlrage](https://aws.amazon.com/ec2/instance-types) instances with Hyper-Threading enabled (enabled by default).

| Nodes | Cores | Rmax (TFLOPS) | Rpeak (TFLOPS) | Speedup | Ideal speedup | Speedup Ratio |
|:-----:|:-----:|:--------------:|:-------------:|:-------:|:-------------:|:-------------:|
|   1   |   36  |      0.53      |       1.63    |   1.00  |       1       |      1.00     |
|   2   |   72  |      0.98      |       3.26    |   1.85  |       2       |      0.93     |
|   4   |  144  |      1.51      |       6.53    |   2.87  |       4       |      0.72     |
|   8   |  288  |      2.90      |      13.05    |   5.50  |       8       |      0.69     |
|   16  |  576  |      5.23      |      26.10    |   9.92  |       16      |      0.62     |
|   32  |  1152 |      8.65      |      52.20    |  16.41  |       32      |      0.51     |

## AWS-PG

The following shows the HPL benchmark results running on AWS [c4.8xlrage](https://aws.amazon.com/ec2/instance-types) instances Hyper-Threading disabled and [placement group](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement-groups.html) enabled. A placement group is a logical grouping of instances within a single Availability Zone, recommended for applications that benefit from low network latency, high network throughput, or both.

| Nodes | Cores | Rmax (TFLOPS) | Rpeak (TFLOPS) | Speedup | Ideal speedup | Speedup Ratio |
|:-----:|:-----:|:--------------:|:-------------:|:-------:|:-------------:|:-------------:|
|   1   |   18  |      0.62      |       0.82    |   1.00  |       1       |      1.00     |
|   2   |   36  |      1.14      |       1.63    |   1.82  |       2       |      0.91     |
|   4   |   72  |      1.97      |       3.26    |   3.15  |       4       |      0.79     |
|   8   |  144  |      3.51      |       6.53    |   5.61  |       8       |      0.70     |
|   16  |  288  |      5.70      |      13.05    |   9.12  |       16      |      0.57     |
|   32  |  576  |      10.74     |      26.10    |  17.18  |       32      |      0.54     |

## Azure

The following shows the HPL benchmark results running on Azure [Standard_F16](https://azure.microsoft.com/en-us/documentation/articles/virtual-machines-windows-sizes/#fs-series) VMs.

| Nodes | Cores | Rmax (TFLOPS) | Rpeak (TFLOPS) | Speedup | Ideal speedup | Speedup Ratio |
|:-----:|:-----:|:--------------:|:-------------:|:-------:|:-------------:|:-------------:|
|   1   |   16  |      0.48      |       0.6     |   1.00  |       1       |      1.00     |
|   2   |   32  |      0.87      |       1.2     |   1.82  |       2       |      0.91     |
|   4   |   64  |      1.49      |       2.4     |   3.14  |       4       |      0.78     |
|   8   |  128  |      3.04      |       4.8     |   6.38  |       8       |      0.80     |
|   16  |  256  |      5.33      |       9.6     |  11.18  |       16      |      0.70     |
|   32  |  512  |      10.53     |       19.2    |  22.11  |       32      |      0.69     |


## Azure-IB

The following shows the HPL benchmark results running on Azure [Standard_A9](https://azure.microsoft.com/en-us/documentation/articles/virtual-machines-windows-sizes/#a-series) VMs using infiniband interconnection network.

| Nodes | Cores | Rmax (TFLOPS) | Rpeak (TFLOPS) | Speedup | Ideal speedup | Speedup Ratio |
|:-----:|:-----:|:--------------:|:-------------:|:-------:|:-------------:|:-------------:|
|   1   |   16  |      0.30      |       0.65    |  19.01  |       1       |      1.00     |
|   2   |   32  |      0.58      |       1.30    |  18.56  |       2       |      0.98     |
|   4   |   64  |      1.16      |       2.60    |  18.58  |       4       |      0.98     |
|   8   |  128  |      2.25      |       5.20    |  17.97  |       8       |      0.95     |
|   16  |  256  |      4.42      |      10.40    |  17.68  |       16      |      0.93     |
|   32  |  512  |      8.59      |      20.80    |  17.19  |       32      |      0.90     |

# Speedup Ratio

The following visual shows the speedup ratio for AWS without Hyper-Threading(AWS), AWS with Hyper-Threading enabled(AWS-HT), Azure and Azure with IB (Azure-IB). It is obvious that Azure outperforms AWS because of a faster, low latency interconnection network which makes HPL scale more efficiently.

![Speedup Ratio](../images/speedup-ratio.png "Speedup Ratio")

# Performance per Core 

The following visual shows the performance per core in GFLOPS for AWS without Hyper-Threading(AWS), AWS with Hyper-Threading enabled(AWS-HT), Azure and Azure with IB (Azure-IB). Although Azure has a better interconnection network and performs better on scaling, but still AWS has better performance per core for up to 16 nodes because of faster processors.

![Performance per Core](../images/performance-per-core.png "Performance per Core")


# Links

- [HPL](http://www.netlib.org/benchmark/hpl)

- [HPL Calculator](http://hpl-calculator.sourceforge.net)
