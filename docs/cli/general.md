# CLI
---

Advanced users can request to access our compute platform via command-line interface (CLI).

## Compute and storage resources

As of Dec 9, 2015 major compute and storage systems are:

- angstrom.exabyte.io - an elastic compute cluster with (approximately):
    - 100,000 compute cores,
    - 100 terabytes of memory,
    - 8 exabytes of disk storage,
    - 10 Gb low latency Ethernet or 40Gb Ethernet (soon) interconnect

- global `/home` storage system, provides each user with a large global storage space; global /home is permanent storage that is accessible from all cluster nodes

- local node storage provides each user with storage on each compute node and is limited to 40Gb per node; local node storage is temporary storage that is accessible only from a single cluster node


## Passwords and ssh keys

Each person has a single password associated with their login account on the web. As a new user, you will be able to upload a public [ssh-key](https://wiki.archlinux.org/index.php/SSH_keys) directly from your profile page. This key together with your username can be used to access computational resources via command line terminal. Sharing a corresponfing private key with any third party is not advised. Anyone who is logged in using this key will have access to compute allocation registered under your username.

<!-- TODO: add gif images showing how to get started -->


## How to Login

Use any secure shell (ssh) terminal application and connect to our resources via command line.

An example below explains how to login for a user with username `amy`, who created and downloaded an ssh-key from a profile web page into `/myfolder/exabyte-cluster` using any Linux or Mac terminal application:

1. Change the permissions on the key to be accessible to you only:

    ```
    chmod 400 /myfolder/exabyte-cluster
    ```

2. Connect to compute platform at `login.exabyte.io`

    ```
    ssh -i /myfolder/exabyte-cluster amy@login.exabyte.io
    ```


## Login Failures

If you fail to type your correct password five times in a row when accessing our web application, your account will be locked.  To clear these failed logins, you should [contact us](#how-to-get-help).

