# Categorias
## Create category

`POST /categories`

### Header:

```json
    Autorization: Bearer [adm_token]
```

### Body

```json
{
  "type": "English lessons",
  "description": "Educational program targeted at developers whose objective is to learn English as a second language in order to land an international job"
}
```

### Responses

```json
    HTTP/1.0 201 CREATED
    Content-Type: application/json
    Content-Length: 203
    Server: Werkzeug/2.0.2 Python/3.9.6
    Date: Thu, 16 Dec 2021 16:30:46 GMT

    {
        "id": 4,
        "type": "English lessons",
        "description": "Educational program targeted at developers whose objective is to learn English as a second language in order to land an international job"
    }

    * se o user role não for admin:
    {
        "error": "Exclusive resource for admin."
    }, 401 (UNAUTHORIZED)
```

#

## Listar todas as categorias

`GET /categories`

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
    Content-Length: 402
    Server: Werkzeug/2.0.2 Python/3.9.6
    Date: Thu, 16 Dec 2021 16:38:30 GMT

    [
        {
            "id": 1,
            "type": "English lessons",
            "description": "Educational program targeted at developers whose objective is to learn English as a second language in order to land an international job"
        },
        {
            "id": 2,
            "type": "Soft Skills lessons",
            "description": "A special program designed to develop and boost the most required skills in the global tech environment"
        }
    ]

    * se o user role não for admin:
    {
        "error": "Exclusive resource for admin."
    }, 401 (UNAUTHORIZED)
```

#

## Listar uma categoria específica

`GET /categories/<int:id>`

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
    Content-Length: 203
    Server: Werkzeug/2.0.2 Python/3.9.6
    Date: Thu, 16 Dec 2021 16:42:17 GMT

    {
        "id": 1,
        "type": "English lessons",
        "description": "Educational program targeted at developers whose objective is to learn English as a second language in order to land an international job"
    }


    * se o user role não for admin:
    {
        "error": "Exclusive resource for admin."
    }, 401 (UNAUTHORIZED)

    * Se a category não existir na base de datos:
    {
        "error": "Category does not exist"
    }, 404 (NOT_FOUND)
```

#

## Deletar uma categoria específica

`DELETE /categories<int:id>`

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
    HTTP/1.0 204 NO CONTENT
    Content-Type: text/html; charset=utf-8
    Server: Werkzeug/2.0.2 Python/3.9.6
    Date: Thu, 16 Dec 2021 16:36:52 GMT

    {}

    * se o user role não for admin:
    {
        "error": "Exclusive resource for admin."
    }, 401 (UNAUTHORIZED)

    * Se a category não existir na base de datos:
    {
        "error": "Category does not exist"
    }, 404 (NOT_FOUND)
```

#

## Atualizar categoria específica

`PATCH /categories<int:id>`

### Header:

```json
    Autorization: Bearer [adm_token]
```

### Body

```json
* usuário pode atualizar todos os campos de uma só vez, ou somente um dos campos:

{
  "type": "Inglês Básico",
  "description": "Primeiros passos com a língua inglesa, e verbo to-be."
}
```

### Responses

```json
    HTTP/1.0 200 OK
    Content-Type: application/json
    Content-Length: 124
    Server: Werkzeug/2.0.2 Python/3.9.6
    Date: Thu, 16 Dec 2021 16:47:31 GMT

    {
        "id": 1,
        "type": "Inglês Básico",
        "description": "Primeiros passos com a língua inglesa, e verbo to-be."
    }

    * se o user role não for admin:
    {
        "error": "Exclusive resource for admin."
    }, 401 (UNAUTHORIZED)

    * Se a category não existir na base de datos:
    {
        "error": "Category does not exist"
    }, 404 (NOT_FOUND)
```

#
