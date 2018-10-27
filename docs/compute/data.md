<!-- TODO: GM to revise/add content -->

# Example Representation

```json
{
    "ppn" : 1,
    "nodes" : 1,
    "queue" : "D",
    "timeLimit" : "01:00:00",
    "notify" : "n",
    "cluster" : {
        "fqdn" : "master-production-20160630-cluster-001.exabyte.io",
        "jid" : "31507.master-production-20160630-cluster-001.exabyte.io"
    },
    "arguments" : {
        "npools": 1,    
    }
}
```

# The "compute" Keyword
    
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
