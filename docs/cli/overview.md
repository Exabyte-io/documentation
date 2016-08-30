<!-- TODO by MM: revise and add necessary content about helper functions and default options/template scripts available -->
# Command Line Interface

Advanced users can request to access our compute platform via command-line interface (CLI) by contacting support team at support@exabyte.io.

In order to deliver the best quality service, we make command-line interface available only for certain [subscription levels](/billing/accounts-and-billing#pricing), when long-term mutual commitment is established.

## Passwords and ssh keys

Each person has a single password associated with their login account on the web. As a new user, you are able to upload a public ssh key directly from your profile page. This key together with your username can be used to access computational resources via command line interface. Sharing a corresponfing private key with any third party is not advised. Anyone who is logged in using this key will have access to compute allocation registered under your username.

More information on how to login is available [here](login.md).

## Storage systems

When as a CLI user, the following storage systems become available:

- `/home`: provides each user with storage space; this is permanent storage accessible from all cluster nodes

- `/share`: provides user signed up for subscription levels that support organizations with a global storage space that can be accessed by multiple users within the organization; this is permanent storage accessible from all cluster nodes

- local node storage provides each user with storage on each compute node and is limited to 40Gb per node; local node storage is temporary storage that is accessible only from a single cluster node


<!-- TODO: add gif images showing how to get started -->
