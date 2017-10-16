<!-- by MM -->

# Creating a project

The following demonstrates how to create a new project inside an organization. Only organization owner has access to new projects. If you want to give other organization members access to the project, please visit [adding a project to a team](teams#adding-a-project-to-a-team) page.

<img data-gifffer="/images/organization-create-project.gif">

!!! note "Default Project"
    When you create an organization, it is initialized with a default project. The name of the default project is as same as the organization name.

# Deleting a project

You can delete a project as follow:

<img data-gifffer="/images/organization-remove-project.gif">

# Creating a job inside a project

Managing jobs inside organization projects is exactly the same as managing jobs in your personal projects. The following shows how to create and submit a job inside an organization project:

<img data-gifffer="/images/organization-project-create-job.gif">

!!! note "CLI Jobs"
    If you decide to create and submit a job from [CLI](/cli/overview) inside an organization project, you should set `#PBS -A ACCOUNTING_NAME` directive inside your job script file. `ACCOUNTING_NAME` can be obtained from "OVERVIEW" tab of the project. 
