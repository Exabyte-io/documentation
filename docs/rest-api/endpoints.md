# Endpoints

Endpoint is a function which is executed when a request is made for a URL with specific HTTP method. For example contacting materials endpoint with PUT HTTP method and a material in JSON format will create the material inside the database and return the result.

The following shows a list of currently supported endpoints with links to the [Swagger](#Links) documentation, a software framework to design, build, document, and consume RESTful Web services.

- [Material](/api/?url=https://platform.exabyte.io/api/2018-10-01/swagger.json/#!/Material/get_materials)
- [Workflow](/api/?url=https://platform.exabyte.io/api/2018-10-01/swagger.json/#!/Workflow/get_workflows)
- [Job](/api/?url=https://platform.exabyte.io/api/2018-10-01/swagger.json/#!/Job/get_jobs)
- [Project](/api/?url=https://platform.exabyte.io/api/2018-10-01/swagger.json/#!/Project/get_projects)
- [Bank Material](/api/?url=https://platform.exabyte.io/api/2018-10-01/swagger.json/#!/BankMaterial/get_bank_materials)
- [Bank Workflow](/api/?url=https://platform.exabyte.io/api/2018-10-01/swagger.json/#!/BankWorkflow/get_bank_workflows)
- [Property](/api/?url=https://platform.exabyte.io/api/2018-10-01/swagger.json/#!/Property/get_refined_properties) (RefinedProperty)
- [RawProperty](/api/?url=https://platform.exabyte.io/api/2018-10-01/swagger.json/#!/RawProperty/get_raw_properties)
- [Charge](/api/?url=https://platform.exabyte.io/api/2018-10-01/swagger.json/#!/Charge/get_charges)
- [Login](/api/?url=https://platform.exabyte.io/api/2018-10-01/swagger.json/#!/API/post_login)
- [Logout](/api/?url=https://platform.exabyte.io/api/2018-10-01/swagger.json/#!/API/get_logout)

In the example animation below, we demonstrate how to use Swagger for API version 2018-10-01 to list the materials an account as access to. It is assumed that the reader has already generated the authentication parameters explained in [here](authentication.md).

<img data-gifffer="/images/swagger-list-materials.gif"/>


# API Versions

- [2018-10-01](/api/?url=https://platform.exabyte.io/api/2018-10-01/swagger.json)


# Links

- [Swagger](https://github.com/swagger-api/swagger-ui/tree/v2.2.10)
