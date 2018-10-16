# User Dashboard

The Dashboard provides the user with an instant impression of the overall status of the system and of his own recent work. Four main component panels can be recognized in this Dashboard, consisting in the following sets of information:

<img src="/images/user-dashboard.png" > 


## 1. Jobs summary

The jobs summary widget summarizes the total number of jobs run during a certain period of time indicated at the top of the panel, and also offers a break down of the job current status between "Active", "Submitted", "Pre-submission", "Success" and "Errors". There is also a quick link to jump to the jobs list at the bottom of the panel, labelled "View All Jobs".


## 2. Compute Usage

The compute usage chart shows the combined financial cost for all the recent calculations, over the given duration of time.

## 3. Storage Quota

This widget displays a summary of the user's current data storage quota, in the form of the ratio between used and total available storage space. The user can click on the <i class="zmdi zmdi-plus-circle-o zmdi-hc-border"></i> icon at the top-right corner of the panel to request an increase in storage space. In addition, the neighbouring <i class="zmdi zmdi-refresh-sync zmdi-hc-border"></i> icon can be used to refresh the data.


## 4. Datapoints

| Datapoint             | Description
| :-------------        |:-------------
| Total charges     | Shows a summary of the total charges over all time
| Recent charges     | Shows the equivalent charges of last week for comparison
| Longest Job           | Shows compute walltime of the longest job ever performed by the user
| Current Compute Load   | Shows current server compute load (low/medium/high)
| Estimated Wait Time   | Shows an estimated wait time for compute power
