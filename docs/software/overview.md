# Application

The "Application" entity concept relates to the computational engine (otherwise known as software application) to employ for the execution of a simulation. 

## [Supported Applications]()

The platform currently offers the choice between the following software engines, some of which (Quantum ESPRESSO and VASP, for instance) have extensive integrated support in the user interface, and others are currently available through command line terminal connection. Click on the name of the application below to navigate to the corresponding part of the documentation.

| Name    |  Version(s)      | Notes      |
| :-------- |:----------- |:------------- |
| [Quantum ESPRESSO](modeling/quantum-espresso.md) | 5.1-6.0 | Fully integrated |
| [VASP](modeling/vasp.md)      | 5.3.5-5.4.4 | Fully integrated (*) |
| LAMMPS    | 11-2016 | Available through command line |
| NWChem    | 6.6     | Available through command line |
| CP2K      | 4.1     | Available through command line |
| Turbomole | 7.0     | Available through remote desktop |

> * VASP is available for current licensees and on-demand for users with academic affiliations

## [Structural Analysis Tools]()

### [Visual]()

We support the following structural analysis tools through a remote desktop connection.

| Name      |  Version(s) | Notes         |
| :-------- |:----------- |:------------- |
| VESTA     | 3.3.8       | Available through remote desktop |
| VMD       | 1.9.3       | Available through remote desktop |
| XCrysDen  | 1.5.60      | Available through remote desktop |

### [Python-based]()

For command-line users we provide system system-default python installation (version 2.7.5) and suggest for users to employ virtual environment [[1]](#links) for controlling the versions for python packages as explained below.

#### [Virtual Environment]()

Here is an example quick setup for a python virtual environment with pymatgen [[2]](#links), a widely used package for materials analysis.

```bash
mkdir pymatgen project
virtualenv .virtualenv
source ./virtualenv/bin/activate
pip install -r pymatgen==2018.8.10
```

## Links

1. [Python Virtual Environment](https://docs.python-guide.org/dev/virtualenvs/#lower-level-virtualenv)
2. [Pymatgen, Official Webpage](http://pymatgen.org/)
