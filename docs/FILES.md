# Arquivos

A intenção deste arquivo, em específico, é estabelecer as estruturas mínimas de cada um para o Docker. Sendo eles:

1. `docker-compose.yml` / `compose.yml`
2. `Dockerfile`
3. `.dockerignore`

## Docker Compose

É o arquivo **YAML** [^1] de configuração. Setamos configurações de rede, imagens, contêineres, CPU, RAM e afins.

```yaml
services:
  backend:
    build:
      dockerfile: ./

    ports:
      - 3000:3000
    volumes:
      - ./src:./app
```

---

## Dockerfile

É o arquivo que conversa com o Docker. Nele, dizemos as instruções do que fazer com cada arquivo, quais comandos rodar, que porta expôr e outras opções.

```dockerfile
FROM node:24-alpine

WORKDIR /app

COPY src/package*.json ./

RUN npm install

COPY ./src /app

EXPOSE 3000

CMD ["npm", "start"]
```

---

## Docker ignore

É simplesmente um arquivo `.ignore` padrão.

[^1]: O YAML (YAML Ain't Markup Language) Uma linguagem de serialização de dados amigável para humanos, compatível com todas as linguagens de programação. - [The Official YAML Web Site](https://yaml.org/)
