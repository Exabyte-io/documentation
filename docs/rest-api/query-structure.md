# Request Structure

A request is an HTTP request that consists of the following:

* The URL that serves as the entry point for the web service.
* The endpoint that is executed when a request is made at a given URL path for a specific HTTP method.
* Any parameters for the endpoint, each parameter is separated by an ampersand (&).
* The API version to use. URL path versioning is the only type of API versioning currently available.
* Authentication parameters that Exabyte uses to ensure the validity and authenticity of the request.

The following is a sample request which uses `GET` method and connects to `materials` endpoint. `KuAsBRwofzGfHPWiT` specifies the material ID and `X-Auth-Token` and `X-User-Id` are authentication parameters passed inside the request header.

```bash
curl -X GET https://platform.exabyte.io/api/v1/materials/KuAsBRwofzGfHPWiT -H "X-Auth-Token: f2KpRW7KeN9aPmjSZ" -H "X-User-Id: fbdpsNf4oHiX79vMJ"
```


# Response Structure

In response to the request, the service returns a JSON data structure. All responses follow the [JSend](http://labs.omniti.com/labs/jsend) JSON format, with one minor tweak: failures have an identical structure to errors. Successful responses will have a status code of 200, unless otherwise indicated.

```json
{
  "data": {
    ...
  },
  "status": "success"
}
```

# Filter the results

Some of the endpoints support list action which uses `GET` HTTP method to return a list of items accessible under a given endpoint. The list action either returns a list of all items or the item for which the ID is passed. If you want list action to return a specific subset of items, you can use `query` parameter to filter the results. `query` is a dictionary following [Mongo Query](https://docs.mongodb.com/manual/tutorial/query-documents/) format. 

`query` parameter is passed inside URL and must be encoded.  URLs can only be sent over the Internet using the ASCII character-set. URL encoding replaces unsafe ASCII characters with a "%" followed by two hexadecimal digits. URLs cannot contain spaces. URL encoding normally replaces a space with a plus (+) sign or with %20. Please see [HTML URL Encoding Reference](https://www.w3schools.com/tags/ref_urlencode.asp) for more information. The following example lists the materials with formula equal to SiGe (`query={"formula": "SiGe"}`).

An example way of listing materials with "SiGe" chemical formula is given below:
```bash
curl -X GET https://platform.exabyte.io/api/v1/materials?query=%7B%22formula%22%3A+%22SiGe%22%7D -H "X-Auth-Token: f2KpRW7KeN9aPmjSZ" -H "X-User-Id: fbdpsNf4oHiX79vMJ"
```

# Results Pagination

The number of returned results for list action is set to 20 by default. If you want to get more results you should use `pageIndex` and `pageSize` parameters to paginate the results. `pageIndex` parameter specifies the index of the page to return while `pageSize` specifies the size of each page. `pageIndex` is an integer and `pageSize` is an integer between 5 and 100. 

For example if there are 100 materials which you want to get via 2 calls to the API, the following queries can be used:

```bash
curl -X GET https://platform.exabyte.io/api/v1/materials?pageIndex=0&pageSize=50 -H "X-Auth-Token: f2KpRW7KeN9aPmjSZ" -H "X-User-Id: fbdpsNf4oHiX79vMJ"
curl -X GET https://platform.exabyte.io/api/v1/materials?pageIndex=1&pageSize=50 -H "X-Auth-Token: f2KpRW7KeN9aPmjSZ" -H "X-User-Id: fbdpsNf4oHiX79vMJ"
```
