# Upload an External command-line Job

This page explains how to initiate an [External Upload](../../external/overview.md) to parse and organize a folder with a data from an external calculation. 
 
## Notes

In the present example we use example data from a [VASP](../../software-directory/modeling/vasp/overview.md) calculation, however the directives work for other simulation engines too.

The platform will attempt to extract the [Entities](../../entities-general/overview.md), such as [Materials](../../materials/overview.md) and [Properties](../../properties/overview.md) from the calculation data in failsafe manner.

## Prepare an archive

First, arrange all the files inside a folder. Then create a .zip archive with the data. On a UNIX-based operating system this could be done in command line or righ-hand context menu. The command-line routine could be, for example:

```bash
cd JOB_DIRECTORY
zip -r9 ../archive.zip .
``` 

## Upload archive

### Open Upload Dialog

Navigate to the [External Uploads Explorer](../../external/ui/explorer.md) page and initiate the upload task [creation](../../external/actions/create.md). Inside the Upload Dialog one can set the name of the and its human-readable description as desired. These will be used for the Job created inside the [External Project](../../jobs/projects.md#external-project) when the upload is complete.

### Fill the form data

Pay attention to the [job script file](../../external/actions/create.md#job-script-file) and the [standard output](../../external/actions/create.md#standard-output-file). They will be used as the input/output files for the job accordingly.

### Submit the dialog

Use the file selector to select the archive prepared in the previous step. When finished, click "Submit" button to initiate the upload. 

## View the External Job

### Wait for the task to finish

The [status](../../external/status.md) of the upload will be set to "A" - active, while the upload task is in progress. When the task finished, the status will change to "F" - finished.

### Navigate into External Project

In order to view the job, navigate into the list of Projects from the [Left-hand sidebar](../../ui/left-sidebar.md#), then navigate into the [External Project](../../jobs/projects.md#external-project).

### View the latest Job

The latest job inside the project is the one containing the uploaded data. The platform will attempt to extract the Materials, Properties, input/output files and administrative information about the job and make it available in the same manner as for the jobs originating inside the platform. 

## Animation

In the following animation, we demonstrate the above-mentioned steps: we create a non-nested ".zip" archive from the calculation data, upload it to the platform and view the Job (with Materials and Properties) created inside the "External" project as a result.   

<div class="video-wrapper">
<iframe class="gifffer" width="100%" height="100%" src="https://www.youtube.com/embed/oxTm1a4qnLQ" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>
