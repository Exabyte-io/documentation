# Registration of Jobs in Web Interface

By default, all jobs submitted from command line are propagated and registered automatically in the [Web Interface](../ui/overview.md) for user convenience. When jobs are registered in this way, their associated simulation files contained in the job's main [Working Directory](batch-scripts/directories.md) become accessible under the [Files Explorer Interface](../jobs/ui/files-tab.md) within the corresponding [Job Viewer page](../jobs/ui/viewer.md). 

If the user does not want the job to be shown on the Web Interface, he/she should specify the following [directive](batch-scripts/directives.md) inside the job script file.

```bash
#PBS -R n
```
