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

