# Check Account Quota and Balance

This page explains how to retrieve [accounting information](../accounts/overview.md) for users logged-in via the [Command Line Interface](../cli/overview.md), including information about any [Organizational Accounts](../collaboration/organizations/overview.md) that the user is member of.
 
Each of the commands outlined in what follows can accept keyword parameters as option flags, as listed by passing the `--help` flag to them. The full documentation manual for the accounting system software that we implement can be found under Ref. [^1]. 

## Account Balance

Information about the [Account Balance](../accounts/balance.md) (in US dollars) is accessed using the `balance` command, as demonstrated in the example below.

`# > balance`

```bash
Id Name     Amount Reserved Balance CreditLimit Available
-- -------- ------ -------- ------- ----------- ---------
1  steven  1000.00     10.00 990.00        0.00   990.00
```

The entries returned by the above command are summarized in the table below, complementing their [general discussion](../accounts/balance.md). We remind the reader that in order to perform computations on our platform, a positive balance is required.


| Entry | Description |
|------|---------|
| Amount | Total combined amount of money |
| Reserved | Money already allocated for executing Jobs |
| Available | Remaining money not allocated yet |
| Credit Limit | Not applicable in our case |
| Balance | Same as Available, due to absence of credits | 


## Itemized Account Statement

We track the **usage** of our platform, or [balance](../accounts/balance.md) spent on computations per each [account](../accounts/overview.md) and each [project](../jobs/projects.md). The usage statistics of each [cluster](../infrastructure/clusters/overview.md), in terms of number of CPU hours consumed and charges incurred, is referred to as the **Account Statement**.

This statement can be inspected with the `statement` command under CLI, as demonstrated in the example below.

`# > statement`

```bash
################################################################################
#
# Statement for user steven
# Includes account 2 (steven)
# Generated on Wed Feb 11 16:00:34 2016.
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
Account Deposit       1000.00 2016-08-06 09:29:14

############################### Debit Detail ###################################

Object Action JobId Project  User     Machine            Amount Time
------ ------ ----- -------- -------- ------------------ ------ -------------------
Job    Charge 15    steven   steven   cluster.exabyte.io  -0.00 2016-08-08 04:09:51
Job    Charge 16    steven   steven   cluster.exabyte.io  -0.00 2016-08-08 04:10:35
Job    Charge 17    steven   steven   cluster.exabyte.io  -0.00 2016-08-08 04:28:08
Job    Charge 18    steven   steven   cluster.exabyte.io  -0.00 2016-08-08 04:28:21
Job    Charge 28    steven   steven   cluster.exabyte.io  -0.01 2016-08-08 06:48:42
Job    Charge 30    steven   steven   cluster.exabyte.io  -0.03 2016-08-08 09:53:29
Job    Charge 31    steven   steven   cluster.exabyte.io  -0.40 2016-08-08 12:25:53
Job    Charge 42    steven   steven   cluster.exabyte.io  -0.01 2016-08-09 14:13:29
Job    Charge 44    steven   steven   cluster.exabyte.io  -0.07 2016-08-09 14:21:25
Job    Charge 45    steven   steven   cluster.exabyte.io  -0.05 2016-08-09 14:23:33
Job    Charge 46    steven   steven   cluster.exabyte.io  -0.01 2016-08-09 14:28:13
Job    Charge 66    steven   steven   cluster.exabyte.io  -0.01 2016-08-10 08:46:56
Job    Charge 67    steven   steven   cluster.exabyte.io  -0.01 2016-08-10 08:50:09
Job    Charge 68    steven   steven   cluster.exabyte.io  -0.02 2016-08-10 08:53:15
Job    Charge 69    steven   steven   cluster.exabyte.io  -0.03 2016-08-10 09:02:38
Job    Charge 70    steven   steven   cluster.exabyte.io  -0.03 2016-08-10 09:33:31
Job    Charge 71    steven   steven   cluster.exabyte.io  -0.03 2016-08-10 12:00:42
Job    Charge 76    steven   steven   cluster.exabyte.io  -0.01 2016-08-11 01:41:50
Job    Charge 81    steven   steven   cluster.exabyte.io  -0.01 2016-08-11 02:28:48
Job    Charge 83    steven   steven   cluster.exabyte.io  -0.01 2016-08-11 03:54:15
Job    Charge 84    steven   steven   cluster.exabyte.io  -0.01 2016-08-11 03:56:04
Job    Charge 85    steven   steven   cluster.exabyte.io  -0.01 2016-08-11 03:58:12
Job    Charge 86    steven   steven   cluster.exabyte.io  -0.03 2016-08-11 05:34:53
Job    Charge 87    steven   steven   cluster.exabyte.io  -0.01 2016-08-11 05:44:15
Job    Charge 88    steven   steven   cluster.exabyte.io  -0.01 2016-08-11 06:56:45
Job    Charge 89    steven   steven   cluster.exabyte.io  -0.09 2016-08-11 07:01:45
Job    Charge 92    steven   steven   cluster.exabyte.io  -0.01 2016-08-11 11:57:44

############################### End of Report ##################################

```

It is often convenient to pass the `-s` (start) and `-e` (end) flags to the `statement` command, to narrow down the window of time over which the statement is printed. These flags should contain information about the delimiting dates, in the format "YYYY-MM-DD". So, for example, the command `statement -s 2017-01-08 -e 2018-01-08` would return the account statement during the course of a year, starting from the 8th of January 2017. 

The full list of flags that can be passed to `statement` is reproduced below for reference purposes.

```bash
# > statement --help

Usage:
    gstatement [[-a] *account_id*] [-p *project_name*] [-u *user_name*] [-m
    *machine_name*] [-s *start_time*] [-e *end_time*] [--summarize] [-h,
    --hours] [--debug] [-?, --help] [--man] [-V, --version]
```

## Detailed List of Jobs

To get detailed information about all the jobs submitted on our system to date, enter the `lsjob` command.

`# > lsjob`

```bash
Id JobId User     Project  Machine            Queue QualityOfService Stage   Charge Processors Nodes WallDuration StartTime           EndTime             Description
-- ----- -------- -------- ------------------ ----- ---------------- ------- ------ ---------- ----- ------------ ------------------- ------------------- -----------
28 75    christie christie cluster.exabyte.io batch GS               Charge    0.00 8                109          2016-08-11 01:36:58 2016-08-11 01:38:47
29 76    christie christie cluster.exabyte.io batch GS               Charge    0.01 16               71           2016-08-11 01:40:38 2016-08-11 01:41:49
30 77    christie christie cluster.exabyte.io batch GS               Charge    0.00 16               6            2016-08-11 02:24:38 2016-08-11 02:24:44
31 78    christie christie cluster.exabyte.io batch GS               Charge    0.00 16               5            2016-08-11 02:25:41 2016-08-11 02:25:46
32 79    christie christie cluster.exabyte.io batch GS               Charge    0.00 16               6            2016-08-11 02:25:57 2016-08-11 02:26:03
33 80    christie christie cluster.exabyte.io batch GS               Charge    0.00 16               6            2016-08-11 02:26:22 2016-08-11 02:26:28
34 81    christie christie cluster.exabyte.io batch GS               Charge    0.01 16               70           2016-08-11 02:27:37 2016-08-11 02:28:47
35 82    christie christie cluster.exabyte.io batch GS               Charge    0.00 16               6            2016-08-11 03:28:55 2016-08-11 03:29:01
36 83    christie christie cluster.exabyte.io batch GS               Charge    0.01 16               75           2016-08-11 03:52:59 2016-08-11 03:54:14
37 84    christie christie cluster.exabyte.io batch GS               Charge    0.01 16               72           2016-08-11 03:54:51 2016-08-11 03:56:03
38 85    christie christie cluster.exabyte.io batch GS               Charge    0.01 16               69           2016-08-11 03:57:02 2016-08-11 03:58:11
39 86    christie christie cluster.exabyte.io batch GO               Charge    0.03 16               72           2016-08-11 05:33:39 2016-08-11 05:34:51
40 87    christie christie cluster.exabyte.io batch GS               Charge    0.01 16               71           2016-08-11 05:43:03 2016-08-11 05:44:14
41 88    christie christie cluster.exabyte.io batch GS               Charge    0.01 16               70           2016-08-11 06:55:34 2016-08-11 06:56:44
42 89    christie christie cluster.exabyte.io batch GO               Charge    0.09 32               96           2016-08-11 07:00:08 2016-08-11 07:01:44
```

---

## Storage Quota

Information about the [Storage Quota](../accounts/quota.md) within the available [computing clusters](../infrastructure/clusters/overview.md) can be retrieved via the `quota` command.

<!-- TODO:
Wait for Mohammed to fix this command to show example of output
-->

## Links

[^1]: [Gold User’s Guide, Document](http://docs.adaptivecomputing.com/gold/pdf/GoldUserGuide.pdf)
