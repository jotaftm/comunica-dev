## Criar um endereço

### Request

`POST /address`

### Header:
```json
    Autorization: Bearer [token]
```

### Body
`Content-Type: application/json`
```json
    {
        "zip_code": "12345678",
        "address": "Quadra 00 Casa",
        "number": "9",
        "city": "Brasília",
        "state": "Distrito Foderal",
        "country": "Brasil"
    }
```

### Responses

```json
    HTTP/1.0 201 CREATED    
    Content-Type: application/json

	{
	    "id": 4,
	    "zip_code": "12345678",
	    "address": "Quadra 00 Casa",
	    "number": "9",
	    "city": "Brasília",
	    "state": "Distrito Foderal",
	    "country": "Brasil",
	    "user_id": 69
    }
```
Caso algum dado esteja incorreto:
```json
    {
        "message": {
            "country": "Missing required parameter in the JSON body or the post body or the query string"
        }
    }
```
#

## Receber todos os endereços

`DELETE /address/<int:address_id>`

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

    [
	    {
	    	"id": 1,
	    	"zip_code": "12345678",
	    	"address": "Quadra 00 Casa",
	    	"number": "9",
	    	"city": "Brasília",
	    	"state": "Distrito Foderal",
	    	"country": "Brasil",
	    	"user_id": 3
	    }
    ]
```
Caso usuário logado não seja um admnistrador:
```json
    HTTP/1.0 401 UNAUTHORIZED
    Content-Type: application/json

    {
	    "error": "Exclusive resource for admin."
    }
```
#

## Receber endereço do usuário atual

`GET /address/personal`

### Header:
```json
    Autorization: Bearer [user_token]
```

### Body
```json
    {}
```

### Responses

```json
    HTTP/1.0 200 OK
    Content-Type: application/json

    [
	    {
	    	"id": 1,
	    	"zip_code": "12345678",
	    	"address": "Quadra 00 Casa",
	    	"number": "9",
	    	"city": "Brasília",
	    	"state": "Distrito Foderal",
	    	"country": "Brasil",
	    	"user_id": 3
	    }
    ]
```
#

## Receber endereço de um usuário específico

`GET /address/<int:user_id>`

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

    [
	    {
	    	"id": 1,
	    	"zip_code": "12345678",
	    	"address": "Quadra 00 Casa",
	    	"number": "9",
	    	"city": "Brasília",
	    	"state": "Distrito Foderal",
	    	"country": "Brasil",
	    	"user_id": 3
	    }
    ]
```
Caso usuário logado não seja um admnistrador:
```json
    HTTP/1.0 401 UNAUTHORIZED
    Content-Type: application/json

    {
	    "error": "Exclusive resource for admin."
    }
```
Caso o endereço não seja encontrado:
```json
    HTTP/1.0 404 NOT FOUND
    Content-Type: application/json

    {
	    "error": "Address not found!"
    }
```
#
## Deletar um endereço

`GET /address/<int:address_id>`

### Header:
```json
    Autorization: Bearer [user_token]
```

### Body
```json
    {}
```

### Responses

```json
    HTTP/1.0 204 NO CONTENT
    Content-Type: application/json
```
Caso o endereço não seja encontrado:
```json
    HTTP/1.0 404 NOT FOUND
    Content-Type: application/json

    {
	    "error": "Address not found!"
    }
```
#
## Atualizar um endereço

`GET /address/<int:address_id>`

### Header:
```json
    Autorization: Bearer [user_token]
```

### Body
`Content-Type: application/json`
```json
    {
        "zip_code": "12345678",
        "address": "Quadra 00 Casa",
        "number": "9",
        "city": "Brasília",
        "state": "Distrito Foderal",
        "country": "Brasil",
        "user_id": 2
    }
```

### Responses

```json
    HTTP/1.0 200 OK
    Content-Type: application/json

    {
	    "id": 7,
	    "zip_code": "12345678",
	    "address": "Quadra 00 Casa",
	    "number": "9",
	    "city": "Brasília",
	    "state": "Distrito Foderal",
	    "country": "Brasil",
	    "user_id": 2
    }
```
Caso o endereço não seja encontrado:
```json
    HTTP/1.0 404 NOT FOUND
    Content-Type: application/json

    {
	    "error": "Address not found!"
    }
```
#
