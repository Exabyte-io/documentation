# Structured Representation of Compute Parameters

Below we show an example JSON structured representation for the compute parameters introduced [here](ui.md). The keywords contained here are referenced in the ensuing table, where each entry can be clicked upon to retrieve its corresponding documentation explanation.

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

<center>
    
| Keyword    |  
| :-------- |
| [ppn](ui.md#nodes-/-ppn) |
| [nodes](ui.md#nodes-/-ppn) |  
| [queue](ui.md#queue)  |
| [timeLimit](ui.md#time-limit) |  
| [notify](ui.md#notifications) |
| [cluster](ui.md#cluster-choice) | 
| [arguments](ui.md#advanced-options) |

</center>
