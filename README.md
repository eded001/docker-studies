# Docker Studies

Laboratório de estudos e experimentos com **Docker e Docker Compose**, organizado em pequenos projetos para praticar containerização, comunicação entre serviços e persistência.

## Projetos

### `basic-backend`

Backend básico em Node.js/Express usado como ponto de partida para estudar criação de imagens e execução de containers.

### `basic-frontend`

Frontend isolado para praticar containerização de aplicações cliente.

### `backend-db`

Projeto com backend Python/FastAPI integrado a PostgreSQL e Redis, voltado a cenários com múltiplos serviços.

## Tecnologias exploradas

- Docker
- Docker Compose
- Node.js
- Express
- Python
- FastAPI
- PostgreSQL
- Redis

## Estrutura

```text
.
├── basic-backend/
├── basic-frontend/
├── backend-db/
└── docs/
```

## Objetivo

O repositório funciona como ambiente de prática para conceitos como:

- criação de `Dockerfile`;
- build de imagens;
- execução e remoção de containers;
- mapeamento de portas;
- volumes;
- variáveis de ambiente;
- redes entre containers;
- Docker Compose;
- aplicações multi-serviço.

Cada diretório representa uma etapa independente da evolução dos estudos.
