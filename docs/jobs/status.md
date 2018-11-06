# Job Status Indicators

Jobs listed under the [Explorer](ui/explorer.md) can be in one of the following possible statuses, appearing under its corresponding letter/color badge.

!!!note "Note: explanation of clusters-related terms"
    The user is referred to [this page](/link-to-be-adjusted/setup.md) for instructions on how to operate the computing [clusters](/link-to-be-adjusted/service-levels.md#clusters-and-premium-hardware) offered on our platform. The concept of [Queue](/link-to-be-adjusted/levels-queues.md) on the  cluster is also explained in its respective page.
>>>>>>> feature/SCI-357-1

# Pre-submission

Badge: <span class="btn badge b-info border-50">P</span>

"Pre-submission" status indicates that the Job has been created as an entry in [Explorer](ui/explorer.md), but it has not been submitted to the queue of the cluster yet. It can still be edited by [opening](/entities-general/actions/open-edit.md) it under [Designer](/jobs-designer/overview.md).

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

Badge: <span class="btn badge b-default border-50">E</span>

When Job execution is terminated as a result of user intervention its status is set to "Terminated".

# Timeout

Badge: <span class="btn badge b-black border-50">E</span>

When the Job exceeded the allocated time limit, it is assigned the "Timeout" status.
