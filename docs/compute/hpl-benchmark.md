# HPL Scalability Benchmark

## Methodology

### HPL

HPL is a software package that solves a (random) dense linear system in double precision (64 bits) arithmetic on distributed-memory computers. It can thus be regarded as a portable as well as freely available implementation of the High Performance Computing Linpack Benchmark. 

The algorithm used by HPL can be summarized by the following keywords: Two-dimensional block-cyclic data distribution - Right-looking variant of the LU factorization with row partial pivoting featuring multiple look-ahead depths - Recursive panel factorization with pivot search and column broadcast combined - Various virtual panel broadcast topologies - bandwidth reducing swap-broadcast algorithm - backward substitution with look-ahead of depth 1. 

The HPL package provides a testing and timing program to quantify the accuracy of the obtained solution as well as the time it took to compute it. The best performance achievable by this software depends on a large variety of factors. The following shows a smaple HPL.dat that we use for running HPL on 32 nodes on AWS. 

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

The specification of AWS and Azure resources are as follow:

|Provider  |CPU                                      |Memory (GB) |Disk (GB) |Bandwidth (Gbps)|
|:---------|:---------------------------------------:|:----------:|:-------:|:---------------:|
|AWS       |36 core, Intel Xeon E5-2666-v3, 2.90GHz  |60          |10       |10               |
|Azure     |16 core, Intel Xeon E5-2673-v3, 2.40GHz  |32          |256      |10               |


## Results

The maximal LINPACK performance achieved (Rmax), theoretical peak performance (Rpeak), speedup and speedup ratio (speedup / ideal speedup) are shown below. The HPL benchmark is executed on 1-32 nodes on AWS and Azure resources.

### AWS

| Nodes | Cores | Rmax (TFlop/s) | Rpeak (TFlop/s) | Speedup | Ideal speedup | Speedup Ratio |
|:-----:|:-----:|:--------------:|:---------------:|:-------:|:-------------:|:-------------:|
|   1   |   36  |      0.53      |       1.63      |   1.00  |       1       |      1.00     |
|   2   |   72  |      0.98      |       3.26      |   1.85  |       2       |      0.93     |
|   4   |  144  |      1.51      |       6.53      |   2.87  |       4       |      0.72     |
|   8   |  288  |      2.90      |      13.05      |   5.50  |       8       |      0.69     |
|   16  |  576  |      5.23      |      26.10      |   9.92  |       16      |      0.62     |
|   32  |  1152 |      8.65      |      52.20      |  16.41  |       32      |      0.51     |

#### Performance

![AWS Performance](../images/aws-preformance.png "AWS Performance")

#### Speedup

![AWS Speedup](../images/aws-speedup.png "AWS Speedup")


### Azure

| Nodes | Cores | Rmax (TFlop/s) | Rpeak (TFlop/s) | Speedup | Ideal speedup | Speedup Ratio |
|:-----:|:-----:|:--------------:|:---------------:|:-------:|:-------------:|:-------------:|
|   1   |   16  |      0.48      |       0.6       |   1.00  |       1       |      1.00     |
|   2   |   32  |      0.87      |       1.2       |   1.82  |       2       |      0.91     |
|   4   |   64  |      1.49      |       2.4       |   3.14  |       4       |      0.78     |
|   8   |  128  |      3.04      |       4.8       |   6.38  |       8       |      0.80     |
|   16  |  256  |      5.33      |       9.6       |  11.18  |       16      |      0.70     |
|   32  |  512  |      10.53     |       19.2      |  22.11  |       32      |      0.69     |

#### Performance

![Azure Performance](../images/azure-preformance.png "Azure Performance")

#### Speedup

![Azure Speedup](../images/azure-speedup.png "Azure Speedup")

The following diagram shows the speedup ratio for AWS with Hyper-Threading enabled and Azure.

### Speedup Ratio

![Speedup Ratio](../images/speedup-ratio.png "Speedup Ratio")


## Links

- [HPL](http://www.netlib.org/benchmark/hpl)

- [HPL Calculator](http://hpl-calculator.sourceforge.net)
