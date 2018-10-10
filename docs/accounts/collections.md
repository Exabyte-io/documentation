# Collections

The term "Collection", in the context of our platform, refers to the broad concept of a **database of items**, whereby such items can be of any general type. These databases, together with all the different items that they contain, are collectively stored in the back-end of our platform using MongoDB [[1](#links)], a document-oriented database program which uses JSON-like documents with schemata. 

The "front-end" of these collections, or in other words the way the users can visualize and interact graphically with such databases as lists of items on our platform, can typically be accessed via the general [Explorer](/entities-general/ui/explorer.md) component of the User Interface. 

# Account-Owned Entity Collections

Each Account owns a set of distinct collections corresponding to each type of entity that exists on our platform, that is "Materials", "Workflows" and "Jobs". The reader is referred to the [general introduction](/entities-general/overview.md) to the concept of entities for a thorough explanation of all the features and properties that pertain to them. 

# Bank Entity Collections

As we explain in their [dedicated documentation page](/entities-general/bank.md), we classify Banks as a special type of Account in its own right. As such, all "bankable" entities (namely Materials and Workflows, but not Jobs for the moment) are stored inside their respective Bank databases as distinct "Bank Collections".

# Auxiliary Collections

Due to its wide scope of applicability, the concept of Collections is not restricted to entities only, but rather may be applied to numerous other types of item databases present across the entirety of the Exabyte platform, such as the collection of [Pseudopotentials](/methods/pseudopotential/overview.md) available for computation.

# Rest API 

Entity collections can also be accessed via the Rest API, as explained [here](/rest-api/overview.md). 

# Links

1. [MongoDB Atlas Database as a Service, Website](https://www.mongodb.com/)
