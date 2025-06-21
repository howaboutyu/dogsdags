# ML Airflow DAGs

This repository contains example Apache Airflow DAGs for machine learning pipelines using the TaskFlow API.

## Structure

- `dags/`
  - `ml_pipeline_example.py`: A template DAG that loads the Iris dataset, trains a RandomForest model, and evaluates it.

## Docker Compose + Makefile Setup

Prerequisites:

- Docker & Docker Compose plugin
- make
- curl

This repository uses a Makefile to manage Apache Airflow via Docker Compose. The Makefile will:

- Download the official `docker-compose.yaml` for Airflow (v3.0.2)
- Generate an `.env` file setting `AIRFLOW_UID` and `AIRFLOW_GID` to your host user/group IDs

Usage:

```bash
make init      # download files & initialize Airflow DB
make up        # download files & start Airflow webserver and scheduler
make down      # stop Airflow containers
make restart   # restart Airflow
make logs      # tail Airflow webserver logs
make shell     # open a bash shell in the webserver container
make status    # show running containers
```

The Makefile automatically ensures the `docker-compose.yaml` and `.env` files are present.