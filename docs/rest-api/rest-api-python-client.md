<!-- by MM -->

exabyte-api-client is a Python package that provides access to Exabyte REST API via Python.

# How to Install

It is recommended to create a Python virtual environment before installing exabyte-api-client Python package:

```bash
virtualenv my-virtualenv
source my-virtualenv/bin/activate
```

You can install exabyte-api-client via pip in two ways:

## Install it via PyPI:

```bash
pip install exabyte-api-client
```

## Install it via source code in development mode:

```bash
git clone git@github.com:Exabyte-io/exabyte-api-client.git
cd exabyte-api-client
pip install -e .
```

# How to Use

## Obtain authentication parameters

The following Python code shows how to obtain authentication parameters. An instance of `ExabyteLoginEndpoint` class is created and required parameters are passed to its constructure. Then the `login` method of the instance is called to retrieve authentication parameters.

```python
import json
import argparse

from endpoints.login import ExabyteLoginEndpoint

HOST = 'platform.exabyte.io'
PORT = 443


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--username', required=True, help='username')
    parser.add_argument('-p', '--password', required=True, help='password')
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_arguments()
    login_endpoint = ExabyteLoginEndpoint(HOST, PORT, args.username, args.password)
    auth_params = login_endpoint.login()
    print json.dumps(auth_params, indent=4)
```

Save the above Python code in a file (`get_auth_params.py`) and run it:

```bash
python get_auth_params.py -u YOUR_USERNAME -p YOUR_PASSWORD
```

## Get the list of all materials

The following Python code shows how to get a list of materials. An instance of `ExabyteLoginEndpoint` class is created and required parameters are passed to its constructure to retrieve authentication parameters. Then an instance of `ExabyteMaterialsEndpoint` is created with obtained authentication parameters. Finally `get_materials` method is called to get the list materials.

```python
import json
import argparse

from endpoints.login import ExabyteLoginEndpoint
from endpoints.materials import ExabyteMaterialsEndpoint

HOST = 'platform.exabyte.io'
PORT = 443


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--username', required=True, help='username')
    parser.add_argument('-p', '--password', required=True, help='password')
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_arguments()
    login_endpoint = ExabyteLoginEndpoint(HOST, PORT, args.username, args.password)
    auth_params = login_endpoint.login()
    materials_endpoint = ExabyteMaterialsEndpoint(HOST, PORT, **auth_params)
    materials = materials_endpoint.get_materials()
    print json.dumps(materials, indent=4)
```

Save it in a file (`get_materials.py`) and run it:

```bash
python get_materials.py -u YOUR_USERNAME -p YOUR_PASSWORD
```

## Get a list of materials with a given formula

The following code returns a list of material with a given formula. `get_materials` method of `ExabyteMaterialsEndpoint` class is called with `query` parameter (`{'query': {'formula': 'SiGe'}}`) to filter materials with a given formula.

```python
import json
import argparse

from endpoints.login import ExabyteLoginEndpoint
from endpoints.materials import ExabyteMaterialsEndpoint

HOST = 'platform.exabyte.io'
PORT = 443


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--username', required=True, help='username')
    parser.add_argument('-p', '--password', required=True, help='password')
    parser.add_argument('-f', '--formula', required=True, help='material formula')
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_arguments()
    login_endpoint = ExabyteLoginEndpoint(HOST, PORT, args.username, args.password)
    auth_params = login_endpoint.login()
    materials_endpoint = ExabyteMaterialsEndpoint(HOST, PORT, **auth_params)
    materials = materials_endpoint.get_materials({'query': {'formula': args.formula}})
    print json.dumps(materials, indent=4)
```

Save it in a file (`get_materials_by_formula.py`) and run it:

```bash
python get_materials_by_formula.py -u YOUR_USERNAME -p YOUR_PASSWORD -f SiGe
```

!!! tip "More Information"
    exabyte-api-client source code contains more examples which show how to interact with Exabyte REST API over different endpoints. For more information about available endpoints, their parameters and responses please visit [Exabyte REST API documentation](query-structure).
