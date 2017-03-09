<!-- by MM -->

## Request Structure

A request is an HTTP request that consists of the following:

* The URL that serves as the entry point for the web service.

* The endpoint that is executed when a request is made at a given URL path for a specific HTTP method.

* Any parameters for the endpoint, each parameter is separated by an ampersand (&).

* The API version to use. URL path versioning is the only type of API versioning currently available.

* Authentication parameters that Exabyte uses to ensure the validity and authenticity of the request.

The following is a sample request which uses `GET` HTTP method, connects to `https://platform.exabyte.io/api` on `materials` endpoint. `KuAsBRwofzGfHPWiT` specifies the material ID and `X-Auth-Token` and `X-User-Id` are authentication parameters passed inside request header.

```bash
curl -X GET https://platform.exabyte.io/api/v1/materials/KuAsBRwofzGfHPWiT -H "X-Auth-Token: f2KpRW7KeN9aPmjSZ" -H "X-User-Id: fbdpsNf4oHiX79vMJ"
```


## Response Structure

In response to the request, the service returns an JSON data structure. The structure of an JSON response is specific to the associated request. All responses follow the [JSend](http://labs.omniti.com/labs/jsend) format, with one minor tweak: failures have an identical structure to errors. Successful responses will have a status code of 200, unless otherwise indicated. Sample response to the above request is included below:

<details>
  <summary>Response</summary>
```bash
{
  "data": {
    "_id": "KuAsBRwofzGfHPWiT",
    "access": {
      "level": 20,
      "type": 0
    },
    "basis": {
      "coordinates": [
        {
          "id": 1,
          "value": [
            0,
            0,
            0
          ]
        },
        {
          "id": 2,
          "value": [
            0.25,
            0.25,
            0.25
          ]
        }
      ],
      "elements": [
        {
          "id": 1,
          "value": "Si"
        },
        {
          "id": 2,
          "value": "Ge"
        }
      ],
      "name": "basis",
      "units": "crystal"
    },
    "createdAt": "2016-10-29T03:44:21.162Z",
    "derivedProperties": {
      "symmetry": {
        "spaceGroup": "F-43m"
      }
    },
    "editable": false,
    "elements": [
      "Si",
      "Ge"
    ],
    "exabyteId": "tnnXu2d3pkWf9Ypc3",
    "formula": "SiGe",
    "hash": "72ac9a1f4b487390c88673c2358c8930",
    "lattice": {
      "a": 3.867,
      "alpha": 60,
      "b": 3.867,
      "beta": 60,
      "c": 3.867,
      "gamma": 60,
      "type": "FCC",
      "units": {
        "angle": "degree",
        "length": "angstrom"
      },
      "vectors": {
        "a": [
          3.867,
          0,
          0
        ],
        "alat": 1,
        "b": [
          1.9335000000000004,
          3.3489202364344242,
          0
        ],
        "c": [
          1.9335000000000004,
          1.1163067454781415,
          3.1573922784475164
        ],
        "name": "lattice vectors",
        "units": "angstrom"
      }
    },
    "mainDep": {
      "_dependentsById": {}
    },
    "nElements": 2,
    "nSites": 2,
    "name": "Silicon FCC",
    "owner": {
      "_id": "jnLJpf9vJKYtFoQxc",
      "name": "exadmin",
      "type": 0
    },
    "tags": [],
    "unitCellFormula": "SiGe",
    "updatedAt": "2016-10-29T03:44:40.994Z"
  },
  "status": "success"
}
```
</details>

## Filter the results

Some of the endpoints support list action which uses `GET` HTTP method to return a list of items accessible under a given endpoint. The list action either returns a list of all items or the item for which the ID is passed. If you want list action to return an specific subset of items, you can use `query` parameter to filter the results. query is a dictionary following [Mongo Query](https://docs.mongodb.com/manual/tutorial/query-documents/) format. `query` parameter is passed inside URL and must be encoded.  URLs can only be sent over the Internet using the ASCII character-set. URL encoding replaces unsafe ASCII characters with a "%" followed by two hexadecimal digits. URLs cannot contain spaces. URL encoding normally replaces a space with a plus (+) sign or with %20. Please see [HTML URL Encoding Reference](https://www.w3schools.com/tags/ref_urlencode.asp) for more information. The following example lists the materials with formula equal to SiGe (`query={"formula": "SiGe"}`).

<details>
  <summary>List materials with SiGe formula:</summary>
```bash
curl -X GET https://platform.exabyte.io/api/v1/materials?query=%7B%22formula%22%3A+%22SiGe%22%7D -H "X-Auth-Token: f2KpRW7KeN9aPmjSZ" -H "X-User-Id: fbdpsNf4oHiX79vMJ"
```
```bash
{
  "data": {
    "_id": "KuAsBRwofzGfHPWiT",
    "access": {
      "level": 20,
      "type": 0
    },
    "basis": {
      "coordinates": [
        {
          "id": 1,
          "value": [
            0,
            0,
            0
          ]
        },
        {
          "id": 2,
          "value": [
            0.25,
            0.25,
            0.25
          ]
        }
      ],
      "elements": [
        {
          "id": 1,
          "value": "Si"
        },
        {
          "id": 2,
          "value": "Ge"
        }
      ],
      "name": "basis",
      "units": "crystal"
    },
    "createdAt": "2016-10-29T03:44:21.162Z",
    "derivedProperties": {
      "symmetry": {
        "spaceGroup": "F-43m"
      }
    },
    "editable": false,
    "elements": [
      "Si",
      "Ge"
    ],
    "exabyteId": "tnnXu2d3pkWf9Ypc3",
    "formula": "SiGe",
    "hash": "72ac9a1f4b487390c88673c2358c8930",
    "lattice": {
      "a": 3.867,
      "alpha": 60,
      "b": 3.867,
      "beta": 60,
      "c": 3.867,
      "gamma": 60,
      "type": "FCC",
      "units": {
        "angle": "degree",
        "length": "angstrom"
      },
      "vectors": {
        "a": [
          3.867,
          0,
          0
        ],
        "alat": 1,
        "b": [
          1.9335000000000004,
          3.3489202364344242,
          0
        ],
        "c": [
          1.9335000000000004,
          1.1163067454781415,
          3.1573922784475164
        ],
        "name": "lattice vectors",
        "units": "angstrom"
      }
    },
    "mainDep": {
      "_dependentsById": {}
    },
    "nElements": 2,
    "nSites": 2,
    "name": "Silicon FCC",
    "owner": {
      "_id": "jnLJpf9vJKYtFoQxc",
      "name": "exadmin",
      "type": 0
    },
    "tags": [],
    "unitCellFormula": "SiGe",
    "updatedAt": "2016-10-29T03:44:40.994Z"
  },
  "status": "success"
}
```
</details>


## Results Pagination

The number of returned results for list action is set to 20 by default. If you want to get more results you should use `pageIndex` and `pageSize` parameters to paginate the results. `pageIndex` parameter specifies the index of the page to return while `pageSize` specifies the size of each page. `pageIndex` is an integer and `pageSize` is an integer between 5 and 100. For example if there are 100 materials which you want to get via 2 calls to the API, use the following queries:

```bash
curl -X GET https://platform.exabyte.io/api/v1/materials?pageIndex=0&pageSize=50 -H "X-Auth-Token: f2KpRW7KeN9aPmjSZ" -H "X-User-Id: fbdpsNf4oHiX79vMJ"
curl -X GET https://platform.exabyte.io/api/v1/materials?pageIndex=1&pageSize=50 -H "X-Auth-Token: f2KpRW7KeN9aPmjSZ" -H "X-User-Id: fbdpsNf4oHiX79vMJ"
```
