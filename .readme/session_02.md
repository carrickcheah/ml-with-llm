# Session 2

Today tasks:  

- dockerize trade producer  
      - write docker file  
      - build docker image  
      - Run a docker container

- add precommit hooks for automatic linting and formatting  

- build candle service ( transform mirco service )  
      - write docker file  

## Task 1 Dockerize trades, the first microservice

- google search " uv dockerfile example"  
- [UV Dockerfile Example](https://docs.astral.sh/uv/guides/integration/docker)  
- cd/trades  
- create Dockerfile  
- update Makefile  

- to check whether Docker is working, we can run this 2 code:  
      - run-dev:        ( run locally, if work mean code no problem)  
      - run: build      ( if run successfully, job done; if not then dockerfile problem )  

## Task 2 Optimising the Dockerfile - Multistage builds

- [Optimize Dockerfile Example](https://github.com/astral-sh/uv-docker-example/tree/main)
optmize the Dockerfile. naive.Dockerfile is too heavy. Purpose is build smaller image.  

## Linting and formatting with ruff

Create a pyproject.toml file in main. Just use it as template format for ruff format.  
Use ruff check to check.


##  Pre-commit to automate linting and formatting

[installation website](pre-commit.com)  
       - Bash$ uv tool install pre-commit  
       - Check version | Bash$ pre-commit --version  
       - Create a file in root | .pre-commit-config.yaml 
       - Bash$ pre-commit install | go the pre-commit webstie follow instruction.  


## Build second microservice: candles

This microservice reads data from the 'trades' Kafka topic, and stores it in the 'candles' Kafka topic.  
Utilizing the Redpanda streaming platform necessitates specifying the Kafka broker address and a consumer group.  
The module processes data over 60-second windows.  

       - KAFKA_BROKER_ADDRESS=
       - KAFKA_INPUT_TOPIC=
       - KAFKA_OUTPUT_TOPIC=
       - KAFKA_CONSUMER_GROUP=
       - CANDLE_SECONDS=

## Init new project

bash$   uv init candles

## Create config, settings.env, and Makefile

Setup the credentials  

## Custom window aggregations with Quix Streams ( turn raw data into ohlc)

- sdf.reduce(reducer=update_candle, initializer=init_candle)
- create 2 function to convert raw data into ohlc
       - def init_candle and  def update_candle












## Reflection on the lessons learnt  

Different style dockerinzetion will decide the image file size. No need memorize, go the official github page to get example. The website address above.

Ruff is very good tool for format and debug.  


