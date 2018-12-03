# Specify Job Project

In order to specify a [project](../jobs/projects.md) that the job should belong to and should be [charged upon](../accounts/payments-charges.md), the following directive should be used in the [job script file](batch-scripts/sample-scripts.md). 

```
#PBS -A <Project Name>
```

Each user has a [default project](../jobs/projects.md#default-project) that jobs are charged on by default, unless this choice is modified with the directive.

For the case of [Organizational Accounts](../collaboration/organizations/overview.md), if no project is specified within the job script through the above-mentioned directive, then the [personal account](../collaboration/organizations/roles.md#organizations-vs.-personal-accounts) of the user will be charged upon, under the default project.

## Register Jobs in Web Interface

By default, all jobs submitted from command line are registered in the [Web Interface](../ui/overview.md) for user convenience. When jobs are registered in this way, their files become accessible under the [Files Explorer Interface](../jobs/ui/files-tab.md) within the corresponding [Job Viewer page](../jobs/ui/viewer.md). 

If the user does not want the job to be shown on the Web Interface, he/she should specify the `#PBS -R n` directive inside the job script file.
