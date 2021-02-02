# TensorFlow
[TensorFlow](https://www.tensorflow.org/) is a powerful open-source machine learning platform geared towards neural networks.

## Installation Instructions

Although we do not yet have a module file available to run TensorFlow, it can easily be installed to your user environment.

### Selecting Versions for Python and TensorFlow

Keep in mind that TensorFlow's development is rapidly evolving, and thus its dependencies can suddenly change in new versions.
We recommend checking the [official TensorFlow documentation](https://www.tensorflow.org/install/pip) to verify that the
version of Python and version of TensorFlow selected are compatible with one-another. Further notes:
  * [TensorFlow versions 1.X](https://pypi.org/project/tensorflow/1.15.5/) 
 are only compatible with Python releases earlier than Python 3.7.
  * Python 3.8 is only supported by [TensorFlow versions 2.2](https://www.tensorflow.org/install/pip) and later.

### Creating a Virtual Environment

To maximize predictibility and control over the python environment,
we recommend using [PyEnv](/cli/actions/customize/#via-pyenv) to set up a Python virtual environment containing
the desired version of Python.

### Installing TensorFlow

Once the desired version of Python has been installed, and its virtual environment has been activated, TensorFlow can
be installed via pip:

`python -m pip install tensorflow --no-cache-dir`

Or, if a specific version of TensorFlow is desired (for example, version `2.4.1`):

`python -m pip install tensorflow==2.4.1`
