# Structured Representation of Jobs

**Job** is a "container" entity that is used to organize the data and track resource allocation. The terminology and naming is common for distributed resource allocation management. A job, in the computational sense, represents the simplest entity that has accounting set up for, and can have one or more [Materials](/materials/overview.md) and [Workflows](/workflows/overview.md) associated with it. 

Jobs can be nested and chained as necessary.

# Example representation

In order to organize and store the information about Jobs we employ [Exabyte Data Convention](/data/convention/overview.md), as explained [elsewhere](/entities-general/data.md) in this documentation.

Below is an example JSON structured representation a of a Job. It contains a single Workflow and one Material.

```json
{
    "name" : "Test Job",
    "version" : "0.2.0",
    "_material" : {
        "_id" : "FJHNZCixeNfopuLrA",
        "exabyteId" : "e3nJ9g7tLaARSA25g"
    },
    "workflow" : {
        ...
    },
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
    "_project" : {
        "_id" : "ypijc9N27BixEpKfT",
    },
    "status" : "finished",
    "createdAt" : "2017-10-17T18:20:53.975Z",
    "updatedAt" : "2017-10-17T18:22:31.389Z"
}
```

# Explanation of Keywords

## Top-level Keywords

| Keyword    |   Description      |  
| :-------- |:----------- |
| _material |  Link to the identifiers of [material(s)](/materials/data.md) for this job   | 
| workflow |  Content of the [Workflow](/workflows/data/data.md) for this job | 
| compute | Computational parameters for this job. See separate table below. |
| _project  | Link to the identifier of the [project](projects.md) containing the job  |
| status |   Indication of the current [status](status.md) of the job |  

## The "compute" Keyword
    
| Keyword    |   Description      |  
| :-------- |:----------- |
| ppn |  The number of processors per node   | 
| nodes |  The number of computing nodes dedicated to the job execution | 
| queue | Type of queue on which job is being submitted |
| timeLimit  | The maximum duration of time that the job can be executed for  |
| notify | Enable the sending of notifications on the job status to the user   | 
| cluster | Please refer to the table contained [in this section](/accounts/ui/charges-payments.md#advanced-search) for an explanation of the "jid" and  "fqdn" (Fully Qualified Domain Name) keywords in the context of clusters | 
| arguments | Extra arguments  | 

!!!note "Note: explanation of clusters-related terms"
    The user is referred to [this page](/compute/setup.md) for instructions on how to operate the supercomputing [clusters](/pricing/service-levels.md#clusters-and-premium-hardware) offered on our platform. The concept of [Queue](/compute/levels-queues.md) on the  cluster is also explained in its respective page.
