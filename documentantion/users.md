## Create User

### Request

`GET /users/basic`

### Header:
```json
    {}
```

### Body
```json
{
    "email": "user@mail.com" ,
    "name": "user",
    "cpf" :"00000000001",
    "password": "123456",
    "is_premium": false
}
```

### Responses

```json
    HTTP/1.0 200 OK
    Content-Type	application/json
    Content-Length	234
    Server	Werkzeug/2.0.2 Python/3.9.6
    Date	Wed, 15 Dec 2021 01:40:26 GMT

    {
        "id": 1,
        "email": "user@mail.com",
        "name": "user",
        "cpf": "00000000000",
        "created_at": "Tue, 14 Dec 2021 21:37:36 GMT",
        "premium_at": null,
        "premium_expire": null,
        "is_premium": false,
        "verified": false
    }
```
#

## Login

### Request - `GET /users/login`

### Header:
```json
    {}
```

### Body
```json

    {
        "email": "user@mail.com" ,
        "password": "123456",
    }
```

### Responses

```json
    HTTP/1.0 200 OK

    Content-Type	application/json
    Content-Length	529
    Server	Werkzeug/2.0.2 Python/3.9.6
    Date	Wed, 15 Dec 2021 01:49:17 GMT


    {
	    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTYzOTUzMzU0NywianRpIjoiYTU4OTQ1NDYtNjRiZS00ZTIwLTlkM2ItNDEzYmJiZmRmN2U0IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6eyJpZCI6MjMsImVtYWlsIjoidXNlckBtYWlsLmNvbSIsIm5hbWUiOiJ1c2VyIiwiY3BmIjoiMDAwMDAwMDAwMDEiLCJjcmVhdGVkX2F0IjoiVHVlLCAxNCBEZWMgMjAyMSAyMTozNzozNiBHTVQiLCJwcmVtaXVtX2F0IjpudWxsLCJwcmVtaXVtX2V4cGlyZSI6bnVsbCwiaXNfcHJlbWl1bSI6ZmFsc2UsInZlcmlmaWVkIjpmYWxzZX0sIm5iZiI6MTYzOTUzMzU0NywiZXhwIjoxNjM5NTM0NDQ3fQ.ncwa6qUMdrPAJKBGm4VhFx2hkwRSwvQLT0eIuw1PYGU"
    }
```

```json
    HTTP/1.0 404 NOT FOUND

    Content-Type	application/json
    Content-Length	32
    Server	Werkzeug/2.0.2 Python/3.9.6
    Date	Wed, 15 Dec 2021 01:55:49 GMT


    {
	    "error": "User not found"
    }
```
```json
    HTTP/1.0 401 UNAUTHORIZED

    Content-Type	application/json
    Content-Length	35
    Server	Werkzeug/2.0.2 Python/3.9.6
    Date	Wed, 15 Dec 2021 01:56:51 GMT


    {
	    "error": "Invalid password."
    }
```
#
