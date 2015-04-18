## Compute and Storage Resources

As of Feb 11, 2015 major compute and storege systems are:

- cluster.exabyte.io - a 60 node cluster with 2160 compute cores, 3.6 Terabytes of memory, up to 0.1 Petabyte of disk storage and a 10 Gb low latency Ethernet Interconnect

- global `/home` storage system, provides each user with a large global storage space; global /home is permanent storage that is accessible from all cluster nodes

- local node storage provides each user with storage on each compute node and is limited to 250Gb per node; local node storage is temporary storage that is accessible only from a single cluster nodes

---

## How to Get Help

We encourage you to ask lots of questions. There are many ways to do that.

Support team can be contacted by phone, email, or the web (below) during working hours Pacific Time. Our consultants are experts in high performance and cloud computing and can answer just about all of your questions.

Our website is always available with a rich set of documentation, tutorials, and live status information.

Technical questions, computer operations, passwords, and account support

- email: info@exabyte.io
- phone: 1.510.473.7770
- computer operations = menu option 1
- online Help Desk = http://help.exabyte.io/

Computer operations (24x7) can reset your login credentials and give you machine status information. Account Support and HPC Consulting are available 8-5 Pacific Time on business days.

---

## New Accounts

In order to use our facilities you need:

1. A user account with an associated username
2. Access to an allocation of resources under the above username

If you are not a member of a project that already has an allocation, you may purchase an allocation using your profile page. If you need to get a new user account that will be associated with an existing award, you should [contact us](#how-to-get-help).

---

### Passwords and ssh keys

Each person has a single password associated with their login account on the web. As a new user, you will be able to download a private [ssh-key](https://wiki.archlinux.org/index.php/SSH_keys) directly from your profile page. This key together with your username can be used to access computational resources via command line terminal. This is a private key, sharing it with any third party is not advised. Anyone who is logged in using this key will have access to compute allocation registered under your username.

<!-- TODO: add gif images showing how to get started -->

---

### How to Login

Use any secure shell (ssh) terminal application and connect to our resources via command line.

An example below explains how to login for a user with username `amy`, who created and downloaded an ssh-key from a profile web page into `/myfolder/exabyte-cluster` using any Linux or Mac terminal application:

1. Change the permissions on the key to be accessible to you only:

    ```
    chmod 400 /myfolder/exabyte-cluster
    ```

2. Connect to cluster.exabyte.io

    ```
    ssh -i /myfolder/exabyte-cluster amy@cluster.exabyte.io`
    ```

---

### Login Failures

If you fail to type your correct password five times in a row when accessing our web application, your account will be locked.  To clear these failed logins, you should [contact us](#how-to-get-help).

---
