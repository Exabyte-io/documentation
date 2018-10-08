# Introduction

We allow command-line access for the limited set of expert users whom we have established lasting relationships with. Below is a brief explanation of how their data is secured. 

# File system permissions

Command-line users have access to two main directories, `/home` and `/share`. 

## Home directory

Each user has read and write permissions on their home directory. **No one else** is able to access the content of it.

!!! warning "Modifying permissions within /home"
    We strongly advise agains modifying permissions for your home directory or any top-level system directories included within (eg. `~/.ssh/`). If you feel that you *must* do that please coordinate the actions with us first. For the purpose of setting up shared data access `share` directory should be used instead.

## Share directory

Share directory (`/share`) is accessible to organizations. 

When an organization is created, a directory with specially set permissions is created inside `/share/groups` directory. 

> Please note that you should not modify permissions on `/share` directory, otherwise you would get permission denied while submitting organizational jobs to the system. 

An organization has an owner and may have multiple projects and teams. Each team may have access to multiple projects. Members of a project (and the organization owners/administrators) are able to see the content of a project directory. For example, imagine you have created an organization named "my-org" and a project called "my-project". You would then see `/share/groups/my-org/my-project` directory. You as an organization owner have read and write permissions on `/share/groups/my-org/my-project` directory. Also any member of "my-project" as defined inside the web application has read and write permissions on the project directory.
