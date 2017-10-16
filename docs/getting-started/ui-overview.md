# Left sidebar (items navigation)

Clicking on the Left Hand Menu Icon <i class="zmdi zmdi-menu zmdi-hc-border"></i> will open the Items and Functions Navigator

<img data-gifffer="/images/OpenLeftHandSidebar.gif" />


| Menu Item & Icon                                         | Description
| :---------------------------                      |:-------------
| <i class="zmdi zmdi-circle"></i> &nbsp; Load                                      | Compute load shows how busy the compute system is. There are three levels: low, medium and high. It is opportune to start jobs when the indicator is low in order to achieve a quicker turnaround. Conversely, if the compute load is high, wait times for job turnaround will be longer.
| <i class="zmdi zmdi-view-dashboard"></i> &nbsp; [Dashboard](ui-overview.md#dashboard)         | Dashboard highlights important datapoints and files of recent activity
| <i class="zmdi zmdi-file"></i> &nbsp; [Create Job](/getting-started/run-first-simulation.md)             | This is a quick link to get you started straight away on a job. Jobs saved will be collected in your default user project, which is name the same as your username and can be found in the projects page].
| <i class="zmdi zmdi-folder"></i> &nbsp; [Projects](ui-overview.md#projects)           | Shows your list of projects
| <i class="zmdi zmdi-file"></i> &nbsp; [Jobs](ui-overview.md#jobs)                   | Shows your list of jobs
| <i class="zmdi zmdi-chart"></i> &nbsp; [Analytics](ui-overview.md#analytics)         | Allows you to compare multiple materials
| <i class="zmdi zmdi-widgets"></i> &nbsp; [Materials](ui-overview.md#materials)         | Shows your list of materials
| <i class="zmdi zmdi-account"></i> &nbsp; Users                                         | Shows a list of public users of Exabyte
| <i class="zmdi zmdi-cloud-box"></i> &nbsp; [Dropbox](#dropbox)                                         | File browser for cloud-based file/directories
| <i class="zmdi zmdi-globe-alt"></i> &nbsp; Organizations                                 | Team collaboration and extended privacy
| <i class="zmdi zmdi-comments"></i> &nbsp; Forum                                         | Discuss issues with other users and Exabyte.io staff
| <i class="zmdi zmdi-file"></i> &nbsp; Documentation                                 | A link to this documentation

# Right sidebar (account navigation)

Clicking on your name/username in the top right will open the Account navigation.

<img data-gifffer="/images/OpenRightHandSidebar.gif" />

| Menu Item & Icon                                                            | Description
|:-----------------------------------------------------------------------   |:-------------
| Account Switcher                                                        | Enables switching between personal and organizational accounts. Opens in a small window showing your active accounts. Clicking on one triggers switch to that account.
| Quota, Queue, Service Level                                             | This section shows a quick snapshot of the status of your quota: Storage, job queue breakdown and your service level. You can easily upgrade your service level, to obtain more compute power, simply by clicking the upgrade button. If you want to compare service levels, you will find more information in the Account menu, below.
| Account Balance                                                         | A snapshot of your current balance, quickly credit the balance using the Apply Credit Button
| <i class="zmdi zmdi-settings"></i> &nbsp; [Account](../billing/settings-and-profile.md)                           | A link to [your account](../billing/settings-and-profile) page. In here you will find your user profile, your preferences and service level.
| <i class="zmdi zmdi-card"></i> &nbsp; [Billing & Payments](../billing/billing-and-payments.md)               | A link to the [billings and payments](../billing/billing-and-payments.md) section. In here you will your compute charges, payment records and payment methods.
| <i class="fa fa-terminal"></i> &nbsp; Terminal                                                                | Access to an in-browser command-line terminal thorugh which you can directly access your cloud account.
| <i class="fa fa-desktop"></i> &nbsp; Remote Desktop                                                          | Opens a desktop session (VNC) on Exabyte.io remote server.
| <i class="zmdi zmdi-accounts-add"></i> &nbsp; Invite a friend                                                         | Earn credits by inviting people to join Exabyte.io
| <i class="zmdi zmdi-power"></i> &nbsp; Logout                                                                  | Secure logout

<hr>

# Items Navigation

## User Dashboard

Dashboard quickly fills you on on the status of the system and your recent work.

### Compute Usage

Compute usage chart shows the compute costs for the recent calculations.

### Datapoints

| Datapoint             | Description
| :-------------        |:-------------
| Charges this week     | Shows a summary of the total charges of this week
| Charges last week     | Shows the equivalent charges of last week for comparison
| Longest Job           | Shows compute walltime of the longest job
| Current Server Load   | Shows current server compute load (low/medium/high)
| Estimated Wait Time   | Shows an estimated wait time for compute power

### Storage Quota

This widget displays a summary of your current data storage quota: used and total storage space. Click on the <i class="zmdi zmdi-plus-circle-o zmdi-hc-border"></i> icon to request an increase. Click on the <i class="zmdi zmdi-refresh-sync zmdi-hc-border"></i> icon to refresh data.

### Jobs summary

Jobs summary widget summarizes the total number of jobs run during this same period, and also offers a break down of the job types. There is also a quick link to jump to the jobs list.

## Create Job

"Create Job" link <i class="zmdi zmdi-file-plus zmdi-hc-border"></i> takes you to the job designer page where you can create simulations. By default new jobs is saved in your [default project](/getting-started/data-conventions.md).

## Projects

"Projects" page lists all the projects you have created. Projects contain "Jobs", click on the project name to navigate into it. Click on the <i class="zmdi zmdi-plus-circle"></i> icon to create a new one.

## Jobs

"Jobs" page is a complete list of *all* the jobs you created. From here you can:

- click on a job item name to quickly open it,
- click on the plus icon <i class="zmdi zmdi-plus-circle zmdi-hc-border"></i> to create a new job,
- use the checkboxes to select multiple items, and the toolbar icons (top right) to run actions on all the items selected,
- use the search bar <i class="zmdi zmdi-search zmdi-hc-border"></i> to filter the items list,
- click on a dropdown inside a job item to open a submenu where you can:
    -  <i class="zmdi zmdi-play zmdi-hc-border"></i> Run,
    -  <i class="zmdi zmdi-stop zmdi-hc-border"></i> Terminate,
    -  <i class="zmdi zmdi-copy zmdi-hc-border"></i> Clone,
    -  <i class="zmdi zmdi-delete zmdi-hc-border"></i> Delete,
    -  <i class="zmdi zmdi-eye zmdi-hc-border"></i> Open the jobs

## Materials

A list of all the materials you have imported, created or uploaded into your account. Same as for "Jobs" you can create, search and navigate into materials, plus:

- <i class="zmdi zmdi-cloud-download zmdi-hc-border"></i> Import materials into your account (direct import from materialsproject.org is supported at current)
- <i class="zmdi zmdi-cloud-upload zmdi-hc-border"></i> Upload materials from your computer

## Users

"Users" page shows all user profiles that are accessible to you.

## Analytics

"Analytics" page is meant for data analytics. From here you can access all data accessible to you through our application, including public, your personal and organizational data alltogether.

## Dropbox

Dropbox is a limited-capacity cloud-based data storage (see [data conventions](/getting-started/data-conventions/#dropbox-directory)) accessible under the same filesystem path everywhere within our application. This menu item opens a file browser where one can navigate and edit (upload, download, delete) files and directories. Convenient for auxiliary simulations data (eg. pseudopotentials).

![Dropbox](../images/Dropbox.png "Dropbox")

## Organizations

"Organizations" is where collaboration happens between teams. The Organizations page will show all the organizations that you are a member of.

<hr>

# Account Navigation

## Account Switcher

The Account card at the top of the right hand menu shows the account you are currently using. Initially this is your personal profile, but if you have created, or are a member of, an organization, clicking here will open the list of organizations to which you belong.

You can then click on one to start using our product as a member of an organization. Interface will now show data related to the organization profile: eg. storage quota and balance will be that of the organization, projects and jobs etc.

<img data-gifffer="/images/AccountSwitcher.gif" />

## Account Snapshot

Below the account switcher is a snapshot of your account (or that of an organization, as explained above). We show some basic information related to your account: Storage Quota, job queue summary, service level and current balance.

## Account and Preferences

Account page has three tabs:

+ Bio <i class="zmdi zmdi-eye zmdi-hc-border"></i> shows your public profile information and recent work
+ Preferences <i class="zmdi zmdi-settings zmdi-hc-border"></i> holds your account preferences such as [REST API](/rest-api/authentication.md) key, job cloning suffix and other settings
+ Service Level <i class="zmdi zmdi-layers zmdi-hc-border"></i> shows details about your current balance, storage quota and Service Level. See the [Accounts & Billings](/billing/settings-and-profile.md) section for more details.

## Billing

Billings link takes you to the Billing page which shows your account Charges <i class="zmdi zmdi-file-text zmdi-hc-border"></i> (ie. per each job), Payments <i class="zmdi zmdi-file-plus zmdi-hc-border"></i> and Payment Methods <i class="zmdi zmdi-card zmdi-hc-border"></i>. More details [here](/billing/billing-and-payments.md).

## Terminal and Remote Desktop

Alternative ways to access your account. More information [here](../cli/login.md).

## Invite a friend

You both will get $10 credit when registration request is approved. Find out how in the [Refer a friend page](/collaboration/invite-friends.md)
