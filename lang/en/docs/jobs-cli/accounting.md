# Accounting

We describe here the [accounting](../accounts/overview.md) aspects which are particularly relevant in the context of [Job Submission via CLI](overview.md).

## Job Project Specification

In order to specify a [project](../jobs/projects.md) that the job should belong to and should be [charged upon](../accounts/payments-charges.md), the following [resource management directive](batch-scripts/directives.md) should be used within the job's corresponding [batch script file](batch-scripts/overview.md). 

```bash
#PBS -A <Project Name>
```

Each user has a [default project](../jobs/projects.md#default-project) that jobs are charged on by default, unless this choice is modified with the above directive.

For the case of [Organizational Accounts](../collaboration/organizations/overview.md), if no project is specified within the batch script, then the [personal account](../collaboration/organizations/roles.md#organizations-vs.-personal-accounts) of the user will be charged upon under its default project.

!!! warning "Remember to specify job project for organizational accounts"
    Please remember to always specify the job project explicitly for organizational accounts. Otherwise the personal account will be charged, and/or (if there is not enough balance) the jobs might be removed from scheduling. 

## Registration of Jobs in Web Interface

We explain how jobs submitted via CLI can be transmitted and registered in the [Web Interface](../ui/overview.md) of our platform in a [dedicated Tutorial](../tutorials/jobs-cli/job-cli-example.md).

## Check Account Balance and Quota

The [balance](../accounts/balance.md) and [storage quota](../accounts/quota.md) for the [Account](../accounts/overview.md) under consideration can be inspected via CLI by following the instructions contained [in this page](../cli/actions/balance-quota.md).

## View List of Jobs and Charges

The complete list of jobs executed by the user to date via CLI can be retrieved [as follows](actions/view-job-list.md).
