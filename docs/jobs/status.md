# Job Status Indicators

Jobs listed under the [Explorer](ui/explorer.md) can be in one of the following possible statuses, appearing under its corresponding letter/color badge.

!!!note "Note: explanation of clusters-related terms"
    The user is referred to [this page](/infrastructure/compute-settings/ui.md) for instructions on how to operate the computing [clusters](/infrastructure/clusters/overview.md) offered on our platform. The concept of [Queue](/infrastructure/resource/queues.md) on the  cluster is also explained in its respective page.

# Pre-submission

Badge: <span class="btn badge b-info border-50">P</span>

"Pre-submission" status indicates that the Job has been created as an entry in [Explorer](ui/explorer.md), but it has not been submitted to the [queue](/infrastructure/resource/queues.md) of the cluster yet. It can still be edited by [opening](/entities-general/actions/open-edit.md) it under [Designer](/jobs-designer/overview.md).

# Submitted 

 Badge <span class="btn badge b-primary border-50">S</span>
 
 "Submitted" status means that the Job has been submitted already, but is not actively running yet.

# Active

Badge: <span class="btn badge b-warning border-50">A</span>

The "Active" status highlights the fact that the Job is currently in the process of being executed.

# Finished

Badge: <span class="btn badge b-success border-50">F</span>

When the Job is "Finished", its execution is terminated correctly (without errors) following the completion of its computational tasks.

# Error

Badge: <span class="btn badge b-danger border-50">E</span>

An "Error" status indicates that the Job execution terminated as a result of encountering a computational error.

# Terminated

Badge: <span class="btn badge b-default border-50">T</span>

When Job execution is terminated as a result of user intervention its status is set to "Terminated".

# Timeout

Badge: <span class="btn badge b-black border-50">T</span>

When the Job exceeded the allocated time limit, it is assigned the "Timeout" status.
