# Materials Bank

We collect unique copies of all materials under their standard primitive representation [[1](#links)] in a central "Bank" collection. The general features of such repositories are discussed in the following [introductory page](/entities-general/bank.md). 

Advanced search functionality specific to Materials and available also in the Bank are described [here](actions/advanced-search.md).

# Mapping Function

In the case of materials, the [Mapping Function](/entities-general/bank.md#bank-mapping-function) consists in first calculating the standard primitive representation of the candidate crystal structure originating from an Account-owned collection. 

Starting from this representation, the corresponding ["hash" string](/entities-general/bank.md#hash-strings) is then calculated. It is then compared against those of existing Bank entries. From this point onwards, the following two alternative scenarios can emerge.

## Positive Match

If a positive match of hash strings is encountered between the candidate structure and an existing Bank entry, then no new entry is created within the Bank collection. Rather, the Account-owned material is linked to the existing entry with the same hash.

## No Match

If no match is found, then a new Bank entry is created, under the primitive representation of the candidate material. Future materials sharing the same representation, and therefore the same hash, will then point to this new Bank entry.

# Links

1. [Standard primitive representation: Niggli Cell](https://nvlpubs.nist.gov/nistpubs/sp958-lide/188-190.pdf)
