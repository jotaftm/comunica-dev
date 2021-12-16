# Lessons

## Listar lessons do user logado

### Request

`GET /lessons/personal`

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
    HTTP/1.1 200 OK
    Connection: keep-alive
    Server: gunicorn
    Date: Thu, 16 Dec 2021 22:32:41 GMT

[
  {
    "lesson": {
      "id": 2,
      "title": "Inglês iniciante - Aula 1",
      "description": "Introdução ao verbo To Be",
      "url_video": "http://www.youtube.com/wjd19824kasd12",
      "is_premium": false,
      "category": {
        "id": 2,
        "type": "Inglês basico",
        "description": ""
      }
    },
    "finished": false
  },
  {
    "lesson": {
      "id": 3,
      "title": "Inglês iniciante - Aula 2",
      "description": "Introdução ao verbo To Be",
      "url_video": "http://www.youtube.com/wjd19824kasd12",
      "is_premium": false,
      "category": {
        "id": 2,
        "type": "Inglês basico",
        "description": ""
      }
    },
    "finished": false
  },
  {
    "lesson": {
      "id": 4,
      "title": "Communications",
      "description": "Phrasal verbs",
      "url_video": "http://www.youtube.com/wjd19824kasd12",
      "is_premium": false,
      "category": {
        "id": 3,
        "type": "Inglês iniciante",
        "description": "Fazendo as primeiras perguntas em inglês."
      }
    },
    "finished": false
  }
]

* se user nao estiver logado:
{
    "error": "Unauthorized acces."
}, 401 (UNAUTHORIZED)
```

#

### Atualizar lesson finalizada

`PATCH /lessons/finished/<int:id>`

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
    HTTP/1.1 200 OK
    Connection: keep-alive
    Server: gunicorn
    Date: Thu, 16 Dec 2021 22:41:52 GMT

    {
        "lesson": {
            "id": 2,
            "title": "Inglês iniciante - Aula 1",
            "description": "Introdução ao verbo To Be",
            "url_video": "http://www.youtube.com/wjd19824kasd12",
            "is_premium": false,
            "category": {
                "id": 2,
                "type": "Inglês basico",
                "description": ""
                }
        },
            "finished": true
}

* se user nao estiver logado:
{
    "error": "Unauthorized acces."
}, 401 (UNAUTHORIZED)
```

#

### Listar lessons premium

`GET /lessons/<int:id>`

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
    HTTP/1.1 200 OK
    Connection: keep-alive
    Server: gunicorn
    Date: Thu, 16 Dec 2021 22:41:52 GMT

    {
        "id": 1,
        "title": "Inglês Avançado - Aula 2",
        "description": "Introdução ao verbo To Be",
        "url_video": "http://www.youtube.com/wjd19824kasd12",
        "is_premium": true,
        "category": {
            "id": 1,
            "type": "Inglês Avançado",
            "description": ""
        }
    }

* se o user role não for admin:
    {
        "error": "Exclusive resource for admin."
    }, 401 (UNAUTHORIZED)


    * Se a lesson não existir na base de datos:
    {
        "error": "Lesson does not exist"
    }, 404 (NOT_FOUND)
```

#

### Criar lessons

`POST /lessons`

### Header:

```json
    Autorization: Bearer [adm_token]

```

### Body

```json
{
  "title": "Trabalho em equipe",
  "description": "Como lidar com personalidades fortes",
  "url_video": "http://www.youtube.com/wjd19824kasd12",
  "is_premium": true,
  "category": "Inglês avançado"
}
```

### Responses

```json
    HTTP/1.1 201 CREATED
    Connection: keep-alive
    Server: gunicorn
    Date: Thu, 16 Dec 2021 22:49:41 GMT

{
    "id": 5,
    "title": "Trabalho em equipe",
    "description": "Como lidar com personalidades fortes",
    "url_video": "http://www.youtube.com/wjd19824kasd12",
    "is_premium": true,
    "category": {
        "id": 4,
        "type": "Inglês avançado",
        "description": ""
    }
}

* se o user role não for admin:
    {
        "error": "Exclusive resource for admin."
    }, 401 (UNAUTHORIZED)
```

#

### Listar todas as lessons

`GET /lessons`

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
    HTTP/1.1 200 OK
    Connection: keep-alive
    Server: gunicorn
    Date: Thu, 16 Dec 2021 20:15:30 GMT

    [
  {
    "id": 1,
    "title": "Inglês Avançado - Aula 2",
    "description": "Introdução ao verbo To Be",
    "url_video": "http://www.youtube.com/wjd19824kasd12",
    "is_premium": true,
    "category": {
      "id": 1,
      "type": "Inglês Avançado",
      "description": ""
    }
  },
  {
    "id": 2,
    "title": "Inglês iniciante - Aula 1",
    "description": "Introdução ao verbo To Be",
    "url_video": "http://www.youtube.com/wjd19824kasd12",
    "is_premium": false,
    "category": {
      "id": 2,
      "type": "Inglês basico",
      "description": ""
    }
  },
  {
    "id": 3,
    "title": "Inglês iniciante - Aula 2",
    "description": "Introdução ao verbo To Be",
    "url_video": "http://www.youtube.com/wjd19824kasd12",
    "is_premium": false,
    "category": {
      "id": 2,
      "type": "Inglês basico",
      "description": ""
    }
  },
  {
    "id": 4,
    "title": "Communications",
    "description": "Phrasal verbs",
    "url_video": "http://www.youtube.com/wjd19824kasd12",
    "is_premium": false,
    "category": {
      "id": 3,
      "type": "Inglês iniciante",
      "description": "Fazendo as primeiras perguntas em inglês."
    }
  }
]

* se o user role não for admin:
    {
        "error": "Exclusive resource for admin."
    }, 401 (UNAUTHORIZED)
```

#

### Deletar lesson

`DELETE /lessons/<int:id>`

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
    HTTP/1.1 204 NO CONTENT
    Content-Length: 0
    Connection: keep-alive
    Server: gunicorn
    Date: Thu, 16 Dec 2021 23:00:00 GMT

{}

* se o user role não for admin:
    {
        "error": "Exclusive resource for admin."
    }, 401 (UNAUTHORIZED)


* Se a lesson não existir na base de datos:
    {
        "error": "Lesson does not exist"
    }, 404 (NOT_FOUND)
```

#

### Atualizar lesson

`PATCH /lessons/<int:id>`

### Header:

```json
    Autorization: Bearer [adm_token]

```

### Body

```json
{
  "title": "Habilidades de trabalhar em equipe",
  "description": "Introdução ao verbo ToBe",
  "url_video": "http://www.youtube.com/wjd19824kasd12",
  "is_premium": false,
  "category": "Soft Skills - iniciante"
}
```

### Responses

```json
    HTTP/1.1 200 OK
    Connection: keep-alive
    Server: gunicorn
    Date: Thu, 16 Dec 2021 23:04:35 GMT

{
  "id": 2,
  "title": "Habilidades de trabalhar em equipe",
  "description": "Introdução ao verbo ToBe",
  "url_video": "http://www.youtube.com/wjd19824kasd12",
  "is_premium": false,
  "category": {
    "id": 5,
    "type": "Soft Skills - iniciante",
    "description": ""
  }
}

* se o user role não for admin:
    {
        "error": "Exclusive resource for admin."
    }, 401 (UNAUTHORIZED)


* Se a lesson não existir na base de datos:
    {
        "error": "Lesson does not exist"
    }, 404 (NOT_FOUND)
```
