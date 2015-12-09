
# Documentation

Welcome to our documentation repository! We aim to provide all the necessary information for you to use our product here. In case you find that something is missing of you still have questions after reading this documentation, please <a href="mailto:support@exabyte.io" target="_blank">contact us</a> .

## How to Get Help

We encourage you to ask lots of questions. There are many ways to do that.
Our support team can be contacted by phone, email, or the web during working hours Pacific Time. Our consultants are experts in high performance and cloud computing and can answer just about all of your questions.

Technical questions, computer operations, passwords, and account support

- email: support@exabyte.io
- phone: 1.510.473.7770
- feedback: https://platform.exabyte.io/

## New Accounts

In order to use our facilities you need:

1. A user account with an associated username
2. Access to an allocation of resources under the above username

All newly registered users have $10 credited to their personal allocations. If you are not a member of a project that already has an allocation, you may purchase an allocation using our web application.

<!-- TODO: add explanation about how to purchase above -->
<!-- TODO: add pricing description -->


# QuickStart

If you are new to Exabyte.io and feeling impatient, you can get started by following this tutorial summarizing the
[first steps with Exabyte](tutorials/first-steps.md). You will learn how to create and save your first material and run a simulation that predicts this material's electronic bandstructure.

# Basics

## Projects

We organize user workspace using projects. Project contains a study of a particular material or a set of materials that are related to each other. Projects have a single owner, and can have multiple users that collaborate together.

Here is how the list of projects looks like from within the application.

<br>
<img src="images/list_of_projects.png" width="800">
<br>

Every user has a default project with a name equal to username created for him/her at the moment of registration. You can create a new project by clicking (+) button at the top right corner of the page. You can delete the projects by using action buttons in the "Actions" row. Default project cannot be deleted by convention.

To see the jobs that belong to a project, click on the project's name.

### Jobs

When you click on one of the Projects you see the list of jobs.

<br>
<img src="images/list_of_jobs.png" width="800">
<br>

You can create a new Job by clicking "New Job" button at the top right corner of the page.

To view the job, click on its name.


## Materials

"Materials" section contains all previously created materials. It is empty initially, however you can start saving (and retrieving) your materials while running the jobs. Clicking "New Material" button at the top right corner of the page will get you started with this.


## Profile

### Settings

Settings section lets one view and update personal information, system-specific parameters and security settings.

#### SSH Keys

SSH Keys section contains the your public keys that give you command-line access to our compute platform through secure shell protocol. You can generate ssh keys on your local machine and upload the public one to our compute platform.

More documentation about command-line access to our compute platform is available [here](cli/general.md).

A good tutorial on how to create SSH keys can be found [here](https://www.digitalocean.com/community/tutorials/how-to-set-up-ssh-keys--2).


## Billing

Billing page contains accounting information about your jobs:

- Project: project the job belongs to
- Job: the name of the job
- Processors: number of the processors the job used at runtime
- Invoice Date: Billing record for the job
- Sum($): cost per job in $
- Wall duration: total amount of compute time used by the job (in CPU-hours)

