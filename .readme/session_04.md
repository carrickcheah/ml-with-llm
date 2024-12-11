# Session 4

- [ ] Show horizontal scaling in action  
- [ ] Add `candle_seconds` to our messages  
- [ ] Complete to-feature-store service  
     - [ ] Dockerize it  
- [ ] Docker compose file for our technical-indicators pipeline  
- [ ] Building the backfill pipeline.  

...............................................................................................
............................................................................................... 

## Partition in terminal

Setting numbers of partitions

     simple step, 
      - add this command to Makefile  
          add-one-partition-to-trades-topic:  
	     docker compose -f redpanda.yml exec redpanda rpk topic add-partitions trades --num 1  

      - Bash$  
          cd docker-compose  
          Make add-one-partition-to-trades-topic  

      - Check redpanda localhost. Now it should appear.  

...............................................................................................
............................................................................................... 

## to-feature-store services

This microservices do 2 things:  
    1) read data from technical-indicators microservices, and
    2) publish data to hopsworks feature store  

## step by step

In `run.py`, implement QuixStream logic.

    1   create a basic sink to write processed data to a single CSV file. If workthen we move forward.  
        [CSV Sink](https://quix.io/docs/quix-streams/connectors/sinks/csv-sink.html)

    2   Now we create sinks.py, it is a customize file write to connect hopsworks

    3   create hopsworks_credentials.env | dont mixed with settings.env

    4 test run. if of, then dockerize this service.

## structure

to-feature-store/
 │
 ├── run.py/   
 ├── sinks.py/
 ├── config.py/
 ├── settings.py/   
 ├── Makefile/   
 ├── Dockerfile/
 ├── credentials.env/   
 ├── hopsworks_credentials.env/
 
...............................................................................................
...............................................................................................                    		
##  Ingesting historical trade data from Kraken

 - Reason we create backfill pipeline: Need a lot of data to train ML Model.  
 - Use the same mircoservices, adjust code only.

## step by step

 - Visit Kraken API -> click RESTAPI -> Get Recent Trades -> ( checking format)
 
 - create historical.settings.env and live.settings.env  
 - Inside historical.settings.env change topic to " trades_historical". Because we want seperate live n histrorical data.  

 - create a base.py, implement a new class --name TradesAPI. Later will use in websocket.py.

 - 
 


 
 ## structure below.

to-feature-store/
 │
 ├── run.py/   
 ├── historical.settings.env/
 ├── live.settings.env/
 ├── config.py/
 ├── Makefile/   
 ├── Dockerfile/
 ├── kraken_api
        ├── base.py/
        ├── rest.py/
        ├── trade.py/
        ├── websocket.py/





