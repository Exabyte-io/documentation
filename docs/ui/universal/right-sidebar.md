# Right-hand sidebar (account navigation)

Clicking on your name/username in the top right corner of the page will open the Account Navigator, in the form of a sidebar menu towards the right-hand side of the page. The general appearance of this sidebar is portrayed in the following image:

<img src="/images/ui-right-sidebar.png"/>

In particular, the following entries in this right-hand Account Navigator sidebar are worth noticing:

| Menu Item & Icon                                                            | Description
|:-----------------------------------------------------------------------   |:-------------
| Account Switcher                                                        | Enables switching between personal and organizational accounts. Opens in a small window showing your active accounts. Clicking on one triggers switch to that account.
| Quota, Queue, Service Level                                             | This section shows a quick snapshot of the status of your quota: Storage, job queue breakdown and your service level. You can easily upgrade your service level, to obtain more compute power, simply by clicking the upgrade button. If you want to compare service levels, you will find more information in the Account menu, below.
| Account Balance                                                         | A snapshot of your current balance, quickly credit the balance using the Apply Credit Button
| <i class="zmdi zmdi-settings"></i> &nbsp; [Account Preferences](../billing/settings-and-profile.md)                           | A link to [your account](../billing/settings-and-profile) page. In here you will find your user profile, your preferences and service level.
| <i class="zmdi zmdi-card"></i> &nbsp; [Billing & Payments](../billing/billing-and-payments.md)               | A link to the [billings and payments](../billing/billing-and-payments.md) section. In here you will your compute charges, payment records and payment methods.
| <i class="fa fa-terminal"></i> &nbsp; Terminal                                                                | Access to an in-browser command-line terminal thorugh which you can directly access your cloud account.
| <i class="fa fa-desktop"></i> &nbsp; Remote Desktop                                                          | Opens a desktop session (VNC) on Exabyte.io remote server.
| <i class="zmdi zmdi-accounts-add"></i> &nbsp; Invite a friend                                                         | Earn credits by inviting people to join Exabyte.io
| <i class="zmdi zmdi-power"></i> &nbsp; Logout                                                                  | Secure logout


# Account Switcher

The `My Accounts` card <i class="zmdi zmdi-globe-alt"></i>  at the top of the right hand menu sidebar shows the account that the user is currently logged into. Initially, this always defaults to the user's personal profile, but if the user created, or is a member of, an [organization](/collaboration/organizations.md), clicking here will open the complete list of organizations to which the user belongs. The user is then free to switch between his personal account and any of these other organizational accounts by clicking on their corresponding names among the list of account entries. 

For example, in the image below, two accounts are listed and can be chosen from: a personal account labelled "Team Exabyte", and a wider organizational account called "Exabyte.io":

![Accounts List](/images/accounts-list.png "Accounts List")

Once the user has decided to start using our product as a member of an organization, the interface will consequently reflect the change by showing the data related specifically to the organizational profile, for example storage quota and balance affecting the wider organization as opposed to the user's personal consumption.

# Account Snapshot

Below the account switcher, the right-hand sidebar offers a snapshot of the user's account (or that of an organization, as explained above). Some basic information related to the corresponding account is shown here: Storage Quota on each available supercomputing cluster, job queue summary in terms of numbers of submitted and active jobs, service level, and finally the current balance. The possibility to expand or replenish these two latter indicators is also offered next to each one of them.

An example of an account snapshot is shown below, for the case of an account with access to three different (relatively empty) clusters, and with no jobs currently being submitted or currently active. 

![Account Snapshot](/images/account-snapshot.png "Account Snapshot")


# Account Preferences

By clicking on the subsequent `Account Preferences` entry <i class="zmdi zmdi-settings"></i> in the right-hand sidebar menu, the user is offered the possibility to extensively customize the corresponding account information. This information in particular is comprised of the following main categories:

## General account information

![General Account Info](/images/general-account-info.png "General Account Info")

In this section, the user can enter generic information pertaining to the currently-selected account in the corresponding text fields, such as the desired account's name and affiliation, a general verbal description, and the email account and website associated with the account. Once all desired pieces of information have been entered, the `Update` button at the bottom should be pressed to apply and save the changes. 

## Modify Password

The possibility to modify the password for the current account is also offered towards the bottom of the Account Preferences page. To achieve this, the user should in particular first enter the old password that needs to be changed, and then the newly desired password followed by its confirmation. To apply this password modification for future use, the final `Submit` button should be clicked upon.


## Billing and Payments

The "Billing and Payments" link <i class="zmdi zmdi-card zmdi-hc-border"></i> redirects to the Billing page, containing a series of tabs at the top showing in turn all the different charges applied to the currently-selected account (for each job separately) <i class="zmdi zmdi-file-text zmdi-hc-border"></i>, the various payments made by the account owner <i class="zmdi zmdi-file-plus zmdi-hc-border"></i>, and the chosen payment methods <i class="zmdi zmdi-card zmdi-hc-border"></i>. More details about such billing and payments information can be found [here](/accounts/accounting/overview.md).

## Terminal and Remote Desktop

The Terminal and Remote Desktop functionalities provide alternative methods for accessing your account. More information about such practices can be retrieved [here](../../compute/cli/login.md).
