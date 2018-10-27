# Job Status Indicators

Jobs listed under the [Explorer](ui/explorer.md) can be in one of the following possible statuses, appearing under its corresponding letter/color badge.

!!!note "Note: explanation of clusters-related terms"
    The user is referred to [this page](/compute/setup.md) for instructions on how to operate the supercomputing [clusters](/pricing/service-levels.md#clusters-and-premium-hardware) offered on our platform. The concept of [Queue](/compute/levels-queues.md) on the  cluster is also explained in its respective page.

# Pre-submission  

The "Pre-submission" status, identified with this badge <span class="btn badge border-50" style="background: #5bc0de !important;">P</span>, indicates that the Job has been created as an entry in [Explorer](ui/explorer.md), but it has not been submitted to the queue of the cluster yet. It can still be edited by [opening](/entities-general/actions/open-edit.md) it under [Designer](/jobs-designer/overview.md).

# Submitted 

The "Submitted" status, labelled with this badge <span class="btn badge border-50" style="background: #1056be !important;">S</span>, means that the Job has been submitted already, but is not actively running yet.

# Active

The "Active" status is displayed under this badge <span class="btn badge border-50" style="background: #E67E22 !important;">A</span>. It highlights the fact that the Job is currently in the process of being executed.

# Finished

When the Job is "Finished" <span class="btn badge border-50" style="background: #27AE60 !important;">F</span>, then its execution terminated correctly (without errors) following the completion of its computational tasks.

# Error

An "Error" status <span class="btn badge border-50" style="background: #E74C3C !important;">E</span> indicates that the Job execution terminated as a result of encountering a computational error.

# Terminated

When Job execution "Terminated" as a result of user intervention, then its status appears under the following badge <span class="btn badge border-50" style="background: #777 !important;">T</span>.

# Timeout

When the Job exceeded the allocated time limit, it appears under the "Timeout" badge <span class="btn badge border-50" style="background: black !important;">T</span>.
