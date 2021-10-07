# nlp-inference-api
A fully scalable API template for machine learning inference.

## Setup

Set up for the project is handled using docker and docker-compose. Build and run the image using the following command:

```
docker-compose up -d --build
```

You can stop the containers at any time by running:

```
docker-compose down -v
```

## Testing

With the docker container running you can execute the test suite by running the following command:

```
docker-compose exec api python -m pytest
```

## Code Quality and Linting

Code quality and linting is handled using isort, black and flake8 packages.

First run black to automate a portion of the formating:

```
docker-compose exec api black .
```

Then sort imports with isort:

```
docker-compose exec api isort .
```

Finally run flake8 and make any necessary changes:

```
docker-compose exec api flake8 .
```

## Deployment

This repo is set up to be deployed to AWS using serverless. First export your desired environment variables.

You will need to have brew, node and serverless set up for a mac.

```
export API_USERNAME='newApiDocsUsername'
export API_PASSWORD='newApiDocsPassword'
export STAGE='prod'
serverless deploy
```