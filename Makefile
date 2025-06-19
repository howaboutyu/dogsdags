.PHONY: init up down restart logs shell status

init:
	@echo "Initializing Airflow..."
	docker compose up airflow-init

up:
	@echo "Starting Airflow..."
	docker compose up -d airflow-webserver airflow-scheduler

down:
	@echo "Stopping Airflow..."
	docker compose down

restart: down up

logs:
	docker compose logs -f airflow-webserver

shell:
	docker compose exec airflow-webserver bash

status:
	docker compose ps