[![lucasledesma](https://circleci.com/gh/lucasledesma/medicare.svg?style=svg&circle-token=7b83526a5c4cccab4003d4135fff4b9b97f77486)](https://app.circleci.com/pipelines/github/lucasledesma/medicare)

# Medicare API

## Content

* [Some thoughts](#some-thoughts)
* [Get the code](#Get-the-code)
* [Set the environment variable ENV](#set-the-environment-variable-env)
* [How to run the code](#how-to-run-the-code)
* [How to execute test cases](#how-to-execute-test-cases)
* [CI](#ci)
* [WTF metric](#wtf-metric)
* [Things to keep learning](#things-to-keep-learning)

## Some thoughts

Yes! Finally I am learning python... 

UPDATE: I've been learning python this week when I had some time, and I can say that I am at that moment when the more you learn the more you realize you know very little. However, I am confident that at some point all pieces will start to fit. 

One thing that makes it easy, is that all the frameworks are architected very similar. No matter the language, the pattern behind them are the same and thus easier to follow. I have experience writing APIs in C# (dotnetcore), Go (Gorilla Mux), Nodejs (express), etc... thus it was easier to follow up with Python and FastApi for example...

## Get the code

First things first, get the code clonning the repo:

```git clone git@github.com:lucasledesma/medicare.git```

Change directory to the repo folder. For example:

```cd medicare```

## Set the environment variable ENV

You need to choose between ```development``` and ```production```.

Development will get you up and running quickly since it works with a small dataset.

If you choose production be patient while we get the data... 

If you selected ```production``` as env, and run the code with docker-compose (see below), the docker-compose log will make it seem as the process is stuck, but is not the case, it is just an issue with the logs. Just wait a couple of minutes...

```export ENV=development```

or

```export ENV=production```

## How to run the code

You have two  options depending on your preferences and your environment:

1. Using docker-compose
2. Using make

### How to run using docker-compose

One alternative to run Medicare API using docker is to use the docker-compose.yaml in the ```app``` folder.

Change directory to ./app

```cd app```

Build:

```docker-compose build```

Run:

```docker-compose up```


Then you can access swagger in [http://localhost:8000/docs](http://localhost:8000/docs)

### How to run using make

Yet, an easier way to run the code, provided you have make and python installed is to use the ```Makefile``` in the root of the project.

```make run``` or just ```make```

Then you can access swagger in [http://localhost:8000/docs](http://localhost:8000/docs)

## How to execute test cases

Note that tests will run out of the box in development environment. However, if you want to run them against the production db, you first need to get the production db, so first run ```make``` or ```make venv check-env getdata importdata```. This will bring the file ```data/production.db```.

In the root of the project you can do ```make test```

Or, go to the test directory of the project

```cd test```

and run

```pytest```

Automated test cases are important not just to test the functionality but also for refactoring. During this exercise having test cases allowed me not just to find bugs in the original implementation, but also to spot issues caused by changes.

## CI

I am very used to do CI/CD with go, react, c#. "Build once, deploy the same wau everywhere".

However, it is the first time I work with an interpreted language, thus no build is needed. Still I need to have something to validate every push, thus I created a quick pipeline at least to run the tests for every commit. That gives me confidence.

See build badge at the top of this page.

## WTF metric

I am sure you are familiarized with the [WTF metric](http://reviewthecode.blogspot.com/2016/01/wtf-per-minute-actual-measurement-for.html#:~:text=WTF%20Per%20Minute%20%2D%20An%20Actual%20Measurement%20for%20Code%20Quality,-Cars%20have%20MPH&text=The%20better%20the%20car%20the,per%20minute%2C%20aka%20code%20quality) for code quality.

I have to say that while taking a look at the code you will have lots of WTF. The explanation is simple, this was a quick exercise to learn a new language, so no much time invested.

Some WTFs you may say:

* Yes, there are lot of code smells... methods too long, extensive use of literals, etc. I didn't have time or was too exhausted to refactor some methods, or to externalize all the variables as configuration.

* Yes, I didn't use Alembic for creating the DB. I still need to learn it... see section below.

* Yes, I could have put the DB in the docker image and make you get the image with the API and the DB altogether... it would have been easier. But I think it is a bad practice to put data in an image, even in this case where the data is not changing. Still, I wanted to have the DB in an external volume mounted to the API container.

And many more...

## Things to keep learning

In this quick python tour I was able to grasp many things... still there are many things I need to keep learning, for example:

* I did my own migration script, because it was easier than learning yet another python framework for migrations... yes I was tired already. 

* I used pydantic for API models/DTOs , it is nice since it provides many built in features for validations... still I didn't dig deeper in custom validators

* yes, I used Sqlalchemy orm. Although I am not fun or ORMs, I found it to be the fastest way to have something more traditional working. I know there is also an async alternative, just didn't have time to learn it yet.

* I used FastAPI .env file for configuration. But I need to dig deeper to handle multiple .env file like in react for example where you can have .env.development, .env.local, etc. and they have a defined precedence

* I used FastAPI, since it already provides a lot of stuff for quickly building an API. However, I was able only to grasp the surface of all its features

* Unit tests... I used pytest, but didn't have time to read much about mocking libraries for example. Or testcontainers, if there is such a thing in python, for bringing up an entire environment if integration test is needed

* I used sqlite because it was faster, but I would have prefer to have a postgresdb up an running in a container with the data. I can start the API and the postgres db from the docker-compose file. Next step?

