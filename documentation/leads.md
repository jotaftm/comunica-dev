## Criar Leads

### Request

`POST /leads`

#

`Content-Type application/json`

### Header:

```json
{}
```

### Body

```json
{
  "email": "jota_lead@mail.com",
  "name": "Jota Lead"
}
```

### Responses

```json
    HTTP/1.0 201 CREATED
    Content-Type: application/json
    Content-Length: 143
    Server: Werkzeug/2.0.2 Python/3.9.6
    Date: Thu, 16 Dec 2021 13:49:36 GMT

    {
        "id": 6,
        "email": "jota_lead@mail.com",
        "name": "Jota Lead",
        "created_at": "Thu, 16 Dec 2021 10:44:06 GMT",
        "is_user": false
    }

    * Se o usuário não informar email e name; se passar 3 campos, ou se email e name não forem do tipo string:
    {
        "error": "Request body must contain only email and name fields, and both must be of type string"
    }, 400(BAD REQUEST)

    * Se o lead já existir na base de datos:
    {
        "error": "Lead already exists"
    }, 409 (CONFLICT)
```

#

### Listar todos os leads

`GET /leads`

### Header:

```json
    Autorization: Bearer [adm_token]
```

### Body

```json
{}
```

### Responses

```json
    HTTP/1.0 200 OK
    Content-Type: application/json
    Content-Length: 505
    Server: Werkzeug/2.0.2 Python/3.9.6
    Date: Thu, 16 Dec 2021 14:02:50 GMT

    [
        {
            "id": 3,
            "email": "luiz_federico@yahoo.com.br",
            "name": "Luiz Federico",
            "created_at": "Wed, 15 Dec 2021 22:20:14 GMT",
            "is_user": false
        },
        {
            "id": 5,
            "email": "rodrigo.santos@yahoo.com.br",
            "name": "Rodrigo Santos",
            "created_at": "Wed, 15 Dec 2021 22:20:14 GMT",
            "is_user": false
        },
        {
            "id": 6,
            "email": "jota_lead@mail.com",
            "name": "Jota Lead",
            "created_at": "Thu, 16 Dec 2021 10:44:06 GMT",
            "is_user": false
        }
    ]

    * se o user role não for admin:
    {
        "error": "Exclusive resource for admin."
    }, 401 (UNAUTHORIZED)
```

# Update leads

### Request

`UPDATE /leads/<int:id>`

#

`Content-Type application/json`

### Header:

```json
    Autorization: Bearer [adm_token]
```

### Body

```json
    * usuário pode atualizar todos os campos de uma só vez, ou somente um dos campos:
    {
        "email": "jota_lead@mail.com",
        "name": "Jota Lead"
    }
```

### Responses

```json
    HTTP/1.0 200 OK
    Content-Type: application/json
    Content-Length: 148
    Server: Werkzeug/2.0.2 Python/3.9.6
    Date: Thu, 16 Dec 2021 14:34:11 GMT

   {
       "id": 6,
       "email": "jota_le@mail.com",
       "name": "Jota Lead Update",
       "created_at": "Thu, 16 Dec 2021 10:44:06 GMT",
       "is_user": false
    }

    * se o user role não for admin:
    {
        "error": "Exclusive resource for admin."
    }, 401 (UNAUTHORIZED)


    * Se o lead não existir na base de datos:
    {
        "error": "Lead does not exist"
    }, 404 (NOT_FOUND)
```

# Listar lead específico

### Request

`GET /leads/<int:id>`

#

`Content-Type application/json`

### Header:

```json
    Autorization: Bearer [adm_token]
```

### Body

```json
{}
```

### Responses

```json
    HTTP/1.0 200 OK
    Content-Type: application/json
    Content-Length: 148
    Server: Werkzeug/2.0.2 Python/3.9.6
    Date: Thu, 16 Dec 2021 14:37:49 GMT

    {
        "id": 6,
        "email": "jota_le@mail.com",
        "name": "Jota Lead Update",
        "created_at": "Thu, 16 Dec 2021 10:44:06 GMT",
        "is_user": false
    }

    * se o user role não for admin:
    {
        "error": "Exclusive resource for admin."
    }, 401 (UNAUTHORIZED)

    * Se o lead não existir na base de datos:
    {
        "error": "Lead does not exist"
    }, 404 (NOT_FOUND)
```

# Delete lead

### Request

`DELETE /leads/<int:id>`

#

`Content-Type application/json`

### Header:

```json
{}
```

### Body

```json
{}
```

### Responses

```json
    HTTP/1.0 204 NO CONTENT
    Content-Type: text/html; charset=utf-8
    Server: Werkzeug/2.0.2 Python/3.9.6
    Date: Thu, 16 Dec 2021 14:43:53 GMT

    {}

    * Se o lead não existir na base de datos:
    {
        "error": "Lead does not exist"
    }, 404 (NOT_FOUND)
```
