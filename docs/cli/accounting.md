# Accounting
---
This page explains how to retrieve accounting information for users logged-in via command line.

## Total remaining allocation

`# > gbalance`

```bash
Id Name     Amount Reserved Balance CreditLimit Available
-- -------- ------ -------- ------- ----------- ---------
1  steven  1000.00     0.00 1000.00        0.00   1000.00
```

The information above shows:

- username (*Name*) for the
- the allocation *Amount* in US dollars,
- *Reserved* amount reserved for the currently running jobs,
- *Balance* available to the user,
- *CreditLimit* illustrating how much credit user has with exabyte.io
- *Available* amount allocated for the current user (for team allocations)


## Itemized account statement

Example belows shows how to view the account statement since the beginning of time

`# > statement`

```bash
################################################################################
#
# Statement for user steven
# Includes account 2 (steven)
# Generated on Wed Feb 11 16:00:34 2015.
# Reporting account activity from -infinity to now.
#
################################################################################

Beginning Balance:                 0.00
------------------ --------------------
Total Credits:                  1000.00
Total Debits:                     -0.91
------------------ --------------------
Ending Balance:                  999.09

############################### Credit Detail ##################################

Object  Action  JobId Amount  Time
------- ------- ----- ------- -------------------
Account Deposit       1000.00 2015-02-06 09:29:14

############################### Debit Detail ###################################

Object Action JobId Project  User     Machine            Amount Time
------ ------ ----- -------- -------- ------------------ ------ -------------------
Job    Charge 15    steven   steven   cluster.exabyte.io  -0.00 2015-02-08 04:09:51
Job    Charge 16    steven   steven   cluster.exabyte.io  -0.00 2015-02-08 04:10:35
Job    Charge 17    steven   steven   cluster.exabyte.io  -0.00 2015-02-08 04:28:08
Job    Charge 18    steven   steven   cluster.exabyte.io  -0.00 2015-02-08 04:28:21
Job    Charge 28    steven   steven   cluster.exabyte.io  -0.01 2015-02-08 06:48:42
Job    Charge 30    steven   steven   cluster.exabyte.io  -0.03 2015-02-08 09:53:29
Job    Charge 31    steven   steven   cluster.exabyte.io  -0.40 2015-02-08 12:25:53
Job    Charge 42    steven   steven   cluster.exabyte.io  -0.01 2015-02-09 14:13:29
Job    Charge 44    steven   steven   cluster.exabyte.io  -0.07 2015-02-09 14:21:25
Job    Charge 45    steven   steven   cluster.exabyte.io  -0.05 2015-02-09 14:23:33
Job    Charge 46    steven   steven   cluster.exabyte.io  -0.01 2015-02-09 14:28:13
Job    Charge 66    steven   steven   cluster.exabyte.io  -0.01 2015-02-10 08:46:56
Job    Charge 67    steven   steven   cluster.exabyte.io  -0.01 2015-02-10 08:50:09
Job    Charge 68    steven   steven   cluster.exabyte.io  -0.02 2015-02-10 08:53:15
Job    Charge 69    steven   steven   cluster.exabyte.io  -0.03 2015-02-10 09:02:38
Job    Charge 70    steven   steven   cluster.exabyte.io  -0.03 2015-02-10 09:33:31
Job    Charge 71    steven   steven   cluster.exabyte.io  -0.03 2015-02-10 12:00:42
Job    Charge 76    steven   steven   cluster.exabyte.io  -0.01 2015-02-11 01:41:50
Job    Charge 81    steven   steven   cluster.exabyte.io  -0.01 2015-02-11 02:28:48
Job    Charge 83    steven   steven   cluster.exabyte.io  -0.01 2015-02-11 03:54:15
Job    Charge 84    steven   steven   cluster.exabyte.io  -0.01 2015-02-11 03:56:04
Job    Charge 85    steven   steven   cluster.exabyte.io  -0.01 2015-02-11 03:58:12
Job    Charge 86    steven   steven   cluster.exabyte.io  -0.03 2015-02-11 05:34:53
Job    Charge 87    steven   steven   cluster.exabyte.io  -0.01 2015-02-11 05:44:15
Job    Charge 88    steven   steven   cluster.exabyte.io  -0.01 2015-02-11 06:56:45
Job    Charge 89    steven   steven   cluster.exabyte.io  -0.09 2015-02-11 07:01:45
Job    Charge 92    steven   steven   cluster.exabyte.io  -0.01 2015-02-11 11:57:44

############################### End of Report ##################################

```


## Detailed list of jobs

`# > lsjob`

```bash
Id JobId User     Project  Machine            Queue QualityOfService Stage   Charge Processors Nodes WallDuration StartTime           EndTime             Description
-- ----- -------- -------- ------------------ ----- ---------------- ------- ------ ---------- ----- ------------ ------------------- ------------------- -----------
28 75    christie christie cluster.exabyte.io batch GS               Charge    0.00 8                109          2015-02-11 01:36:58 2015-02-11 01:38:47
29 76    christie christie cluster.exabyte.io batch GS               Charge    0.01 16               71           2015-02-11 01:40:38 2015-02-11 01:41:49
30 77    christie christie cluster.exabyte.io batch GS               Charge    0.00 16               6            2015-02-11 02:24:38 2015-02-11 02:24:44
31 78    christie christie cluster.exabyte.io batch GS               Charge    0.00 16               5            2015-02-11 02:25:41 2015-02-11 02:25:46
32 79    christie christie cluster.exabyte.io batch GS               Charge    0.00 16               6            2015-02-11 02:25:57 2015-02-11 02:26:03
33 80    christie christie cluster.exabyte.io batch GS               Charge    0.00 16               6            2015-02-11 02:26:22 2015-02-11 02:26:28
34 81    christie christie cluster.exabyte.io batch GS               Charge    0.01 16               70           2015-02-11 02:27:37 2015-02-11 02:28:47
35 82    christie christie cluster.exabyte.io batch GS               Charge    0.00 16               6            2015-02-11 03:28:55 2015-02-11 03:29:01
36 83    christie christie cluster.exabyte.io batch GS               Charge    0.01 16               75           2015-02-11 03:52:59 2015-02-11 03:54:14
37 84    christie christie cluster.exabyte.io batch GS               Charge    0.01 16               72           2015-02-11 03:54:51 2015-02-11 03:56:03
38 85    christie christie cluster.exabyte.io batch GS               Charge    0.01 16               69           2015-02-11 03:57:02 2015-02-11 03:58:11
39 86    christie christie cluster.exabyte.io batch GO               Charge    0.03 16               72           2015-02-11 05:33:39 2015-02-11 05:34:51
40 87    christie christie cluster.exabyte.io batch GS               Charge    0.01 16               71           2015-02-11 05:43:03 2015-02-11 05:44:14
41 88    christie christie cluster.exabyte.io batch GS               Charge    0.01 16               70           2015-02-11 06:55:34 2015-02-11 06:56:44
42 89    christie christie cluster.exabyte.io batch GO               Charge    0.09 32               96           2015-02-11 07:00:08 2015-02-11 07:01:44
```

---
