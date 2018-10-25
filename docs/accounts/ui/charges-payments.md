# Charges, Payments, and Payment Methods

Click `Billing and Payments` <i class="zmdi zmdi-card zmdi-hc-border"></i> on the [right-hand sidebar](/ui/universal/right-sidebar.md) to review the list of charges incurred by the account, and the payments executed to address them. The possibility to view or add Payment Methods is also offered. 

An example of a "Billing" page is exhibited below. We have highlighted in red the tabs for viewing charges, payments, and payments methods.

![Billing Page](/images/billing-page.png "Billing Page")

# Review Charges and Payments

Under the first two tabs, labelled "Charges" <i class="zmdi zmdi-file zmdi-hc-border"></i> and "Payments" <i class="zmdi zmdi-file-text zmdi-hc-border"></i>, the user can review respectively the charges incurred and the money paid so far by crediting the [Account Balance](../balance.md). 

Both balance sheets are presented under the standard [Explorer-type](/entities-general/ui/explorer.md) interface of our platform. The total sum of all the entries under each list is also indicated at the top of the page.

# Search Payments and Charges

## Quick Search

A [Search](/entities-general/actions/search.md) bar <i class="zmdi zmdi-search zmdi-hc-border"></i> is present at the top of both balance sheets. 

## Advanced Search

An [Advanced Search](/entities-general/actions/advanced-search.md) <i class="zmdi zmdi-search-for zmdi-hc-border"></i> feature is further offered in the Charges page, in order to filter charges more effectively.

The following properties of Charges are available to be searched under the advanced method.

| Property    |   Description      |  
| :-------- |:----------- |
| jobTitle |   Name of the Job, as defined at the moment of its [creation](/jobs-designer/header-menu/overview.md)   | 
| queue |  Type of [Queue](/jobs-designer/compute-tab.md) on the supercomputing cluster used for the computational task | 
| jid | A combination of the job number assigned by the task scheduler, and the cluster number. For example "142.master-production-20160630-cluster-007.exabyte.io" refers to job no. 20160630 executed on the cluster 007  |
| machine  |  Name of the cluster used for the computation, for example: "cluster-007"  | 
| project |   [Slug](/entities-general/data.md#Slug-Representation) representation of the project containing the Job, in the format "username-project-year-month-computation". For example "gmogni-project-2018-10-bandstructures"   |  
| type |  The type of task being charged, for example "Job"  | 
| wallDuration  | Time duration of the computation  | 
| charge |  Charge amount incurred as part of the computational task   | 
| username | Name of user who performed the computation  | 
| description | Short description of what the charge is for, assigned automatically by the accounting system. For example "charge for whole hour" | 
| startTime |  Date and time at which the Job was submitted to the cluster's queue  | 
| endTime | Date and time of Job termination following its completion  | 

# Payment Methods

The user can inspect the relevant information regarding all available Payment Methods by navigating to the "Payment Methods" tab <i class="zmdi zmdi-card zmdi-hc-border"></i>.

In this page, new Payment Methods (ie. Credit Cards) can also be [added](../accounting/payment-methods.md) to make them available as future options.

!!!warning "Warning: content with restricted access"
    The information contained under the present documentation page is relevant for Account [Owners or Administrators](/collaboration/organizations/roles.md), since only they have sufficient rights to view and modify the content (a user is always the Owner and Administrator of his personal account).
