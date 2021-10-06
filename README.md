# nlp-inference-api
A fully scalable API template for machine learning inference.

## Setup

Set up for the project is handled using docker and docker-compose. Build and run the image using the following command:

```
docker-compose up -d --build
```

## Testing and Code Quality

With the docker container running you can execute the test suite by running the following command:

```
docker-compose exec api python -m pytest
```