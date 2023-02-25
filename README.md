This directory is a template project for FastAPI.

# Dev
## Build 
`docker-compose build --no-cache`

## Enter into the container
`docker compose run --rm api bash`

## Start API
`docker compose up --remove-orphans`

## Client side checks
- Helloworld
    - `http://localhost:8080/`
- API doc
    - `http://localhost:8080/docs`

## References
- [FastAPI入門](https://zenn.dev/sh0nk/books/537bb028709ab9)