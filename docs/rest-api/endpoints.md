# Endpoints

## Definition

An Endpoint is one end of a communication channel, the API end of it. It has a unique URL and a set of parameters associated with it. Sending a request with a specific HTTP[^1] method to an Endpoint triggers a certain function. 

!!! example
    Contacting materials endpoint with a PUT HTTP method and the corresponding data about a material will lead to the creation of the corresponding [Material](../materials/overview.md) inside the database and return the result.

## List of Endpoints

Below is the list of currently supported endpoints with links to the detailed documentation for each.

- [Material](../api/?url=https://platform.exabyte.io/api/2018-10-01/swagger.json/#!/Material/get_materials)
- [Workflow](../api/?url=https://platform.exabyte.io/api/2018-10-01/swagger.json/#!/Workflow/get_workflows)
- [Job](../api/?url=https://platform.exabyte.io/api/2018-10-01/swagger.json/#!/Job/get_jobs)
- [Project](../api/?url=https://platform.exabyte.io/api/2018-10-01/swagger.json/#!/Project/get_projects)
- [Bank Material](../api/?url=https://platform.exabyte.io/api/2018-10-01/swagger.json/#!/BankMaterial/get_bank_materials)
- [Bank Workflow](../api/?url=https://platform.exabyte.io/api/2018-10-01/swagger.json/#!/BankWorkflow/get_bank_workflows)
- [Property](../api/?url=https://platform.exabyte.io/api/2018-10-01/swagger.json/#!/Property/get_refined_properties) (RefinedProperty)
- [RawProperty](../api/?url=https://platform.exabyte.io/api/2018-10-01/swagger.json/#!/RawProperty/get_raw_properties)
- [Charge](../api/?url=https://platform.exabyte.io/api/2018-10-01/swagger.json/#!/Charge/get_charges)
- [Login](../api/?url=https://platform.exabyte.io/api/2018-10-01/swagger.json/#!/API/post_login)
- [Logout](../api/?url=https://platform.exabyte.io/api/2018-10-01/swagger.json/#!/API/get_logout)

## Endpoint Documentation

In order to explain the data formats and allow users to try the endpoints we use Swagger UI[^2], a software framework to design, build, document, and try API services. In the example below, we demonstrate how to use the framework to list the materials an account has access to. It is assumed that the reader has already generated the authentication parameters explained in [here](authentication.md).

1. Open [Swagger UI](../api) page.

2. Set `X-ACCOUNT-ID` and `X-AUTH-TOKEN` authentication parameters.

3. Navigate to `Materials` endpoint, set up [query](./query-structure.md#query) (`{"formula": "Si"}`) and [projection](./query-structure.md#projection) (`{"limit": 5}`) parameters.
 
4. Click on `RESPONSE EXAMPLE` and `RESPONSE SCHEMA` on the right panel to see an example response and its structure (schema).

5. Click on `Try` to connect to the RESTful API and retrieve the materials.

6. A list of materials filtered by the given query and projection parameters will be returned.

The aforementioned steps are demonstrated in the animation below.

<img data-gifffer="/images/swagger-list-materials.gif"/>


## API Versions

Below you can find the currently supported API versions.

- [2018-10-01](../api/?url=https://platform.exabyte.io/api/2018-10-01/swagger.json)


## Links

[^1]: [Hypertext Transfer Protocol (HTTP), Wikipedia](https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol)

[^2]: [Swagger UI, GitHub](https://github.com/swagger-api/swagger-ui/tree/v2.2.10)

///FOOTNOTES GO HERE///
