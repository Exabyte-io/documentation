# Introduction

**Job** is a "container" entity that is used to organize the data and track resource allocation. The terminology and naming is common for distributed resource allocation management. A job in the computational sense represents the simplest entity that has accounting set up for, and can have one or more [Materials](/materials/overview.md) and [Workflows](/workflows/overview.md) associated with it. 

Jobs can be nested and chained as necessary.

# Projects

Jobs are organized into **Projects** for convenience. One can think about projects as collections of jobs in the same manner as a file system directory is a collection of files.

# Example representation

In order to organize and store the information about Jobs we employ [Exabyte Data Convention](/data/overview.md) as explained elsewhere in this documentation.

Below is an example JSON representation a of a job. It contains a single Workflow and one Material:

```json
{
    "name" : "Test Job",
    // version of the current document schema
    "version" : "0.2.0",
    // "link" to material(s) for this job
    "_material" : {
        "_id" : "FJHNZCixeNfopuLrA",
        "exabyteId" : "e3nJ9g7tLaARSA25g"
    },
    // content of the "Workflow"
    "workflow" : {
        ...
    },
    // computational parameters for this job
    "compute" : {
        "ppn" : 1,
        "nodes" : 1,
        "queue" : "D",
        "timeLimit" : "01:00:00",
        "notify" : "n",
        "cluster" : {
            "fqdn" : "master-production-20160630-cluster-001.exabyte.io",
            "jid" : "31507.master-production-20160630-cluster-001.exabyte.io"
        },
        "arguments" : {}
    },
    // "link" to the project the job belongs to
    "_project" : {
        "_id" : "ypijc9N27BixEpKfT",
    },
    "status" : "finished",
    "createdAt" : "2017-10-17T18:20:53.975Z",
    "updatedAt" : "2017-10-17T18:22:31.389Z"
}
```
> Note: JSON does not support inclusion of inline commentaries, we only left them above for clarity.


# Job Statuses

Job statuses as shown in the web application are explained in the table below:

| Label    |      Meaning  |
|----------|:--------------|
<span class="">pre-submission</span> | job is created and saved in database
<span class="">submitted</span> | job is scheduled for execution
<span class="">active</span> | job is currently running
<span class="">finished</span> | job finished successfully
<span class="">error</span> | something went wrong with job execution
<span class="">timeout</span> | job exceeded allocated time limit
<span class="">terminated</span> | job is terminated by user