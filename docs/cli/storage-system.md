## Storage system

When as a CLI user, the following storage systems become available:

- `/home`: provides each user with storage space; this is permanent storage accessible from all cluster nodes.

- `/share`: provides user signed up for subscription levels that support organizations with a global storage space that can be accessed by multiple users within the organization; this is permanent storage accessible from all cluster nodes.


### Unified file system

As a CLI user you have access to multiple data centers. Each data center has its own storage systems. In order to provide you with a unified file system so that you can manage all your data from a central point we have aggregated all `/home` directories to `/export/home` and all `/share` directories to `/share` on login node. The aggregation is done by [UnionFS](https://www.filesystems.org/project-unionfs.html). 

UnionFS merges the contents of several directories (called branches), while keeping their physical content separate. For example imagine there are two clusters available, cluster-001 and cluster-002. The `/home` and `/share` directories of each cluster is mounted separately on login node on `/cluster-001-home`, `/cluster-001-share`, `/cluster-002-home` and `/cluster-002-share`. Then home and share directories are merged to `/export/home` and `/share` respectively. So if you have file X on `/cluster-001-home` and file Y on `/cluster-002-home` you would see both files, X and Y when you go to your home directory.

When you create a new file or directory inside home or share directory, it is placed on the first branch of UnionFS. So you would not access this file other clusters (branches). If you want to have the file or directory on a specific cluster you should create the file on the main branch explicitly. For example if you want to have file Z to be available on home directory of cluster-002, you should create the file in `/cluster-002-home/USERNAME/X`. We do this for you automatically when you submit a job to a specific cluster. The whole job working directory is moved to the destination cluster. The file transfer may take time depending on the size of directory.

!!! warning "Files and directories with the same name"
    If there are multiple files or directories with the same name on the same path, UnionFS only shows the one located on the first branch. For example if file X exists on both clusters, `/cluster-001-home/USERNAME/X` and `/cluster-002-home/USERNAME/X`
    you would only see `/cluster-001-home/USERNAME/X`. So please do not create files and directories with the same name on the same path.
