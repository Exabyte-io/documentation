# Default Entities

Some Entities, such as [Materials](/materials/overview.md) and [Workflows](/workflows/overview.md) have a "default" item in their respective collection. The default material, for example, is used to pre-initiate the [job](/jobs-designer/overview.md) and [workflow](/workflow-designer/general-overview.md) designer interfaces. For example, the workflow templating context may adjust depending on the material, and users can tune the adjustments by changing the default material. Similarly, users can set the most frequently used workflow as default in order to avoid changing it during the job creation.

The user can recognize the entity as being the default entity for future operations by the check-mark assigned to it under the "Default" column of the [Explorer](../ui/explorer.md) interface.

# Changing Default Entity

In order to change the default item, use `Set default` option <i class="zmdi zmdi-star-outline zmdi-hc-border"></i> in the [actions drop-down menu](/entities-general/ui/explorer.md#actions-dropdown). 

> NOTE: an entity cannot be deleted from an account-owned collection for as long as it is set as the default one. Only one entity at a time can be set as default in the context of a particular collection.

# Animation

If we take workflows as our case study, then a new default entry can be chosen as demonstrated in the animation below:

<img data-gifffer="/images/setting-default.gif" />

