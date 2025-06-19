.PHONY: init up down restart logs shell status
COMPOSE_URL := https://airflow.apache.org/docs/apache-airflow/3.0.2/docker-compose.yaml

docker-compose.yaml:
	@echo "Downloading docker-compose.yaml from Apache Airflow docs..."
	curl -LfO $(COMPOSE_URL)

init: docker-compose.yaml
	@echo "Initializing Airflow..."
	docker compose up airflow-init

up: docker-compose.yaml
	@echo "Starting Airflow..."
	docker compose up -d airflow-webserver airflow-scheduler

down: docker-compose.yaml
	@echo "Stopping Airflow..."
	docker compose down

restart: down up

logs: docker-compose.yaml
	docker compose logs -f airflow-webserver

shell: docker-compose.yaml
	docker compose exec airflow-webserver bash

status: docker-compose.yaml
	docker compose ps