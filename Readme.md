# Medicare API

Yes! Finally I am learning python... 

## Content

* [How to run in local environment](#how-to-run-in-local-environment)
* [How to run using docker-compose](#how-to-run-using-docker-compose)
* [How to run using docker](#how-to-run-using-docker)
* [How to execute test cases](#how-to-execute-test-cases)


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

