# Entity Banks

Entity **Banks**, in the context of our Platform, are defined as [collections](/accounts/collections.md) of **unique** entity items, each representing a uniquely distinct physical material or sequence of logical operations. One Bank exists for each **Bankable entity type**, which for the moment consist in Materials and Workflows, but not Jobs. The corresponding list of entity items for that particular bankable type is then referred to  as the **Bank Entity Collection**. 

This concept of Bank collection should not be confused with any of the Account-owned Entity Collections: although the two types of collection communicate with each other as explained below, they remain distinct at all times.


# How Bank Entity Items are Generated

Any entity item of bankable type, created under an Account-owned Entity Collection within our platform, is **automatically** added to the corresponding Bank Entity Collection for that particular entity type. 

!!!note "Note: privacy of data stored in Banks"
    For accounts with private data and  [elevated service levels](/pricing/service-levels.md), the corresponding entries in the various Banks are private and only visible to the members of the account. For the rest - the bank entries are visible to all platform users. These privacy concepts are further explained in subsequent sections of this page. 

# Bank Mapping Function

Before being added to the relevant Bank Entity Collection, each entity item created by users under their Account-owned Entity Collection is first **checked** by a **Bank Mapping Function** (or function) against existing Bank entries, to make sure that the equivalent entry was not already present in the Bank Collection. In case of a positive match at the moment of comparison with existing Bank entries, the newly created entity being added to the Bank is automatically **merged** into the pre-existing entry.

To each entity type corresponds a distinct Mapping Function which inspects and assesses certain defining features of the entity, and this is explained in detail in the entity-specific Bank documentation pages cited in the final section of the present page. 

## Visual Representation

The correspondence between Account-owned and Bank entity collections, for the equivalent entity type, can be visualized as demonstrated in the example diagram below:

![Bank Diagram](/images/Bank-diagram-Mapping.png "Bank Diagram")

As the reader can notice from the above image, distinct Account-owned entity entries <i class="zmdi zmdi-close-circle-o zmdi-hc-border"></i> may end up corresponding to the same **unique** Bank entry <i class="zmdi zmdi-plus-circle-o zmdi-hc-border"></i> within the Bank entity collection domain on the right, after being operated upon by the Bank Mapping Function. As explained earlier, this happens when the underlying physical material, or flow of logical operations, is equivalent between all such interconnected entries.

The reader may refer to this [page](data.md) for an explanation of the structured data keywords contained in the image insets. It is worth noticing in particular that all corresponding interconnected Account-Bank entity items share the same "hash" keyword string, as explained in the forthcoming section.


## Hash Strings

Merging is in practice performed through the generation of **hash strings**, such as the example mentioned in [this previous page](data.md). When an Account-owned entity item is acted upon by the Bank Mapping Function during the process of its addition to the relevant Bank, the corresponding hash string is generated algorithmically by our platform. 

This hash is then compared to those of all entries contained already in the Bank Collection for the given entity type. In case of a positive match, the original Account-owned entity item is directly associated with the existing Bank item sharing the same hash string, without consequently the need to create a new duplicate Bank entry.


# Bank Data Privacy

## Private Bank Entities

If an Account has a sufficient service level that warrants the storage of private entity items in the Bank, the situation presented below might appear, whereby such private items are made accessible only to members of that Account and not to any other:

![Bank Diagram](/images/Bank-diagram-Private.png "Bank Diagram")

## Public Bank Entities

Alternatively, an Account might not have any elevated privacy settings as part of its service level, or even if it has, it might consensually want to make Bank entities accessible to the general public. In this case the scenario portrayed in the diagram below appears, whereby all other Accounts of the platform gain access to such Bank entities:

![Bank Diagram](/images/Bank-diagram-Public.png "Bank Diagram")

!!!note "Note: independent generation of same Bank entity item with different privacy settings"
    If distinct Accounts happen to generate different bankable entity items that end up sharing the same unique Bank representation, then if any of these Accounts makes the Bank entity publicly accessible to all users, this will nullify any other privacy options set by all other Accounts. 


# Summary

A summary  flowchart depicting all the above-mentioned  logical steps involved in the mapping and creation of entity items within the relevant Bank is illustrated in the image contained in the expandable section below: 

<details>
  <summary>
     Expand to view
  </summary> 
    
  ![Bank Diagram](/images/Bank-Flowchart.png "Bank Diagram")
  
  </details>
  

# Importing Entities from Bank

Following the creation of a Bank entity item, this item may be subsequently **imported** by any user with appropriate access to it, thus creating a copy of that item under the corresponding Account-owned entity collection.

Specific examples on how to operate this import procedure from the Bank repositories can be found for both [Materials](/materials/bank.md) and [Workflows](/workflows/bank.md) in their respective documentation pages, whereas the general instructions applicable to both entity types can be found [here](actions/copy-bank.md).
