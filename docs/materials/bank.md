# Materials Bank

We collect unique copies of all materials in a standard primitive representation [[1](#links)] in a central "Bank" collection. The general features of such Bank repositories are discussed in the following [general introductory page](/entities-general/bank.md). Advanced search functionality specific to the Materials Bank are further described [here](../entities-general/actions/advanced-search.md).

# Mapping Function

In the special case of materials, the [Bank Mapping Function](/entities-general/bank.md#bank-mapping-function) consists in first calculating the Niggli standard primitive representation of every candidate crystal structure originating from the Account-owned collections. 

From this Niggli representation, the corresponding ["hash" string](/entities-general/bank.md#hash-strings) is then calculated, and compared against those of existing Bank entries. From this point onwards, two alternative scenarios can emerge:

## Positive Match of Hash Strings

If a positive match of hash strings is encountered between the Account-owned candidate structure and an existing entry within the Materials Bank, then no new Bank entry is created. Rather, the Account-owned material is linked to the existing Bank entry with the same hash.

## No Match of Hash Strings

If no match is found, then a new Bank entry is created, under the same Niggli primitive representation as that of the candidate material. Future materials originating from all Accounts on the platform that share the same Niggli representation, and therefore the same hash, will then point to this new  Bank entry.

# Links

1. [Standard primitive representation: Niggli Cell](https://nvlpubs.nist.gov/nistpubs/sp958-lide/188-190.pdf)
