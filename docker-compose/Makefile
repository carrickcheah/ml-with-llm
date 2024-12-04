start-redpanda:
	docker compose -f redpanda.yml up -d

stop-redpanda:
	docker compose -f redpanda.yml down


reset-docker:
	docker container prune
	docker image prune
	docker volume prune
	docker network prune
	docker system prune -a