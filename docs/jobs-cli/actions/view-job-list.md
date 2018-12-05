# Detailed List of Jobs and Charges

To get detailed information about all the [jobs](../overview.md) [submitted](../overview.md) **to date** by the user on the [Command Line Interface](../../cli/overview.md) (CLI) of our system, the `lsjob` command should be entered, as displayed in the example below.
 
This information includes the relevant [compute parameters](../../infrastructure/compute/parameters.md) used as part of the job execution, as well as the [Project](../../jobs/projects.md) container and [Account Charges](../../accounts/payments-charges.md) incurred by each listed Job. Here, the Jobs are referenced by their **"Job IDs"**, as well as by their IDs attributed by the accounting system. 

`# > lsjob`

```
Id JobId                                                    User     Project  Machine            Queue QualityOfService Stage   Charge Processors Nodes WallDuration StartTime           EndTime             Description
-- -------------------------------------------------------- -------- -------- ------------------ ----- ---------------- ------- ------ ---------- ----- ------------ ------------------- ------------------- -----------
28 814.master-production-20160630-cluster-007.exabyte.io    christie christie cluster.exabyte.io batch GS               Charge    0.00 8                109          2016-08-11 01:36:58 2016-08-11 01:38:47
29 815.master-production-20160630-cluster-007.exabyte.io    christie christie cluster.exabyte.io batch GS               Charge    0.01 16               71           2016-08-11 01:40:38 2016-08-11 01:41:49
30 816.master-production-20160630-cluster-007.exabyte.io    christie christie cluster.exabyte.io batch GS               Charge    0.00 16               6            2016-08-11 02:24:38 2016-08-11 02:24:44
31 817.master-production-20160630-cluster-007.exabyte.io    christie christie cluster.exabyte.io batch GS               Charge    0.00 16               5            2016-08-11 02:25:41 2016-08-11 02:25:46
32 818.master-production-20160630-cluster-007.exabyte.io    christie christie cluster.exabyte.io batch GS               Charge    0.00 16               6            2016-08-11 02:25:57 2016-08-11 02:26:03
```

The full documentation manual for the accounting system software that we implement under the CLI, called **"Gold"**, can be found under Ref. [^1]. 

## Links

[^1]: [Gold User’s Guide, Document](http://docs.adaptivecomputing.com/gold/pdf/GoldUserGuide.pdf)
