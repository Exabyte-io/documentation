# Registration of Jobs in Web Interface

By default, all [jobs submitted](../../jobs-cli/overview.md) from the [Command Line Interface](../../cli/overview.md) (CLI) of our platform are propagated and registered automatically in the [Web Interface](../../ui/overview.md) for user convenience. 

When jobs are registered in this way, their associated simulation files contained in the job's main [Working Directory](../../jobs-cli/batch-scripts/directories.md) become accessible under the [Files Explorer Interface](../../jobs/ui/files-tab.md) within the corresponding [Job Viewer page](../../jobs/ui/viewer.md). 

If the user does not want the job to be shown on the Web Interface, he/she should specify the following [directive](../../jobs-cli/batch-scripts/directives.md) inside the corresponding [job script file](../../jobs-cli/batch-scripts/overview.md).

```bash
#PBS -R n
```

## Animation

In the animation below, we follow upon the outcome of the [previous tutorial](job-cli-example.md), where we provided an example on how to launch a [simulation job via CLI](../../jobs-cli/overview.md).
 
Here, we begin by exiting the [Web Terminal](../../remote-connection/web-terminal.md) with which the Job was launched, and we inspect the evolution of the Job under [Web Interface](../../ui/overview.md) as it is executed by opening its entry within the [Jobs Explorer Interface](../../jobs/ui/explorer.md) of the [Default Project Page](../../jobs/ui/project-page.md). The job is executed under the [Default project](../../jobs/projects.md#default-project) of the [Account](../../accounts/overview.md) under consideration because no project name was specified when the job's [Batch Script](../../jobs-cli/batch-scripts/overview.md) was first created.

When the job is finally terminated, its corresponding simulation files are reviewed under the [Files Tab](../../jobs/ui/files-tab.md) of the [Job Viewer Interface](../../jobs/ui/viewer.md). Each file listed here can be [downloaded](../../data-in-objectstorage/actions/download.md) to the user's local disk by clicking upon the relevant entries in turn.

<div class="video-wrapper">
<iframe class="gifffer" width="100%" height="100%" src="https://www.youtube.com/embed/MBpd-yKUCM4&start=10&end=110" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

