# Compute Structured Representation

Below we show an example JSON structured representation for the compute parameters introduced [here](ui.md). The keywords contained here are further explained in the ensuing table.

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

## List of Keywords
    
| Keyword    |   Description      |  
| :-------- |:----------- |
| ppn |  The number of processors per node   | 
| nodes |  The number of computing nodes dedicated to the job execution | 
| queue | Type of [queue](../resource/queues.md) on which job is being submitted |
| timeLimit  | The maximum duration of time that the job can be executed for  |
| notify | Enable the sending of notifications on the job status to the user  | 
| cluster | Please refer to the table contained [in this section](../../accounts/ui/charges-payments.md#advanced-search) for an explanation of the "jid" and  "fqdn" (Fully Qualified Domain Name) keywords in the context of [clusters](../clusters/overview.md) | 
| arguments | Extra arguments  | 
