.PHONY: init up down restart logs shell status clean-examples
COMPOSE_URL := https://airflow.apache.org/docs/apache-airflow/3.0.2/docker-compose.yaml
ENV_FILE    := .env


docker-compose.yaml:
	@echo "Downloading docker-compose.yaml from Apache Airflow docs..."
	# To get a fresh docker compose file, uncomment below
	# curl -LfO $(COMPOSE_URL)

.env:
	@echo "Generating $(ENV_FILE) with local user and group IDs..."
	@echo "AIRFLOW_UID=$$(id -u)" > $(ENV_FILE)
	@echo "AIRFLOW_GID=$$(id -g)" >> $(ENV_FILE)

init: docker-compose.yaml $(ENV_FILE)
	@echo "Initializing Airflow..."
	docker compose up airflow-init

up: docker-compose.yaml $(ENV_FILE)
	@echo "Starting Airflow..."
	docker compose up -d # airflow-webserver airflow-scheduler

down: docker-compose.yaml $(ENV_FILE)
	@echo "Stopping Airflow..."
	docker compose down

restart: down up

logs: docker-compose.yaml $(ENV_FILE)
	docker compose logs -f airflow-webserver

shell: docker-compose.yaml $(ENV_FILE)
	docker compose exec airflow-webserver bash

status: docker-compose.yaml $(ENV_FILE)
	docker compose ps

clean-examples: docker-compose.yaml $(ENV_FILE)
	@echo "Deleting example and tutorial DAGs from Airflow metadata..."
	@for dag in `docker compose run --rm airflow-cli dags list | awk '/^(example_|tutorial_)/ {print $$1}'`; do \
		echo "Deleting $$dag"; \
		docker compose run --rm airflow-cli dags delete $$dag --yes; \
	 done
	@echo "Removing example logs from host..."
	@rm -rf logs/dag_processor/*/example_dags
