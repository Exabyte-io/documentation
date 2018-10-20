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

This Account-related feature is described in its entirety in a [separate part of the documentation](/accounts/ui/switcher.md).

# Account Snapshot

Below the account switcher, the right-hand sidebar offers a snapshot of the user's account (or that of an organization, as explained above). Some basic information related to the corresponding account is shown here: Storage Quota on each available supercomputing cluster, job queue summary in terms of numbers of submitted and active jobs, service level, and finally the current balance. The possibility to expand or replenish these two latter indicators is also offered next to each one of them.

An example of an account snapshot is shown below, for the case of an account with access to three different (relatively empty) clusters, and with no jobs currently being submitted or currently active. 

![Account Snapshot](/images/account-snapshot.png "Account Snapshot")


# Account Preferences

By clicking on the subsequent `Account Preferences` entry <i class="zmdi zmdi-settings"></i> in the right-hand sidebar menu, the user is offered the possibility to extensively customize various aspects of the account-related information and settings. Such "Account Preferences" are reviewed extensively in their own [documentation section](/accounts/ui/preferences-overview.md).

# Billing and Payments

The "Billing and Payments" link <i class="zmdi zmdi-card zmdi-hc-border"></i> redirects to the Billing page, containing a series of tabs at the top showing in turn all the different charges applied to the currently-selected account (for each job separately) <i class="zmdi zmdi-file-text zmdi-hc-border"></i>, the various payments made by the account owner <i class="zmdi zmdi-file-plus zmdi-hc-border"></i>, and the chosen payment methods <i class="zmdi zmdi-card zmdi-hc-border"></i>. More details about such billing and payments information can be found [here](/accounts/accounting/overview.md).

# Terminal and Remote Desktop

The Terminal and Remote Desktop functionalities provide alternative methods for accessing your account. More information about such practices can be retrieved [here](../../compute/cli/login.md).

# Invite a Friend

The "Invite a Friend" option  <i class="zmdi zmdi-accounts-add zmdi-hc-border"></i> lets users send an email invitation to a friend or colleague who shares similar interests and might also benefit from registering and using our platform product. Both the sender and recipient of the email invitation will get $10 in the form of Account balance credit when the new registration request is approved.

# Logout

The final "Logout" option <i class="zmdi zmdi-power zmdi-hc-border"></i> under the right-hand sidebar should be pressed once all operations under the current Account have been completed, and the current user wishes to let other users login to the platform with their own combination of username/email and password credentials.
