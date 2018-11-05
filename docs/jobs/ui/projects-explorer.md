# Projects Explorer

The list of all [Projects](../projects.md) created under the Account is displayed in the dedicated [Explorer](/entities-general/ui/explorer.md).

An example of appearance of Projects Explorer is shown below. The highlighted columns in the items list are the Project-specific ones. They are reviewed in turn in what follows.

![Projects Explorer](/images/projects-explorer.png "Projects Explorer")

# Number of Jobs

The total number of Jobs contained in each Project entry is indicated under the corresponding column, together with the subset of [active](../status.md) jobs. 

# Accounting Slug / CLI Path

The Accounting [Slug](/entities-general/data.md#Slug-Representation) offers a computer-friendly representation of the name of the Project. This is relevant in the context of [Account Charges](/accounts/ui/charges-payments.md).

The file system path of the Project inside the [Command Line Interface (CLI)](/cli/overview.md) of our platform is also displayed under the same column.
Question marks "???" might be present within this path instead of the actual cluster number label, when an ambiguity is present as to how many different clusters were employed for executing the contained Jobs.

# Status

Similarly to the [status](../status.md) of individual Jobs, each Project also has a general status assigned to it under the relevant column, according to the following conventions.

- "Active": at least one job is present with an [Active](../status.md#Active) status inside the Project. 
- "Stand-by": at least one job in the Project is pending execution but has been submitted to the queue already ([Submitted](../status.md#Submitted) status). 
- "Idle": all other possibilities, whereby all jobs contained in the project have statuses other than Active and Submitted.

# Default Project

A "Default" project is always created automatically at the moment of opening of a new Account. It is initially set to be [shared publicly](/collaboration/sharing/access-levels.md) with all platform users by default. 

Higher levels of privacy for this original Default Project, and all [subsequently created ones](../actions/create-delete-project.md), can only be changed if an appropriate [service level](/pricing/service-levels.md) is attributed to the account.

# View Project Contents

All Project entries listed in Explorer can be [opened](/entities-general/actions/open-edit.md) for content inspection. 

## Jobs Explorer Tab

The list of contained Jobs is displayed under the same interface as [Jobs Viewer](viewer.md), under the "Jobs" tab selectable at the top of the page. This is where the action of creating new Jobs originates, as explained in a separate [documentation page](../actions/create.md).

## Overview Tab

Another tab labelled "Overview" is present next to "Jobs". Here, a summarizing selection of Project's properties is displayed, as shown in the example below. All such properties are also available under the main Projects Explorer interface, as mentioned previously. 

![Overview Tab](/images/overview-tab-projects.png "Overview Tab")
