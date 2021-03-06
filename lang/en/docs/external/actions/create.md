# Create External Uploads

Creating new External Uploads follows [the general explanation](../../entities-general/actions/create.md) - clicking the "Create" button <i class="zmdi zmdi-file-plus zmdi-hc-border"></i>.

It is assumed that the uploaded files belong to a single [command-line job](../../jobs-cli/overview.md) originated outside of the Exabyte platform.

## Open Upload Dialog

Clicking "Create" as prescribed above takes the user to the Upload Dialog where the data can be uploaded. The dialog contains the following parameters. 

### Name

The name of the Job

### Job Script File

The name of (or path to) the [Job script file](../../jobs-cli/batch-scripts). Will be parsed and shown inside the job as input file after upload is complete.

### Standard Output file

The name of (or path to) the file containing the standard (textual) output. Will be parsed and shown inside the job as the outpuf file after upload is complete.

### Description

Human-readable description of the uploaded data (optional).

### File archive

The file archive containing the data. The following must be asserted:

1. the archive type is ".zip"
2. the size of the archive is less than the maximum size (as shown in the helper message)
3. the archive contains the job files at the top level

To demonstrate the last point, here's an acceptable content of the archive:

```text
# Desired archive content            
.
|____CONTCAR
|____DOSCAR
|____EIGENVAL
|____IBZKPT
|____INCAR
|____job.rms
|____KPOINTS
|____OSZICAR
|____OUTCAR
|____PCDAT
|____POSCAR
|____vasprun.xml
```

and, below is the equivalent nested structure that should be **avoided**:

```text
# Undesired content            
.
|____directory
| |____CONTCAR
| |____DOSCAR
| |____EIGENVAL
| |____IBZKPT
| |____INCAR
| |____job.rms
| |____KPOINTS
| |____OSZICAR
| |____OUTCAR
| |____PCDAT
| |____POSCAR
| |____vasprun.xml
```

!!!note "Creating an archive on a UNIX-based system"
    If we assume that `job_dir` is the folder containing the job files, the archive can be created using the following example command: `cd job_dir; zip -r9 ../archive.zip . ; cd -`

## Click "Submit"

When ready, click "Submit" button to initiate the upload.

## Demonstration

For a more detailed demonstration on how external uploads can be created consult the [corresponding tutorial](../../tutorials/other/external-upload.md) 
