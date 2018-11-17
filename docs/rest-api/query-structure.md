# Request Structure

A request is an HTTP request that consists of the following parts.

* **URL**: the entry point for the web service.
* **Endpoint**: a function to execute for a specific URL and HTTP method.
* **Parameters**: parameters pass to the endpoint separated by an ampersand (&).
* **API version**: version of the API. Only URL path versioning is currently supported.
* **Authentication parameters**: credentials to ensure the validity and authenticity of the request.

The following is a sample request which uses `GET` method and connects to `materials` endpoint. `KuAsBRwofzGfHPWiT` specifies the material ID and `X-Auth-Token` and `X-Account-Id` are authentication parameters passed inside the request header.

```bash
curl -X GET https://platform.exabyte.io/api/2018-10-01/materials/KuAsBRwofzGfHPWiT -H "X-Account-Id: fbdpsNf4oHiX79vMJ" -H "X-Auth-Token: tZ7-8vWHW3EvRHyadvl7TC3JnLrO_DlkSlK_LkicYgU"
```

## Response Structure

In response to the request, the service returns a JSON data structure. All responses follow the [JSend](http://labs.omniti.com/labs/jsend) JSON format, with one minor tweak: failures have an identical structure to errors. Successful responses will have a status code of 200, unless otherwise indicated.

```json
{
  "data": {
    ...
  },
  "status": "success"
}
```

## Filter Results

Some of the endpoints support list action which uses `GET` HTTP method to return a list of items accessible under a given endpoint. The list action either returns a list of all items or the item for which the ID is passed. If you want list action to return a specific subset of items, you can use `query`  and `projection` parameters to filter the results.

### Query

`query` parameter is a JSON object following [Mongo Query](https://docs.mongodb.com/manual/tutorial/query-documents/) format. It is passed inside URL and must be encoded.  URLs can only be sent over the Internet using the ASCII character-set. URL encoding replaces unsafe ASCII characters with a "%" followed by two hexadecimal digits. URLs cannot contain spaces. URL encoding normally replaces a space with a plus (+) sign or with %20. Please see [HTML URL Encoding Reference](https://www.w3schools.com/tags/ref_urlencode.asp) for more information. The following example lists the materials with formula equal to SiGe (`query={"formula": "SiGe"}`).

An example way of listing materials with "SiGe" chemical formula is given below:
```bash
curl -X GET https://platform.exabyte.io/api/2018-10-01/materials?query=%7B%22formula%22%3A+%22SiGe%22%7D -H "X-Account-Id: fbdpsNf4oHiX79vMJ" -H "X-Auth-Token: tZ7-8vWHW3EvRHyadvl7TC3JnLrO_DlkSlK_LkicYgU"
```

### Projection

[`projection`](https://docs.meteor.com/api/collections.html#Mongo-Collection-find) is a JSON object with the following keys to limit, paginate, or modify the results.

- **sort**: sort order (default: natural order)

- **skip**: number of results to skip at the beginning

- **limit**: maximum number of results to return. Must be equal or less than 500. Defaults to 50.

- **fields**: dictionary of fields to return or exclude, for example {"name": 1} only returns `name` field.

`projection` parameter is passed inside the URL and must be encoded similar to `query` parameter.

For example if there are 200 materials which you want to get via 2 calls to the API, the following projections can be used:

- {"limit": 100}
- {"skip": 100, "limit": 100}

```bash
curl -X GET https://platform.exabyte.io/api/2018-10-01/materials?projection=%7B%22limit%22%3A+50%7D  -H "X-Account-Id: fbdpsNf4oHiX79vMJ" -H "X-Auth-Token: tZ7-8vWHW3EvRHyadvl7TC3JnLrO_DlkSlK_LkicYgU"
curl -X GET https://platform.exabyte.io/api/2018-10-01/materials?projection=%7B%22skip%22%3A+50%2C+%22limit%22%3A+50%7D  -H "X-Account-Id: fbdpsNf4oHiX79vMJ" -H "X-Auth-Token: tZ7-8vWHW3EvRHyadvl7TC3JnLrO_DlkSlK_LkicYgU"
```

## Links

<!-- TODO by MM: move link to mongoDb, HTML URL Encoding, JSend here and use footnotes -->