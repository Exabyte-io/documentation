<!-- TODO: GM to revise the page to add explanation about how to view quotas -->

## Storage system

Users have access to multiple clusters. Each cluster has its own storage systems mounted on `/home` and `/share` directories. In order to provide a unified file system so that you can manage all your data from a central place we created links inside each user's `home` directory. When you ssh to login node, your home directory contains the following:

```bash
[demo@bohr.exabyte.io ~]$ ls -lhta
total 0
drwxrwxr-x. 2 demo demo 29 Sep  5 02:15 cluster-001
drwxrwxr-x. 2 demo demo 29 Sep  5 02:15 cluster-003
drwxrwxr-x. 2 demo demo 29 Sep  5 02:15 cluster-005
lrwxrwxrwx. 1 demo demo 13 Sep  5 02:15 dropbox -> /dropbox/demo
  
[demo@bohr.exabyte.io ~]$ ls -lhta cluster-001
total 4.0K
drwx------. 9 demo demo 4.0K Sep  5 02:15 ..
drwxrwxr-x. 2 demo demo   29 Sep  5 02:15 .
lrwxrwxrwx. 1 demo demo   18 Sep  5 02:15 share -> /cluster-001-share
lrwxrwxrwx. 1 demo demo   22 Sep  5 02:15 home -> /cluster-001-home/demo
```

In each cluster directory there are 2 subdirectores, `home` and `share`. If you want to run a job on cluster-001, you should navigate to either`cluster-001/home` or `cluster-001/share` directory. Please note that files and directories on `cluster-001` are not accessible on other clusters.

## Dropbox

If you have files that you would like to access from all clusters, for example - pseudopotentials, basis sets, input scripts, you can put them inside `dropbox` directory. `dropbox` directory is accessible on all clusters from the same path: `/home/<USERNAME>/dropbox`. 

!!! warning "Limitations"
    `dropbox` directory is limited to 1GB by default and it is not designed to handle large files or, moreover - to run calculation in.
