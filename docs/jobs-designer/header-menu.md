# Header Menu

The main header menu at the top of the [Jobs Designer](overview.md) interface is comprised of the following aspects shown below. Please refer to the ensuing explanations under the same number labels.

![Header Menu](/images/header-jobs-designer.png "Header Menu")

# 1. Edit Job Name

The name of the Job being created can be edited on the left-hand side of the header menu. 

The name of the Project container is also displayed in smaller characters directly underneath it, however unlike Jobs it cannot be modified following Project creation.

# 2. Insertion of Descriptive Metadata

A description of the Job being created can be entered in the Markdown syntax through the "Information" icon <i class="zmdi zmdi-info-outline zmdi-hc-border"></i>. The reader is referred to [this page](/entities-general/actions/metadata.md#edit-description) for a full explanation of descriptive metadata.

# 3. Select Entities and / or Submit Job

The second button <i class="zmdi zmdi-more-vert zmdi-hc-border"></i> towards the right of the header menu allows the user primarily to add new entities to the Job being created. The following options are available under the corresponding drop-down menu.

## Select Parent

This option is convenient when the Job being created is intended to be run on top of the results obtained from a previous "parent" Job. Some examples where such a scenario is plausible include the re-calculation of a phonon or bandstructure dispersion curve along a different reciprocal path, or obtaining the same results but with a higher precision. In both cases, the same preliminary calculations performed in the preceding parent job can be re-utilized, thus saving computational time.  

The action of selecting a parent job is explained in detail [here](header-menu/select-parent.md).

## Select Materials

Multiple [Materials](/materials/overview.md) can be selected from the account-owned collection, and added to the Job under creation for simultaneously applying the workflow computational tasks to all of them. This procedure is described separately [in this page](header-menu/select-materials.md).

## Select  Workflow

A [Workflow](/workflows/overview.md) can also be selected and added to the Job, for performing computations on all materials selected in the previous step. It is worth highlighting that, contrary to the case of Materials, only one such workflow can be added to a Job at a time. If the user wishes to execute multiple computational tasks sequentially, he/she should consider the possibility of creating a sequence of [Subworkflows](/workflow-designer/subworkflow-editor/overview.md) within the same Workflow instead.

Instructions on how to select Workflows from the account-owned collection and add them to the Job being designed can be found [here](header-menu/select-workflow.md).

## Submit

The `Submit` option is only present for the case of Jobs with a "Pre-submission" [status](/jobs/status.md), which have been opened in Designer directly from [Explorer](/jobs/ui/explorer.md). Pressing `Submit` first saves the Job to the account-owned collection, and then directly submits it to the [queue](/infrastructure/resource/queues.md) for its computational execution on the relevant [cluster](/infrastructure/clusters/overview.md). 

# 4. Save Job

The Job being currently designed can finally be saved, after all appropriate changes have been made, by clicking the "Save" button <i class="zmdi zmdi-check zmdi-hc-border"></i>. 

Once the new Job has been saved, the view is returned to the original [Project page](/jobs/ui/projects-page.md). Here, the new Job is now listed as a top entry under [Jobs Explorer](/jobs/ui/explorer.md) and has a "Pre-submission" [status](/jobs/status.md), indicating its readiness to be [submitted for execution](/jobs/actions/run.md).
