### Pre-configured submit scripts

In order to quickly get up to speed you can use our pre-configured job script examples and input files. Below are example commands needed to copy and run a job with Quantum ESPRESSO.

```bash
# make temporary directory
cd && mkdir -p job-examples/
# copy example files
cd job-examples/ && cp -r ~/job_script_templates/espresso .
# submit for execution
cd espresso && qsub job.pbs
```

This will submit an example job into the queue and schedule it for execution. You can view its status with `qstat`.
