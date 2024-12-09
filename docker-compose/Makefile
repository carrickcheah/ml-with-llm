start-redpanda:
	docker compose -f redpanda.yml up -d

stop-redpanda:
	docker compose -f redpanda.yml down


add-one-partition-to-trades-topic:
	docker compose -f redpanda.yml exec redpanda rpk topic add-partitions trades --num 1

reset-docker:
	docker container prune
	docker image prune
	docker volume prune
	docker network prune
	docker system prune -a