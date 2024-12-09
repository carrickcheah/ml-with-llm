# Session 4

- [ ] Show horizontal scaling in action  
- [ ] Add `candle_seconds` to our messages  
- [ ] Complete to-feature-store service  
     - [ ] Dockerize it  
- [ ] Docker compose file for our technical-indicators pipeline  
- [ ] Building the backfill pipeline.  

## Add `candle_seconds` param to our pipeline

     simple step, 
      - add this command to Makefile  
          add-one-partition-to-trades-topic:  
	     docker compose -f redpanda.yml exec redpanda rpk topic add-partitions trades --num 1  

      - Bash$  
          cd docker-compose  
          Make add-one-partition-to-trades-topic  

      - Check redpanda localhost. Now it should appear.  






