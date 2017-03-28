<!-- by MM -->

Teams let you create manage permissions for the members of an organization. You can use teams to give specific access (read or write) to selected projects.

# Creating a team

The following animation shows how to crate a team. A team consists of a group of organization members that have read or write access to projects associated with the team. The access type (read or write) is set on team creation.

<img data-gifffer="/images/organization-create-team.gif">

# Adding a project to a team

Teams provide specific access (read or write) to projects associated with itself. At least one project should be added to a team. You can add a project to the team as follows:

<img data-gifffer="/images/organization-add-project-to-team.gif">

!!! note "Access Project"
    When a project is added to a team, all team members are granted read or write access to the given project. Team members will be able to see (or edit in case of write access) jobs inside the project.

# Deleting a project from a team

A project can be removed from a team as follow:

<img data-gifffer="/images/organization-remove-project-from-team.gif">

!!! note "Access Project"
    When the project is removed from the team, none of the team members will be able to access the project, unless they are given access inside other teams. 

# Managing team members

The following shows how to add and delete team members:

!!! note "Team Members"
    You should add users to your organization (explained [here](overview#adding-a-member-to-organization)) before adding them to a team.

<img data-gifffer="/images/organization-team-manage-users.gif">

# Collaborating on a project

The following example shows how organization members can collaborate on a project. In first part, organization owner "demo" creates a write-access team with "demo" and "exadmin" as organization members and adds the default project "exabyte.io" into it. "demo" then creates a job and saves it inside the default project. In second part "exadmin" user navigates to the job, adjusts its parameters and submits the job.

## First part

<img data-gifffer="/images/organization-collaborate-on-job-1.gif">

## Second part

<img data-gifffer="/images/organization-collaborate-on-job-2.gif">

