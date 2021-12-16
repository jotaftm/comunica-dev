# Códigos captchas
## Geração de Captcha

### Request
`GET /captchas/generate`
##

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
    HTTP/1.0 201 CREATED
    
    Content-Type: application/json
    Content-Length: 55
    Server: Werkzeug/2.0.2 Python/3.9.6
    Date: Thu, 16 Dec 2021 00:43:50 GMT

    {
        "url_captcha": "https://i.imgur.com/YzItQlG.png"
    }
```
#

### Request
`POST /captchas/validate`
##
`Content-Type	application/json`

### Header:
```json
    {}
```

### Body
```json
    {
        "url_captcha": "https://i.imgur.com/mNOLLkm.png",
        "input_user": "fmG4hBZr"
    }
```

### Responses
```json
    HTTP/1.0 200 OK
    
    Content-Type: application/json
    Content-Length: 350
    Server: Werkzeug/2.0.2 Python/3.9.6
    Date: Thu, 16 Dec 2021 00:51:51 GMT

    {
	    "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTYzOTYxNTkxMSwianRpIjoiYWU2ZTNjODEtY2I1ZC00ZTE4LWFmMGYtYTU0ZTRiYzM0MmYxIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6eyJ1cmxfY2FwdGNoYSI6Imh0dHBzOi8vaS5pbWd1ci5jb20vb3I2dXg4YS5wbmcifSwibmJmIjoxNjM5NjE1OTExLCJleHAiOjE2Mzk2MTY4MTF9.4xUPOU3pU1f5WOJ6NMUfG6njGTu1cDir_XPbeo4T0yk"
    }
```
Se o input do usuário não estiver correto:
```json
    HTTP/1.0 400 BAD REQUEST
    
    Content-Type: application/json
    Content-Length: 33
    Server: Werkzeug/2.0.2 Python/3.9.6
    Date: Thu, 16 Dec 2021 00:47:23 GMT

    {
	    "error": "Not authorized."
    }
```
#
