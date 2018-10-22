# The Workflows Bank

The most common types of calculations routinely encountered have already been assembled in the form of pre-defined workflows, and are currently available for distribution in a central repository accessible to all users. We  refer to it as the Workflows Bank (to be compared with the equivalent Bank facility for pre-defined material structures documented [here](../materials/bank.md)). 

 Through such pre-built workflows, the user is therefore spared from having to re-implement computations such as the calculation of the total energy of crystals, of phonon dispersion curves, electronic band structures and similar.

# Bank Mapping Function

The concept of a "Bank" of entities was already the object of a general review [in this page](/entities-general/bank.md). It is worth noticing that the Bank's ["Mapping Function"](/entities-general/bank.md#bank-mapping-function) described therein consists, in the specific context of workflows, in an assessment of the logical operations and input files contained in the candidate Account-owned workflow.

From this assessment, the corresponding ["hash" string](/entities-general/bank.md#hash-strings) is then calculated, and compared against those of existing Bank entries. From this point onwards, two alternative scenarios can emerge:

## Positive Match of Hash Strings

If a positive match of hash strings is encountered between the Account-owned candidate structure and an existing entry within the Workflows Bank, then no new Bank entry is created. Rather, the Account-owned workflow is linked to the existing Bank entry with the same hash.

## No Match of Hash Strings

If no match is found, then a new Bank entry is created, containing the same logical operations and input files  as those of the candidate workflow. Future workflows originating from all Accounts on the platform that share the same logical composition, and therefore the same hash, will then point to this new  Bank entry.
 
# Animation

In the animation below, we demonstrate how to import a pre-defined workflow, which performs the electronic band structure calculation, from Workflows Bank into the account-owned collection. The workflow is retrieved from the Bank upon entering and searching for the "band structure" keywords in the search bar of the Bank page:

<img data-gifffer="/images/run-first-simulation-import-workflow.gif" />
