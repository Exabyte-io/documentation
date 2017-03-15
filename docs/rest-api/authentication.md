<!-- by MM -->

## Logging In

login endpoint is used to authenticate against REST API. It returns `userId` and `authToken` which should be included in subsequent requests. There are 2 ways to get authentication parameters, via the `login` endpoint and from web application:

```bash
curl -X POST https://platform.exabyte.io/api/v1/login -d "username=USERNAME&password=PASSWORD"
```

The password can be SHA-256 hashed on the client side, in which case your request would look like:

```bash
curl -X POST https://platform.exabyte.io/api/v1/login -d "username=USERNAME&password=HASHED_PASSWORD&hashed=true"
```

And the response will look like:

```json
{
    "data": {
        "authToken": "f2KpRW7KeN9aPmjSZ",
        "userId": "fbdpsNf4oHiX79vMJ"
    },
    "status": "success"
}
```

![Authentication parameters](/images/auth-params.gif "Authentication parameters")

### Authenticated Calls

For any endpoints that require authentication, you must include the `userId` and `authToken` with each request,

Either under the following headers:

* `X-User-Id`
* `X-Auth-Token`

```bash
curl -X GET https://platform.exabyte.io/api/v1/materials -H "X-Auth-Token: f2KpRW7KeN9aPmjSZ" -H "X-User-Id: fbdpsNf4oHiX79vMJ"
```

Or via following URL parameters:

* `userId`
* `authToken`

```bash
curl -X GET https://platform.exabyte.io/api/v1/materials?authToken=f2KpRW7KeN9aPmjSZ&userId=fbdpsNf4oHiX79vMJ"
```

## Logging Out

`logout` endpoint is used for logging a user out. If successful, the authentication parameters will be invalidated (removed from the user account) and it will not work in any subsequent requests.

```bash
curl -X POST https://platform.exabyte.io/api/v1/logout -X POST -H "X-Auth-Token: f2KpRW7KeN9aPmjSZ" -H "X-User-Id: fbdpsNf4oHiX79vMJ"
```
