# Leads

URL para utilização da API: https://leads-back-deploy.herokuapp.com

# Rotas:

## Obtenção dos Leads. 
`GET /leads` 

## Cadastro de um novo Lead

`POST /leads FORMATO DA ENTRADA:`
```json

{
  "name": "John Doe",
  "email": "john@email.com",
  "phone": "(41)90000-0000"
}

```
`FORMATO DE SAÍDA`
```json

{
    "name": "John Doe",
    "email": "john@email.com",
    "phone": "(41)90000-0000",
    "creation_date": "Fri, 10 Sep 2021 17:53:25 GMT",
    "last_visit": "Fri, 10 Sep 2021 17:53:25 GMT",
    "visits": 1
}

```

## Edição de um Lead (quantidade de visits alterada)

`PATCH /leads FORMATO DA ENTRADA:`
```json

{
  "email": "john@email.com",
}

```

## Deleção de um Lead

`DELETE /leads FORMATO DA ENTRADA:`
```json

{
  "email": "john@email.com",
}

```

