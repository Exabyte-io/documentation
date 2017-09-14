<!-- by MM -->

## Storage system

As a CLI user you have access to multiple data centers. Each data center has its own storage systems mounted on `/home` and `/share` directories. In order to provide you with a unified file system so that you can manage all your data from a central place we have mounted all clusters' `/home` and `/share` directories on login node and created necessary links to your home directory. When you ssh to login node, your home directory should contain the following directories:

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

As it can be seen, there is a separate directory for each cluster. In each cluster directory there are 2 subdirectores, `home` and `share`. If you want to run a job in a specific cluster, for example cluster-001, you need to navigate to `cluster-001/home` or `cluster-001/share` directory. Please note that files and directories on `cluster-001` are not accessible on other clusters. If you have files that you would like to access from all clusters, you can put it inside `dropbox` directory. `dropbox` directory is accessible on all cluster from the same path, `/home/USER/dropbox`. 

!!! warning "Dropbox Directory"
    `dropbox` directory is not designed to handle large files or to run calculation on.
