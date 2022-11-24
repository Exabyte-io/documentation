# TensorMol

[TensorMol](https://github.com/jparkhill/TensorMol) is a machine learning toolkit geared towards materials science and
chemistry.

## Installation

Although we do not currently support workflows of TensorMol in the web UI, TensorMol can be easily installed to the
command line interface.

### Selecting a Version of Python and TensorFlow

TensorMol requires that the version of [TensorFlow](./tensorflow) used be released no later than v1. In other words,
TensorFlow versions starting with 1 (such as version `1.15.5`) will be compatible, but TensorFlow versions beginning
with 2 (such as `2.0.0` or `2.4.1`) will not be compatible with TensorMol.

[Whichever version](https://pypi.org/project/tensorflow/#history) of TensorFlow is installed, we recommend checking that
it is compatible with the desired version of Python. Mind, TensorFlow v1 does not support Python 3.8. In this guide, we
will focus on installing **Python 3.6.12** and the **TensorFlow 1.15.5**.

### Creating a Python Environment

TensorMol depends on specific versions of TensorFlow, which in turn requires specific versionf of Python. For this
reason, we recommend using [PyEnv](/cli/actions/customize/#via-pyenv) to install Python 3.6.12, along with a virtual
environment to store the required packages.

### Installing TensorMol's Dependencies

TensorFlow version 1.15.5 can then be installed via Pip:

```bash
python -m pip install "tensorflow<2.0" --no-cache-dir
```


Next, SciPy must be installed as a prerequisite:

```bash
python -m pip install scipy --no-cache-dir
```

### Downloading and Building TensorMol

TensorMol must be acquired from its [GitHub repository](https://github.com/jparkhill/TensorMol). We recommend creating
a `repos` directory on one of the cluster nodes, such as the [AWS cluster](/infrastructure/cluster/aws/#cluster),
cluster-001, as the clusters have more disk space than the login node:

```bash
cd ~/cluster-001
mkdir repos
git clone https://github.com/jparkhill/TensorMol.git
```
Once the repository is cloned, TensorMol can then be installed by going into its directory, and pip installing it. For 
example, if TensorMol had been cloned into `~/cluster-001/repos/TensorMol`, the following commands would complete its
installation:

```bash
cd ~/cluster-001/repos/TensorMol
pip install -e .
```
