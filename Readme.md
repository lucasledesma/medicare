[![lucasledesma](https://circleci.com/gh/lucasledesma/medicare.svg?style=svg&circle-token=7b83526a5c4cccab4003d4135fff4b9b97f77486)](https://app.circleci.com/pipelines/github/lucasledesma/medicare)


# Medicare API

Yes! Finally I am learning python... 

## Content

* [First things first](#first-things-first)
* [How to run in local environment](#how-to-run-in-local-environment)
* [How to run using docker-compose](#how-to-run-using-docker-compose)
* [How to run using docker](#how-to-run-using-docker)
* [How to execute test cases](#how-to-execute-test-cases)

## First things first

Let's get the data!

You basically have two options depending on your preferences :)

1. 
2. 

## How to run in local environment

In the root of the project type:

```uvicorn --port 8000 --host 127.0.0.1 main:app --reload```

Then you can access swagger in [http://localhost:8000/docs](http://localhost:8000/docs)


## How to run using docker-compose

The best alternative to run Medicare API using docker is using the docker-compose.yaml file in the root of the project. 

Build:

```docker-compose build```

Run:

```docker-compose up```

Then you can access swagger in [http://localhost:8000/docs](http://localhost:8000/docs)


## How to run using docker

Alternative,  you can use docker directly, but you need to provide the absolute path to the db in the docker run command. 

In the root of the project type the following command to build the docker image:

```docker build . -t medicare```

In the root of the project type the following command to run the API:

```docker run  -v <absolute_path_to_db_directory>:/data  -p 8000:80 medicare```

```<absolute_path_to_db_directory>``` is the directory where you put the sqlite db file

Then you can access swagger in [http://localhost:8000/docs](http://localhost:8000/docs)


## How to execute test cases

In the root of the project run

```pytest```

## Things to keep learning

In this quick python tour I was able to grasp many things... still there are many things I need to keep learning, for example:

* I did my own migration script, because it was easier than yet learning another python framework for migrations... yes I was tired already. 

* I used pydantic for API models/DTOs , it is nice since it provides many built in features for validations... still I didn't dig deeper in custom validatos

* yes, I used Sqlalchemy orm. Although I am not fun or ORMs, I found it to be the fastest way to have something more traditional working

* I used FastAPI .env file for configuration. But I need to dig deeper to handle multiple .env file like in react for example where you can have .env.development, .env.local, etc. and they have a defined precedence

* I used FastAPI, since it already provides a lot of stuff for quickly building an API. However, I was able only to grasp the surface of all its features

* Unit tests... I used pytest, but didn't have time to read much about mocking libraries for example. Or testcontainers, if there is such a thing in python, for bringing up an entire environment if integration test is needed

* I used sqlite because it was faster, but I would have prefer to have a postgresdb up an running in a container with the data. I can start the API and the postgres db from the docker-compose file. Next step?

