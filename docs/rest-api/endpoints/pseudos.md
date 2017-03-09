## Pseudos

`pseudos` endpoint is accessible at [https://platform.exabyte.io/api/v1/pseudos](https://platform.exabyte.io/api/v1/pseudos). The following actions are supported on `pseudos` endpoint:

### List
`GET` HTTP method is used to retrieve a list of pseudos.

<details>
    <summary>List all pseudos:</summary>
```bash
curl -X GET https://platform.exabyte.io/api/v1/pseudos -H "X-Auth-Token: f2KpRW7KeN9aPmjSZ" -H "X-User-Id: fbdpsNf4oHiX79vMJ"
```
```bash
{
  "status": "success",
  "data": [
    {
      "_id": "58b6b850fe450029c339a559",
      "textHeading": "VRHFIN =S : s2p4\n   LEXCH  = PE\n   EATOM  =   276.8230 eV,   20.3459 Ry\n\n   TITEL  = PAW_PBE S_h 08Apr2002\n   LULTRA =        F    use ultrasoft PP ?\n   IUNSCR =        1    unscreen: 0-lin 1-nonlin 2-no\n   RPACOR =    1.300    partial core radius\n   POMASS =   32.066; ZVAL   =    6.000    mass and valenz\n   RCORE  =    1.500    outmost cutoff radius\n   RWIGS  =    1.800; RWIGS  =    0.953    wigner-seitz radius (au A)\n   ENMAX  =  402.436; ENMIN  =  301.827 eV\n   ICORE  =        2    local potential\n   LCOR   =        T    correct aug charges\n   LPAW   =        T    paw PP\n   EAUG   =  491.964\n   DEXC   =    0.000\n   RMAX   =    1.528    core radius for proj-oper\n   RAUG   =    1.300    factor for augmentation sphere\n   RDEP   =    1.513    radius for radial grids\n   RDEPT  =    1.462    core radius for aug-charge\n \n   Atomic configuration\n    6 entries\n     n  l   j            E        occ.\n     1  0  0.50     -2405.8406   2.0000\n     2  0  0.50      -211.7007   2.0000\n     2  1  1.50      -156.4958   6.0000\n     3  0  0.50       -17.2562   2.0000\n     3  1  0.50        -7.0085   4.0000\n     3  2  1.50        -6.8029   0.0000\n   Description\n     l       E           TYP  RCUT    TYP  RCUT\n     0    -17.2561641     23  1.500\n     0    -11.8350928     23  1.500\n     1     -7.0085400     23  1.500\n     1      3.2596068     23  1.500\n     2     -6.8029130     23  1.500\n   Error from kinetic energy argument (eV)\n   NDATA  =      100\n   STEP   =   20.000   1.050\n  61.9      58.6      57.0      53.9      52.3      49.2      46.2      44.8\n  41.9      39.2      37.9      35.3      32.9      30.6      28.4      26.3\n  24.3      22.5      20.7      18.4      16.9      15.5      13.7      12.5\n  11.5      10.1      8.80      8.04      7.01      6.11      5.31      4.61\n  4.00      3.46      2.99      2.58      2.12      1.82      1.48      1.27\n  1.03     0.837     0.676     0.546     0.440     0.355     0.286     0.220\n 0.180     0.141     0.113     0.961E-01 0.799E-01 0.680E-01 0.574E-01 0.507E-01\n 0.451E-01 0.393E-01 0.341E-01 0.293E-01 0.248E-01 0.207E-01 0.170E-01 0.132E-01\n 0.105E-01 0.807E-02 0.626E-02 0.504E-02 0.421E-02 0.383E-02 0.362E-02 0.351E-02\n 0.340E-02 0.322E-02 0.292E-02 0.259E-02 0.219E-02 0.180E-02 0.145E-02 0.121E-02\n 0.104E-02 0.943E-03 0.887E-03 0.837E-03 0.774E-03 0.690E-03 0.593E-03 0.492E-03\n 0.409E-03 0.353E-03 0.318E-03 0.298E-03 0.275E-03 0.248E-03 0.214E-03 0.180E-03\n 0.152E-03 0.135E-03 0.124E-03 0.115E-03\n",
      "apps": [
        "vasp"
      ],
      "element": "S",
      "access": {
        "type": 0,
        "level": 0
      },
      "source": "vasp",
      "version": "5.2",
      "path": "/export/share/pseudo/s/gga/pbe/vasp/5.2/paw/h/POTCAR",
      "type": "paw",
      "exchangeCorrelation": {
        "approximation": "gga",
        "functional": "pbe"
      },
      "ppHeader": {
        "date": 1018224000,
        "zValence": 6,
        "element": "S"
      },
      "characteristics": [
        {
          "units": "eV",
          "name": "total_energy",
          "value": -4.075985
        },
        {
          "units": "eV",
          "name": "zero_point_energy",
          "value": -0.04181336382812499
        }
      ]
    }
  ]
}
```
</details>

!!! tip "Number of Returned Results"
    The number of returned results are limited to 20 by default ([Results Pagination](../query-structure/#results-pagination)).

<details>
    <summary>Get pseudo by ID:</summary>
```bash
curl -X GET https://platform.exabyte.io/api/v1/pseudos/58b6b850fe450029c339a559 -H "X-Auth-Token: f2KpRW7KeN9aPmjSZ" -H "X-User-Id: fbdpsNf4oHiX79vMJ"
```
```bash
{
  "status": "success",
  "data": {
    "_id": "58b6b850fe450029c339a559",
    "textHeading": "VRHFIN =S : s2p4\n   LEXCH  = PE\n   EATOM  =   276.8230 eV,   20.3459 Ry\n\n   TITEL  = PAW_PBE S_h 08Apr2002\n   LULTRA =        F    use ultrasoft PP ?\n   IUNSCR =        1    unscreen: 0-lin 1-nonlin 2-no\n   RPACOR =    1.300    partial core radius\n   POMASS =   32.066; ZVAL   =    6.000    mass and valenz\n   RCORE  =    1.500    outmost cutoff radius\n   RWIGS  =    1.800; RWIGS  =    0.953    wigner-seitz radius (au A)\n   ENMAX  =  402.436; ENMIN  =  301.827 eV\n   ICORE  =        2    local potential\n   LCOR   =        T    correct aug charges\n   LPAW   =        T    paw PP\n   EAUG   =  491.964\n   DEXC   =    0.000\n   RMAX   =    1.528    core radius for proj-oper\n   RAUG   =    1.300    factor for augmentation sphere\n   RDEP   =    1.513    radius for radial grids\n   RDEPT  =    1.462    core radius for aug-charge\n \n   Atomic configuration\n    6 entries\n     n  l   j            E        occ.\n     1  0  0.50     -2405.8406   2.0000\n     2  0  0.50      -211.7007   2.0000\n     2  1  1.50      -156.4958   6.0000\n     3  0  0.50       -17.2562   2.0000\n     3  1  0.50        -7.0085   4.0000\n     3  2  1.50        -6.8029   0.0000\n   Description\n     l       E           TYP  RCUT    TYP  RCUT\n     0    -17.2561641     23  1.500\n     0    -11.8350928     23  1.500\n     1     -7.0085400     23  1.500\n     1      3.2596068     23  1.500\n     2     -6.8029130     23  1.500\n   Error from kinetic energy argument (eV)\n   NDATA  =      100\n   STEP   =   20.000   1.050\n  61.9      58.6      57.0      53.9      52.3      49.2      46.2      44.8\n  41.9      39.2      37.9      35.3      32.9      30.6      28.4      26.3\n  24.3      22.5      20.7      18.4      16.9      15.5      13.7      12.5\n  11.5      10.1      8.80      8.04      7.01      6.11      5.31      4.61\n  4.00      3.46      2.99      2.58      2.12      1.82      1.48      1.27\n  1.03     0.837     0.676     0.546     0.440     0.355     0.286     0.220\n 0.180     0.141     0.113     0.961E-01 0.799E-01 0.680E-01 0.574E-01 0.507E-01\n 0.451E-01 0.393E-01 0.341E-01 0.293E-01 0.248E-01 0.207E-01 0.170E-01 0.132E-01\n 0.105E-01 0.807E-02 0.626E-02 0.504E-02 0.421E-02 0.383E-02 0.362E-02 0.351E-02\n 0.340E-02 0.322E-02 0.292E-02 0.259E-02 0.219E-02 0.180E-02 0.145E-02 0.121E-02\n 0.104E-02 0.943E-03 0.887E-03 0.837E-03 0.774E-03 0.690E-03 0.593E-03 0.492E-03\n 0.409E-03 0.353E-03 0.318E-03 0.298E-03 0.275E-03 0.248E-03 0.214E-03 0.180E-03\n 0.152E-03 0.135E-03 0.124E-03 0.115E-03\n",
    "apps": [
      "vasp"
    ],
    "element": "S",
    "access": {
      "type": 0,
      "level": 0
    },
    "source": "vasp",
    "version": "5.2",
    "path": "/export/share/pseudo/s/gga/pbe/vasp/5.2/paw/h/POTCAR",
    "type": "paw",
    "exchangeCorrelation": {
      "approximation": "gga",
      "functional": "pbe"
    },
    "ppHeader": {
      "date": 1018224000,
      "zValence": 6,
      "element": "S"
    },
    "characteristics": [
      {
        "units": "eV",
        "name": "total_energy",
        "value": -4.075985
      },
      {
        "units": "eV",
        "name": "zero_point_energy",
        "value": -0.04181336382812499
      }
    ]
  }
}
```
</details>

<details>
    <summary>Get pseudo by a property. The original query before encoding is `query={"type": "paw"}`:</summary>
```bash
curl -X GET https://platform.exabyte.io/api/v1/pseudos?query%3D%7B%22type%22%3A+%22paw%22%7D -H "X-Auth-Token: f2KpRW7KeN9aPmjSZ" -H "X-User-Id: fbdpsNf4oHiX79vMJ"
```
```bash
{
  "status": "success",
  "data": {
    "_id": "58b6b850fe450029c339a559",
    "textHeading": "VRHFIN =S : s2p4\n   LEXCH  = PE\n   EATOM  =   276.8230 eV,   20.3459 Ry\n\n   TITEL  = PAW_PBE S_h 08Apr2002\n   LULTRA =        F    use ultrasoft PP ?\n   IUNSCR =        1    unscreen: 0-lin 1-nonlin 2-no\n   RPACOR =    1.300    partial core radius\n   POMASS =   32.066; ZVAL   =    6.000    mass and valenz\n   RCORE  =    1.500    outmost cutoff radius\n   RWIGS  =    1.800; RWIGS  =    0.953    wigner-seitz radius (au A)\n   ENMAX  =  402.436; ENMIN  =  301.827 eV\n   ICORE  =        2    local potential\n   LCOR   =        T    correct aug charges\n   LPAW   =        T    paw PP\n   EAUG   =  491.964\n   DEXC   =    0.000\n   RMAX   =    1.528    core radius for proj-oper\n   RAUG   =    1.300    factor for augmentation sphere\n   RDEP   =    1.513    radius for radial grids\n   RDEPT  =    1.462    core radius for aug-charge\n \n   Atomic configuration\n    6 entries\n     n  l   j            E        occ.\n     1  0  0.50     -2405.8406   2.0000\n     2  0  0.50      -211.7007   2.0000\n     2  1  1.50      -156.4958   6.0000\n     3  0  0.50       -17.2562   2.0000\n     3  1  0.50        -7.0085   4.0000\n     3  2  1.50        -6.8029   0.0000\n   Description\n     l       E           TYP  RCUT    TYP  RCUT\n     0    -17.2561641     23  1.500\n     0    -11.8350928     23  1.500\n     1     -7.0085400     23  1.500\n     1      3.2596068     23  1.500\n     2     -6.8029130     23  1.500\n   Error from kinetic energy argument (eV)\n   NDATA  =      100\n   STEP   =   20.000   1.050\n  61.9      58.6      57.0      53.9      52.3      49.2      46.2      44.8\n  41.9      39.2      37.9      35.3      32.9      30.6      28.4      26.3\n  24.3      22.5      20.7      18.4      16.9      15.5      13.7      12.5\n  11.5      10.1      8.80      8.04      7.01      6.11      5.31      4.61\n  4.00      3.46      2.99      2.58      2.12      1.82      1.48      1.27\n  1.03     0.837     0.676     0.546     0.440     0.355     0.286     0.220\n 0.180     0.141     0.113     0.961E-01 0.799E-01 0.680E-01 0.574E-01 0.507E-01\n 0.451E-01 0.393E-01 0.341E-01 0.293E-01 0.248E-01 0.207E-01 0.170E-01 0.132E-01\n 0.105E-01 0.807E-02 0.626E-02 0.504E-02 0.421E-02 0.383E-02 0.362E-02 0.351E-02\n 0.340E-02 0.322E-02 0.292E-02 0.259E-02 0.219E-02 0.180E-02 0.145E-02 0.121E-02\n 0.104E-02 0.943E-03 0.887E-03 0.837E-03 0.774E-03 0.690E-03 0.593E-03 0.492E-03\n 0.409E-03 0.353E-03 0.318E-03 0.298E-03 0.275E-03 0.248E-03 0.214E-03 0.180E-03\n 0.152E-03 0.135E-03 0.124E-03 0.115E-03\n",
    "apps": [
      "vasp"
    ],
    "element": "S",
    "access": {
      "type": 0,
      "level": 0
    },
    "source": "vasp",
    "version": "5.2",
    "path": "/export/share/pseudo/s/gga/pbe/vasp/5.2/paw/h/POTCAR",
    "type": "paw",
    "exchangeCorrelation": {
      "approximation": "gga",
      "functional": "pbe"
    },
    "ppHeader": {
      "date": 1018224000,
      "zValence": 6,
      "element": "S"
    },
    "characteristics": [
      {
        "units": "eV",
        "name": "total_energy",
        "value": -4.075985
      },
      {
        "units": "eV",
        "name": "zero_point_energy",
        "value": -0.04181336382812499
      }
    ]
  }
}
```
</details>


## Create

`POST` HTTP method is used to create a new pseudo (upload a UPF file).

<details>
    <summary>Create a new pseudo:</summary>
```bash
curl -X POST https://platform.exabyte.io/api/v1/pseudos?approximation=gga&functional=pbe&method=us&application=espresso -H "X-Auth-Token: f2KpRW7KeN9aPmjSZ" -H "X-User-Id: fbdpsNf4oHiX79vMJ" -F "pseudoFile=@/path/to/your/upfFile.UPF"
```
```bash
{
  "status": "success",
  "data": {
    "_id": "58b6b850fe450029c339a559",
    "textHeading": "VRHFIN =S : s2p4\n   LEXCH  = PE\n   EATOM  =   276.8230 eV,   20.3459 Ry\n\n   TITEL  = PAW_PBE S_h 08Apr2002\n   LULTRA =        F    use ultrasoft PP ?\n   IUNSCR =        1    unscreen: 0-lin 1-nonlin 2-no\n   RPACOR =    1.300    partial core radius\n   POMASS =   32.066; ZVAL   =    6.000    mass and valenz\n   RCORE  =    1.500    outmost cutoff radius\n   RWIGS  =    1.800; RWIGS  =    0.953    wigner-seitz radius (au A)\n   ENMAX  =  402.436; ENMIN  =  301.827 eV\n   ICORE  =        2    local potential\n   LCOR   =        T    correct aug charges\n   LPAW   =        T    paw PP\n   EAUG   =  491.964\n   DEXC   =    0.000\n   RMAX   =    1.528    core radius for proj-oper\n   RAUG   =    1.300    factor for augmentation sphere\n   RDEP   =    1.513    radius for radial grids\n   RDEPT  =    1.462    core radius for aug-charge\n \n   Atomic configuration\n    6 entries\n     n  l   j            E        occ.\n     1  0  0.50     -2405.8406   2.0000\n     2  0  0.50      -211.7007   2.0000\n     2  1  1.50      -156.4958   6.0000\n     3  0  0.50       -17.2562   2.0000\n     3  1  0.50        -7.0085   4.0000\n     3  2  1.50        -6.8029   0.0000\n   Description\n     l       E           TYP  RCUT    TYP  RCUT\n     0    -17.2561641     23  1.500\n     0    -11.8350928     23  1.500\n     1     -7.0085400     23  1.500\n     1      3.2596068     23  1.500\n     2     -6.8029130     23  1.500\n   Error from kinetic energy argument (eV)\n   NDATA  =      100\n   STEP   =   20.000   1.050\n  61.9      58.6      57.0      53.9      52.3      49.2      46.2      44.8\n  41.9      39.2      37.9      35.3      32.9      30.6      28.4      26.3\n  24.3      22.5      20.7      18.4      16.9      15.5      13.7      12.5\n  11.5      10.1      8.80      8.04      7.01      6.11      5.31      4.61\n  4.00      3.46      2.99      2.58      2.12      1.82      1.48      1.27\n  1.03     0.837     0.676     0.546     0.440     0.355     0.286     0.220\n 0.180     0.141     0.113     0.961E-01 0.799E-01 0.680E-01 0.574E-01 0.507E-01\n 0.451E-01 0.393E-01 0.341E-01 0.293E-01 0.248E-01 0.207E-01 0.170E-01 0.132E-01\n 0.105E-01 0.807E-02 0.626E-02 0.504E-02 0.421E-02 0.383E-02 0.362E-02 0.351E-02\n 0.340E-02 0.322E-02 0.292E-02 0.259E-02 0.219E-02 0.180E-02 0.145E-02 0.121E-02\n 0.104E-02 0.943E-03 0.887E-03 0.837E-03 0.774E-03 0.690E-03 0.593E-03 0.492E-03\n 0.409E-03 0.353E-03 0.318E-03 0.298E-03 0.275E-03 0.248E-03 0.214E-03 0.180E-03\n 0.152E-03 0.135E-03 0.124E-03 0.115E-03\n",
    "apps": [
      "vasp"
    ],
    "element": "S",
    "access": {
      "type": 0,
      "level": 0
    },
    "source": "vasp",
    "version": "5.2",
    "path": "/export/share/pseudo/s/gga/pbe/vasp/5.2/paw/h/POTCAR",
    "type": "paw",
    "exchangeCorrelation": {
      "approximation": "gga",
      "functional": "pbe"
    },
    "ppHeader": {
      "date": 1018224000,
      "zValence": 6,
      "element": "S"
    },
    "characteristics": [
      {
        "units": "eV",
        "name": "total_energy",
        "value": -4.075985
      },
      {
        "units": "eV",
        "name": "zero_point_energy",
        "value": -0.04181336382812499
      }
    ]
  }
}
```
</details>

### Delete

`DELETE` HTTP method is used to delete an existing pseudos with a given ID.

<details>
    <summary>Delete a pseudo:</summary>
```bash
curl -X DELETE https://platform.exabyte.io/api/v1/pseudos/RhCFP2WuehvG4hCLp
```
```bash
{
  "status": "success",
  "data": {
    "message": "Pseudo RhCFP2WuehvG4hCLp successfully deleted"
  }
}
```
</details>
