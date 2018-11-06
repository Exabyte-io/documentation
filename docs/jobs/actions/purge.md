# Purge Job

Purge differs from the [delete action](/entities-general/actions/delete.md) in the following aspects: the job being purged is kept in the account-owned collection, but all simulation files present on the cluster's hard drives are removed. These files remain however visible under the [Files Tab](../ui/files-tab.md) of the [Jobs Viewer](../ui/viewer.md), as object representations. 

The purge action is restricted to Jobs with a ["Finished" status](../status.md).

# Action

To purge a Job listed under the [Jobs Explorer](../ui/explorer.md), first [select it](/entities-general/actions/select.md) and press the "Purge" button <i class="zmdi zmdi-card-off zmdi-hc-border"></i> located in the top right [actions toolbar](/entities-general/ui/explorer.md#actions-toolbar).

Alternatively, the same action can be performed under the [actions dropdown](/entities-general/ui/explorer.md#actions-dropdown) of the item entry that needs purging.

# Animation

In the example animation below, we begin by purging an electronic bandstructure calculation Job. We then copy the path of one of the files listed under Jobs Viewer, and under the [Web Terminal](/connection-methods/web-terminal.md) we finally confirm its deletion from the cluster disk after pasting the file path in it.

<img data-gifffer="/images/purge-job.gif">
