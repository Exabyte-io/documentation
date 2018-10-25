# Workflows Bank

The most common types of calculations routinely encountered have already been assembled in the form of pre-defined workflows, and are available for distribution in a central repository accessible to all users. We  refer to it as the Workflows Bank (to be compared with the equivalent facility for material structures documented [here](/materials/bank.md)). 

 Through such pre-built workflows, the user is therefore spared from having to re-implement computations such as the calculation of the total energy of crystals, phonon dispersion curves, electronic band structures and similar.

The concept of a "Bank" of entities was the object of a general introduction [in this page](/entities-general/bank.md).

# Mapping Function

The Bank's ["Mapping Function"](/entities-general/bank.md#bank-mapping-function) consists, in the specific context of workflows, in an assessment of the workflow's logical operations and input files.

Based on this assessment, the corresponding ["hash" string](/entities-general/bank.md#hash-strings) is then calculated, and compared against those of existing Bank entries. From this point onwards, the following two alternative scenarios can emerge.

## Positive Match

If a positive match of hash strings is encountered between the candidate structure and an existing entry within the Workflows Bank, then no new Bank entry is created. Rather, the workflow is linked to the existing entry with the same hash.

## No Match

If no match is found, then a new Bank entry is created, containing the same logical operations and input files  as those of the candidate workflow. Future workflows that share the same logical composition, and therefore the same hash, will then point to this new entry.
 
# Animation

In the animation below, we demonstrate how to import a pre-defined workflow, which performs the electronic band structure calculation, from the Bank into the account-owned collection. The workflow is retrieved upon entering and searching for the "band structure" keywords in the [search bar](/entities-general/actions/search.md).

<img data-gifffer="/images/run-first-simulation-import-workflow.gif" />
