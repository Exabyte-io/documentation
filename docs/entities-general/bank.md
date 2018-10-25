# Entity Bank

Entity **Bank** is a [collections](/accounts/collections.md) of **unique** entity items. One Bank exists for each **Bankable [Entity](overview.md)**. The corresponding list of entities is then referred to as the **Bank Entity Collection**. 

For [accounts](/accounts/overview.md) with [service levels](/pricing/service-levels.md) allowing for private data, the Bank items are private and only visible to the members of the account. For the rest - the Bank entries are visible to all platform users. These privacy notions are further explained in subsequent sections of this page. 
  
 Bankable Entities for the moment consist of Materials and Workflows.

# How Bank Entities are Generated

Any entity item of bankable type is **automatically** added to the corresponding Bank collection using the procedure further described below.

# Mapping Function

After creation, the new Bankable Entity is **checked** by a **Bank Mapping Function** against existing Bank entries, to make sure that it is unique. In case of a positive match, the entity is **merged** into the pre-existing one. The correspondence is established through the **hash** string (the output of the mapping function) as explained below.

Each entity type has a different Mapping Function. It assesses certain defining features of the entity, as explained for the case of [Materials](/materials/bank.md) and [Workflows](/workflows/bank.md) separately. 

## Visual Representation

The correspondence between the Entity and Bank entity collections is visualized below:

![Bank Diagram](/images/Bank-diagram-Mapping.png "Bank Diagram")

Distinct Account-owned entities <i class="zmdi zmdi-close-circle-o"></i> may end up corresponding to the same **unique** Bank entry <i class="zmdi zmdi-plus-circle-o"></i>. As mentioned earlier, this happens when the underlying Bankable Entities produce the same output for the Mapping Function.

The reader may refer to this [page](data.md) for an explanation of the structured data keywords contained in the image insets. It is worth noticing that interconnected entity items share the same "hash" keyword string, as explained in the forthcoming section.

## Hash Strings

The output of the mapping function is a **hash string**. This hash is stored inside each new Bankable Entity and compared to the pre-existing ones in the Bank collection. In case of a positive match, the entities are associated together, thus preventing the creation of duplicates.


# Entity Privacy

## Private 

If an Account has a sufficient [service level](/pricing/service-levels.md) allowing for private data, the situation displayed below will appear, whereby private items are accessible only to the Account members:

![Bank Diagram](/images/Bank-diagram-Private.png "Bank Diagram")

## Public 

Alternatively, the lack of data privacy leads to the following scenario, whereby all other Accounts gain access to the Bank entities.

![Bank Diagram](/images/Bank-diagram-Public.png "Bank Diagram")

> NOTE: If different Accounts happen to generate exactly the same Bank Entity, the privacy settings are nullified if any of these Accounts makes the Entity public.


# Flowchart/Summary

A summary depicting the above steps involved in the creation of Bank entities can be found in the expandable section below: 

<details>
  <summary>
     Expand to view
  </summary> 
    
  ![Bank Diagram](/images/Bank-Flowchart.png "Bank Diagram")
  
  </details>
  

# Importing Entities from Bank

Bank entities may be **imported** by users with appropriate access to it. This creates a copy of that item under the Account-owned collection.

Specific examples of the importing procedure can be found for both [Materials](/materials/bank.md) and [Workflows](/workflows/bank.md), whereas the general instructions are presented [here](actions/copy-bank.md).
