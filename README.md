# Desafio Dog Walking

## Tecnologias

### Frontend
- React
- Jest
- Firebase

### Backend
- Python
- Flask
- GraphQL

## Entidades
(Passeio)
- Status [Esperando, Passeando, Finalizado]
- Data de Agendamento
- Preço
- Duração (30 minutos ou 60 minutos)
- Latitude
- Longitude
- Pets (Lista)
- Horário de Início
- Horário de Término

(Pet)
- Nome
- Raça

## API
- Versionamento
- Retornar JSON

## Rotas da API
- api/v0.1/passeios (GET)
- api/v0.1/passeios?pagina=0 (GET)
- api/v0.1/passeios (POST)
- api/v0.1/passeios (PUT)
- api/v0.1/passeios (DELETE)
- api/v0.1/passeios/hoje (GET)
- api/v0.1/passeios/duracao (GET)
- api/v0.1/passeios/inicio (GET)
- api/v0.1/passeios/fim (GET)

## Especificação do repositório do Dog Walking
- A API para criação de passeio deve receber todos os atributos listados acima menos status;
- A API de show deve retornar a duração real do passeio, ou seja, a diferença entre o início e o término;
- O preço é calculado dinamicamente.
  - Um passeio de 30 minutos para 1 cachorro custa R$25, sendo cada cachorro adicional R$15.
  - Um passeio de 60 minutos para 1 cachorro custa R$35, sendo cada cachorro adicional R$20;

