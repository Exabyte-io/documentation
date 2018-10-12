# People Explorer
 
Under both the wider Organizational Account Profile page and each [Team-specific page](team-pages.md), a "People" tab <i class="zmdi zmdi-account zmdi-hc-border"></i> is present
towards the top of the page. Clicking on this tab from either of these two locations will redirect the user to, respectively, a complete list of all Organization members (People), and to team-specific lists of team members. 

Both lists are presented to the user under the typical [Explorer-type interface](/entities-general/ui/explorer.md) of our platform. For this reason, we refer to both of these interfaces as the "People Explorer".

# Organization vs Teams

When drawing a distinction between the list of [members of the whole Organization](../actions/organization/add-remove-member.md), and the list of [members of any of its constituent Teams](../actions/team/add-remove-member.md) (which is necessarily a **subset** of the former list), we shall use the terms "Organization People Explorer" and "Team People Explorer" respectively. 

Despite both explorer interfaces having most of their features in common, a few differences are worth pointing out, as discussed in the following sections:

# Organization People Explorer

In the example image below, we start from the People Explorer interface under the profile page of an Organization called "Exabyte.io". This "Organization People Explorer" interface lists all members of this particular Organization, of which there are six in total as shown:

![Organization People Explorer](/images/organization-people-explorer.png "Organization People Explorer")

## Central Table of Interface: Owner and Admin Roles

It can be noticed from the above image that a clear indication of which members have the titles of "Owner" or "Admin" attributed to them is also present in the central table of the Organization People Explorer. In this example in particular, the user "exadmin" is the Owner and consequently also an Administrator of the Organization, and moreover it can be deduced that he is in fact the only user out of the whole Organization with Administrative privileges. 

## Organization-related Actions

The various administrative Actions concerning the Members of an Organization, such as their addition or removal from the Organization as well as the appointment or revoking of Administrators, can be executed under the Organization's corresponding People Explorer interface being currently discussed, as described [in this page](../actions/organization/overview.md).

# Team People Explorer

If we then click on one of the Teams included in the parent Organization, listed under the [Teams Explorer](teams-explorer.md) interface of the Organization, we will access its corresponding [Team-specific Page](team-pages.md). Under this latter page, the "Team People Explorer" interface under the "People" tab <i class="zmdi zmdi-account zmdi-hc-border"></i> can then be retrieved. 

For example, in the image below, the members of the Team "Semiconductor band gaps write" contained in the wider "Exabyte.io" Organization mentioned previously are listed under the Team's corresponding People Explorer interface. From inspecting the resulting list of Team members, it can be deduced that there are only four Team members listed this time, that is a subset of the original six members of the wider parent Organization. 

![Team People Explorer](/images/team-people-explorer.png "Team People Explorer")

## Central Table of Interface: Email Addresses

Furthermore, the  information displayed in the central table of the Team People Explorer this time consists in the email addresses of the Team members. No information about Administrator or Owner roles is in fact necessary in the context of Teams, since Teams don't have independent Administrative privileges but rather inherit such titles directly from the parent Organization.

## Actions Related to Team Members

The Team People Explorer interface gives the Owner or Administrators of the parent Organization the possibility to add or remove members to that particular Team under consideration, as explained [in this page](../actions/team/add-remove-member.md).
