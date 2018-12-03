# Detailed List of Jobs

To get detailed information about all the [jobs](../overview.md) submitted to date by the user on the [Command Line Interface](../../cli/overview.md) of our system, enter the `lsjob` command, as displayed in the example below. This information includes the relevant [compute parameters](../../infrastructure/compute/parameters.md) used as part of the job execution.

`# > lsjob`

```bash
Id JobId User     Project  Machine            Queue QualityOfService Stage   Charge Processors Nodes WallDuration StartTime           EndTime             Description
-- ----- -------- -------- ------------------ ----- ---------------- ------- ------ ---------- ----- ------------ ------------------- ------------------- -----------
28 75    christie christie cluster.exabyte.io batch GS               Charge    0.00 8                109          2016-08-11 01:36:58 2016-08-11 01:38:47
29 76    christie christie cluster.exabyte.io batch GS               Charge    0.01 16               71           2016-08-11 01:40:38 2016-08-11 01:41:49
30 77    christie christie cluster.exabyte.io batch GS               Charge    0.00 16               6            2016-08-11 02:24:38 2016-08-11 02:24:44
31 78    christie christie cluster.exabyte.io batch GS               Charge    0.00 16               5            2016-08-11 02:25:41 2016-08-11 02:25:46
32 79    christie christie cluster.exabyte.io batch GS               Charge    0.00 16               6            2016-08-11 02:25:57 2016-08-11 02:26:03
```

---
