# Usuários
## Criar usuário

### Request
`POST /users/basic`
##
`Content-Type	application/json`


### Header:
```json
    Autorization: Bearer [captcha_token]
```

### Body
```json
{
    "email": "user@mail.com" ,
    "name": "user",
    "cpf" :"00000000001",
    "password": "123456"
}
```

### Responses

```json
    HTTP/1.0 200 OK

    Content-Type	application/json
    Content-Length	234
    Server	        Werkzeug/2.0.2 Python/3.9.6
    Date	        Wed, 15 Dec 2021 01:40:26 GMT

    {
	    "id": 1,
	    "email": "comunicadevapi@mail.com",
	    "name": "Jotaa",
	    "cpf": "00000000000",
	    "created_at": "Wed, 15 Dec 2021 19:16:04 GMT",
	    "premium_at": null,
	    "premium_expire": null,
	    "user_role": "user",
	    "is_premium": false,
	    "verified": false
    }
```
#
## Verificar usuário

### Request
`GET {url_base}/users/validate/<str:token>`
##
`Content-Type	application/json`


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
    HTTP/1.1 200 OK

    Content-Type	application/json
    Content-Length	234
    Server	        Werkzeug/2.0.2 Python/3.9.6
    Date	        Wed, 15 Dec 2021 01:40:26 GMT

    {
	    "id": 1,
	    "email": "comunicadevapi@mail.com",
	    "name": "Jotaa",
	    "cpf": "00000000000",
	    "created_at": "Wed, 15 Dec 2021 19:16:04 GMT",
	    "premium_at": null,
	    "premium_expire": null,
	    "user_role": "user",
	    "is_premium": false,
	    "verified": true
    }
```
#
## Login

### Request
`POST /users/login`
##
`Content-Type	application/json`
### Header:
```json
    {}
```

### Body
Deve ser email e senha do user. 
```json
    Content-Type	application/json

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
    HTTP/1.0 401 UNAUTHORIZED
    Content-Type: application/json
    Content-Length: 35
    Server: Werkzeug/2.0.2 Python/3.9.6
    Date: Wed, 15 Dec 2021 11:42:21 GMT


    {
	    "error": "Invalid password."
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
## Receber dados do usuário logado
### Request

`GET /users/personal`
##
`Content-Type	application/json`


### Header:
```json
    Autorization: Bearer [token]
```

### Body
```json
    {}
```

### Responses

```json
    HTTP/1.0 200 OK

    Content-Type: application/json
    Content-Length: 268
    Server: Werkzeug/2.0.2 Python/3.9.6
    Date: Wed, 15 Dec 2021 23:40:48 GMT

    {
	    "id": 1,
	    "email": "comunicadevapi@mail.com",
	    "name": "Jotaa",
	    "cpf": "00000000000",
	    "created_at": "Wed, 15 Dec 2021 19:16:04 GMT",
	    "premium_at": null,
	    "premium_expire": null,
	    "user_role": "user",
	    "is_premium": false,
	    "verified": false
    }
```
Se o token passado for inválido:
```json
    HTTP/1.0 401 UNAUTHORIZED
    
    Content-Type: text/html; charset=utf-8
    X-XSS-Protection: 0
    Connection: close
    Server: Werkzeug/2.0.2 Python/3.9.6
    Date: Wed, 15 Dec 2021 23:36:09 GMT

    {
	    "error": "Invalid token."
    }
```
#
## Receber dados de um usuário específico
### Request

`GET /users/<int:id>`
##
`Content-Type	application/json`


### Header:
```json
    Autorization: Bearer [token]
```

### Body
```json
    {}
```

### Responses

```json
    HTTP/1.0 200 OK

    Content-Type: application/json
    Content-Length: 268
    Server: Werkzeug/2.0.2 Python/3.9.6
    Date: Wed, 15 Dec 2021 23:40:48 GMT

    {
	    "id": 1,
	    "email": "comunicadevapi@mail.com",
	    "name": "Jotaa",
	    "cpf": "00000000000",
	    "created_at": "Wed, 15 Dec 2021 19:16:04 GMT",
	    "premium_at": null,
	    "premium_expire": null,
	    "user_role": "user",
	    "is_premium": false,
	    "verified": false
    }
```
Se o id fornecido na URL não for o mesmo do usuário em questão:
```json
    HTTP/1.0 500 INTERNAL SERVER ERROR
    
    Content-Type: text/html; charset=utf-8
    X-XSS-Protection: 0
    Connection: close
    Server: Werkzeug/2.0.2 Python/3.9.6
    Date: Wed, 15 Dec 2021 23:36:09 GMT

    {
	    "error": "Unauthorized acces."
    }
```
#
## Alterar dados do usuário

### Request 
`PATCH /users/<int:id>`
##
`Content-Type	application/json`
### Header:
```json
    Autorization: Bearer [token]
```

### Body
ALERTA: Para qualquer mudança é necessário ser passado a **senha atual** do usuário como **current_password** do usuário.
##
Todos os demais dados são opcionais.
```json
    {
        "email": "new_mail@mail.com",
        "name": "new name",
        "cpf": "00000000002",
        "password": "654321",
        "current_password": "123456"
    }
```

### Responses
Se todos os dados estiverem corretos
```json
    HTTP/1.0 202 ACCEPTED
    Content-Type: application/json
    Content-Length: 242
    Server: Werkzeug/2.0.2 Python/3.9.6
    Date: Wed, 15 Dec 2021 11:32:29 GMT

    {
        "id": 23,
        "email": "new_mail@mail.com",
        "name": "new name",
        "cpf": "00000000002",
        "created_at": "Tue, 14 Dec 2021 21:37:36 GMT",
        "premium_at": null,
        "premium_expire": null,
        "is_premium": false,
	    "verified": false
    }
```
Se o email já estiver cadastrado:
```json
    HTTP/1.0 404 NOT FOUND

    Content-Type	application/json
    Content-Length	32
    Server	Werkzeug/2.0.2 Python/3.9.6
    Date	Wed, 15 Dec 2021 01:55:49 GMT

    {
	    "error": "User already exists."
    }
```
Se a senha estiver incorreta:
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
Se o id fornecido na URL não for o mesmo do usuário em questão:
```json
    HTTP/1.0 500 INTERNAL SERVER ERROR
    
    Content-Type: text/html; charset=utf-8
    X-XSS-Protection: 0
    Connection: close
    Server: Werkzeug/2.0.2 Python/3.9.6
    Date: Wed, 15 Dec 2021 23:36:09 GMT

    {
	    "error": "Unauthorized acces."
    }
```
#
## Receber dados de todos usuários
### Request

`GET /users`
##
`Content-Type	application/json`


### Header:
```json
    Autorization: Bearer [token_adm]
```

### Body
```json
    {}
```

### Responses

```json
    HTTP/1.0 200 OK

    Content-Type: application/json
    Content-Length: 268
    Server: Werkzeug/2.0.2 Python/3.9.6
    Date: Wed, 15 Dec 2021 23:40:48 GMT

    [
        {
            "id": 4,
            "email": "luiz_federico@yahoo.com.br",
            "name": "Luiz Federico",
            "cpf": "88888888888",
            "created_at": "Thu, 16 Dec 2021 19:51:33 GMT",
            "premium_at": null,
            "premium_expire": null,
            "user_role": "user",
            "is_premium": false,
            "verified": true
        },
        {
            "id": 1,
            "email": "comunica@mail.com",
            "name": "Comunica Dev",
            "cpf": "00000000000",
            "created_at": "Thu, 16 Dec 2021 19:51:33 GMT",
            "premium_at": null,
            "premium_expire": null,
            "user_role": "admin",
            "is_premium": true,
            "verified": true
        }
    ]
```
Se o token fornecido não pertencer à usuário com permissão admin:
```json
    HTTP/1.0 401 UNAUTHORIZED
    
    Content-Type: text/html; charset=utf-8
    X-XSS-Protection: 0
    Connection: close
    Server: Werkzeug/2.0.2 Python/3.9.6
    Date: Wed, 15 Dec 2021 23:36:09 GMT

    {
	    "error": "Exclusive resource for admin."
    }
```
#
## Deletar usuário
### Request

`DELETE /users/<int:id>`
##
`Content-Type	application/json`


### Header:
```json
    Autorization: Bearer [token]
```

### Body
```json
    {}
```

### Responses

```json
    HTTP/1.0 200 OK

    Content-Type: application/json
    Content-Length: 41
    Server: Werkzeug/2.0.2 Python/3.9.6
    Date: Thu, 16 Dec 2021 00:09:36 GMT

    {
	    "message": "Successfully deleted."
    }
```
Se o id fornecido na URL não for o mesmo do usuário em enviado no token:
```json
    HTTP/1.0 401 UNAUTHORIZED
    
    Content-Type: application/json
    Content-Length: 60
    Server: Werkzeug/2.0.2 Python/3.9.6
    Date: Thu, 16 Dec 2021 00:10:21 GMT

    {
	    "error": "No authorization to access this feature."
    }
```
#
## Enviar email para recuperar senha

### Request
`POST /users/confirm/email`
##
`Content-Type	application/json`


### Header:
```json
    {}
```

### Body
```json
{
	"email" : "jotaftm@gmail.com"
}
```

### Responses

```json
    HTTP/1.0 200 OK

    Content-Type	application/json
    Content-Length	234
    Server	        Werkzeug/2.0.2 Python/3.9.6
    Date	        Wed, 15 Dec 2021 01:40:26 GMT

    {
	    "msg": "Mail sent to user successfully"
    }
```
Se o email fornecido não existir na base de dados:
```json
    HTTP/1.0 404 NOT FOUND
    
    Content-Type: application/json
    Content-Length: 60
    Server: Werkzeug/2.0.2 Python/3.9.6
    Date: Thu, 16 Dec 2021 00:10:21 GMT

    {
	    "error": "Email provided does not exist"
    }
```
#
## Definir nova senha

### Request
`POST /users/reset/password`
##
`Content-Type	application/json`


### Header:
```json
    {}
```

### Body
```json
{
	"email" : "jotaftm@gmail.com",
	"new_password": "123456",
	"reset_code": "d50a2"
}
```

### Responses

```json
    HTTP/1.0 200 OK

    Content-Type	application/json
    Content-Length	234
    Server	        Werkzeug/2.0.2 Python/3.9.6
    Date	        Wed, 15 Dec 2021 01:40:26 GMT

    {
	    "msg": "User password reset successfully"
    }
```
Se passar outros campos na requisição:
```json
    HTTP/1.0 403 FORBIDDEN
    
    Content-Type: application/json
    Content-Length: 60
    Server: Werkzeug/2.0.2 Python/3.9.6
    Date: Thu, 16 Dec 2021 00:10:21 GMT

    {
	    "error": "Wrong request"
    }
```
#