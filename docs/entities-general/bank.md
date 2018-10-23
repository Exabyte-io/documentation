# Entity Banks

Entity **Banks** are defined as [collections](/accounts/collections.md) of **unique** entity items, each representing a distinct material or workflow sequence of logical operations. One Bank exists for each **Bankable entity type**, which for the moment consist in Materials and Workflows (but not Jobs). The corresponding list of entities is then referred to  as the **Bank Entity Collection**. 

This concept should not be confused with the Account-owned Entity Collection: although the two collections communicate with each other as explained below, they remain separate.


# How Bank Entities are Generated

Any entity item of bankable type, created under an Account-owned collection, is **automatically** added to the corresponding Bank collection. 

!!!note "Note: privacy of data stored in Banks"
    For accounts with private data and  [elevated service levels](/pricing/service-levels.md), the Bank items are private and only visible to the members of the account. For the rest - the Bank entries are visible to all platform users. These privacy notions are further explained in subsequent sections of this page. 

# Mapping Function

An entity item created under an Account-owned collection is first **checked** by a **Bank Mapping Function** against existing Bank entries, to make sure that it is unique within the Bank collection. In case of a positive match, the entity is **merged** into the pre-existing Bank entry.

Each entity type has a different Mapping Function. It assesses certain defining features of the entity, as explained for the case of [Materials](/materials/bank.md) and [Workflows](/workflows/bank.md) separately. 

## Visual Representation

The correspondence between Account and Bank entity collections can be visualized as shown below:

![Bank Diagram](/images/Bank-diagram-Mapping.png "Bank Diagram")

Distinct Account-owned entities <i class="zmdi zmdi-close-circle-o zmdi-hc-border"></i> may end up corresponding to the same **unique** Bank entry <i class="zmdi zmdi-plus-circle-o zmdi-hc-border"></i> within the domain on the right. As mentioned earlier, this happens when the underlying material, or flow of logical operations, is equivalent between interconnected entries.

The reader may refer to this [page](data.md) for an explanation of the structured data keywords contained in the image insets. It is worth noticing that interconnected entity items share the same "hash" keyword string, as explained in the forthcoming section.


## Hash Strings

Merging of Bank entity items is performed through the generation of **hash strings**. When an Account-owned entity item is acted upon by the Mapping Function, the corresponding hash string is generated algorithmically by our platform. 

This hash is then compared to the pre-existing ones in the Bank collection. In case of a positive match, the entities are associated together, thus preventing the creation of duplicates.


# Entity Privacy

## Private 

If an Account has a sufficient [service level](/pricing/service-levels.md), the situation displayed below might appear, whereby private items are accessible only to the Account members:

![Bank Diagram](/images/Bank-diagram-Private.png "Bank Diagram")

## Public 

Alternatively, the lack of data privacy leads to the following scenario, whereby all other Accounts gain access to the Bank entities:

![Bank Diagram](/images/Bank-diagram-Public.png "Bank Diagram")

!!!note "Note: independent generation of same Bank entity with different privacy settings"
    If different Accounts happen to generate the same Bank representation for an entity, privacy settings are nullified if any of these Accounts makes it public. 


# Summary

A summary depicting the above steps involved in the creation of Bank entities can be found in the expandable section below: 

<details>
  <summary>
     Expand to view
  </summary> 
    
  ![Bank Diagram](/images/Bank-Flowchart.png "Bank Diagram")
  
  </details>
  

# Importing Entities from Bank

Bank entities may be **imported** by users with appropriate access to it. This creates a copy of that item under the Account-owned  collection.

Specific examples of the importing procedure can be found for both [Materials](/materials/bank.md) and [Workflows](/workflows/bank.md), whereas the general instructions are presented [here](actions/copy-bank.md).
