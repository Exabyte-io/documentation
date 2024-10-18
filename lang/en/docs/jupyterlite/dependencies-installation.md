# Dependencies Installation and Imports


## Dependencies installation

To install dependencies in Pyodide, the [`micropip`](./pyodide.md) package is used.

For relative imports to work in provided in api-examples notebooks, one needs to install the `mat3ra-api-examples` package in the beginning of the notebook:

```python
import micropip

await micropip.install('mat3ra-api-examples', deps=False)
```

## Imports

To allow for relative imports like:

```python
from utils.jupyterlite import get_materials
```

Some of the necessary packages are compiled into pure Python wheels and provided inside the `mat3ra-api-examples` package. In top-level `packages` folder.
The dependencies for each notebook and default ones are listed in the [`config.yml` file]("https://github.com/Exabyte-io/api-examples/blob/5e0109589da981b60fec1c1cfcae1977abbbd8ec/config.yml") on the top-level.
To install packages required for the notebook, one can use `install_packages` function from `utils.jupyterlite` module and provide the name of the notebook and the relative path to the `config.yml` file:

```python
from utils.jupyterlite import install_packages
await install_packages("create_interface_with_min_strain_zsl.ipynb", "../../config.yml")
```
