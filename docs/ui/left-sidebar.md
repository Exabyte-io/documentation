# Left-hand sidebar (items navigation)

Clicking on the Menu Icon <i class="zmdi zmdi-menu zmdi-hc-border"></i>  at the top-left corner of the user interface will open the Items and Functions Navigator, in the form of a sidebar on the left-hand side of the page. A second click on this Menu Icon can then close the sidebar. The image below highlights the overall location of this sidebar within the broader interface:

<img src="/images/ui-left-sidebar.png"/>


The following table summarizes the different types of items contained in this left-hand sidebar. In particular, the items of type "Materials", "Jobs" and "Workflows" shall henceforth be commonly referred to as "Entities"  due to the numerous actions and properties that they share together. These common features are introduced in the [following general documentation page](/entities-general/overview.md).

| Menu Item & Icon                                         | Description
| :---------------------------                      |:-------------
| <i class="zmdi zmdi-circle"></i> &nbsp; Load                                      | Compute load shows how busy the compute system is. There are three levels: low, medium and high. It is opportune to start jobs when the indicator is low in order to achieve a quicker turnaround. Conversely, if the compute load is high, wait times for job turnaround will be longer.
| <i class="zmdi zmdi-view-dashboard"></i> &nbsp; Dashboard         | Dashboard highlights important datapoints and files of recent activity
| <i class="zmdi zmdi-file"></i> &nbsp; Create Job             | This is a quick link to get you started straight away on a job. Jobs saved will be collected in your default user project, which is name the same as your username and can be found in the projects page].
| <i class="zmdi zmdi-folder"></i> &nbsp; Projects           | Shows your list of projects
| <i class="zmdi zmdi-file"></i> &nbsp; Jobs                   | Shows your list of jobs
| <i class="zmdi zmdi-widgets"></i> &nbsp; Materials         | Shows your list of materials
| <i class="zmdi zmdi-dot-circle"></i> &nbsp; Workflows         | Shows your list of Workflows
| <i class="zmdi zmdi-balance"></i> &nbsp; Bank            | Import pre-defined Materials and Workflows from a central "Bank" repository
| <i class="zmdi zmdi-cloud-box"></i> &nbsp; Dropbox                         | File browser for cloud-based file/directories
| <i class="zmdi zmdi-globe-alt"></i> &nbsp; Accounts                                 | General list of user accounts
| <i class="zmdi zmdi-comments"></i> &nbsp; Shared with me                            | Items made available by other users
| <i class="zmdi zmdi-comments"></i> &nbsp; Shared publicly                            | Items shared to the general public
| <i class="zmdi zmdi-file"></i> &nbsp; Documentation                                 | A link to this documentation

The more complex entries in this left-hand sidebar are described comprehensively in dedicated documentation pages, referenced in the paragraphs below.

# Dashboard

The Dashboard component of the user interface is reviewed in the [following page](../dashboard.md).


# Create Job

The "Create Job" link <i class="zmdi zmdi-file-plus zmdi-hc-border"></i> takes the user to the job designer page, where new simulations can be conceived from start to finish. By default, new jobs are saved in the user's [default project](/data/convention/non-structured.md). The creation of new complete simulation Jobs is reviewed separately in its own dedicated documentation section, which explains how to proceed through the three main Job creation steps highlighted in the image below, namely the definition of the crystal structure to be investigated (1), of the type of Workflow calculation to be applied upon it (2), and finally of the computational resources to be allocated for this calculation (3): 

![Job Creation](/images/job-creation.png "Job Creation")

# Projects

The "Projects" page lists all the projects that have been previously created. Projects are essentially analogous to folders containing different Jobs items, and can be clicked upon directly on the their name in order to be navigated. The <i class="zmdi zmdi-plus-circle"></i> icon on the right of the Projects page can be clicked to create a new empty Project folder.

# Jobs, Materials and Workflows entities

The "Jobs", "Materials" and "Workflows" pages each offer a complete list of *all* the items of the respective entity type that have been created previously by the user. Due to the numerous different types of actions and other features that these three types of entities have in common, they are reviewed together starting from [this page](overview.md).

# Bank

This feature, common to both Materials and Workflows entities (but not available for Jobs for the moment), is documented [here](/entities-general/bank.md).


# Dropbox

Dropbox is a limited-capacity cloud-based data storage (see [data conventions](/data/convention/non-structured.md/#dropbox-directory)) accessible under the same filesystem path everywhere within our application. This menu item opens a file browser where one can navigate and edit (upload, download, delete) files and directories. This feature is particularly convenient for storing auxiliary simulations data (eg. pseudopotentials). The image below shows the general appearance of this Dropbox interface: 

![Dropbox](/images/Dropbox.png "Dropbox")

Further information about this Dropbox facility can be found [here](data/files/dropbox.md).


# Accounts and Data Sharing

Information about the other user accounts present in the Exabyte platform, about data shared bilaterally between accounts, and about data made publicly-available to the entire users community, can also be accessed from within the final section of the left-hand sidebar menu.

