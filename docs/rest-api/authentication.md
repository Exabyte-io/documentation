# Overview

There are 2 ways to generate authentication parameters, via the `login` endpoint and from the [web application](/accounts/ui/preferences/api/).

# Login

Login endpoint is used to authenticate against REST API. It returns `accountId` and `authToken` which should be included in subsequent requests. 

```bash
curl -X POST https://platform.exabyte.io/api/2018-10-01/login -d "username=USERNAME&password=PASSWORD"
```

And the response will look like:

```json
{
    "X-Account-Id": "fbdpsNf4oHiX79vMJ",
    "X-Auth-Token": "tZ7-8vWHW3EvRHyadvl7TC3JnLrO_DlkSlK_LkicYgU"
}
```

For any endpoints that require authentication, you must include authentication parameters inside request header:

```bash
curl -X GET https://platform.exabyte.io/api/2018-10-01/materials -H "X-Account-Id: fbdpsNf4oHiX79vMJ" -H "X-Auth-Token: tZ7-8vWHW3EvRHyadvl7TC3JnLrO_DlkSlK_LkicYgU" 
```

# Logout

`logout` endpoint is used for logging a user out. If successful, the authentication parameters will be invalidated (removed from the user account) and it will not work in any subsequent requests.

```bash
curl -X POST https://platform.exabyte.io/api/2018-10-01/logout -X POST -H "X-Account-Id: fbdpsNf4oHiX79vMJ" -H "X-Auth-Token: tZ7-8vWHW3EvRHyadvl7TC3JnLrO_DlkSlK_LkicYgU"
```
