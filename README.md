# Airflow Summit 2025 is coming October 07-09. **Register now for early bird ticket!**

[Community](https://airflow.apache.org/community/) | [Meetups](https://airflow.apache.org/community#meetups) | [Documentation](https://airflow.apache.org/docs/) | [Use Cases](https://airflow.apache.org/use-cases/) | [Announcements](https://airflow.apache.org/announcements/) | [Blog](https://airflow.apache.org/blog/) | [Ecosystem](https://airflow.apache.org/ecosystem/) | Version: 3.0.2 | [Search docs](https://airflow.apache.org/docs/)

# ML Airflow DAGs

This repository contains example Apache Airflow DAGs for machine learning pipelines using the TaskFlow API.

## Structure

- `dags/`
  - `ml_pipeline_example.py`: A template DAG that loads the Iris dataset, trains a RandomForest model, and evaluates it.

## Setup

1. (Optional) Create and activate a virtual environment:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Initialize Airflow (if not already done):
   ```bash
   export AIRFLOW_HOME=$(pwd)/airflow_home
   airflow db init
   ```
4. Ensure `dags/` is in your Airflow DAGs folder (default is `$AIRFLOW_HOME/dags`).
5. Start the Airflow scheduler and webserver:
   ```bash
   airflow scheduler
   airflow webserver
   ```
6. Open the Airflow UI at `http://localhost:8080` and you should see the `ml_pipeline_example` DAG.