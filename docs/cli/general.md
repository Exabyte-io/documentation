# COMMAND LINE INTERFACE

Advanced users can request to access our compute platform via command-line interface (CLI).

## Compute and storage resources

As of Dec, 2015 major compute and storage systems are:

- angstrom.exabyte.io - an elastic compute cluster with (approximately):
    - 100,000 compute cores,
    - 100 terabytes of memory,
    - 8 exabytes of disk storage,
    - 10 Gb low latency Ethernet or 40Gb Ethernet (soon) interconnect

- global `/home` storage system, provides each user with a large global storage space; global /home is permanent storage that is accessible from all cluster nodes

- local node storage provides each user with storage on each compute node and is limited to 40Gb per node; local node storage is temporary storage that is accessible only from a single cluster node


## Passwords and ssh keys

Each person has a single password associated with their login account on the web. As a new user, you will be able to upload a public directly from your profile page. This key together with your username can be used to access computational resources via command line interface. Sharing a corresponfing private key with any third party is not advised. Anyone who is logged in using this key will have access to compute allocation registered under your username.

More information on how to login is available [here](login.md).

<!-- TODO: add gif images showing how to get started -->


