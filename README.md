
# Project Folder Structure


## Airflow DAG

A new Airflow DAG named  is added in the  folder.  
It uses the Hugging Face transformers pipeline to classify the image .  
You can trigger this DAG manually or schedule it in your Airflow setup.

# Project Folder Structure
```
repos-root/
  assets/                 # Image assets
  app/                    # Application code with classification script and Dockerfile
    Dockerfile
    image_classification.py
  dags/                   # Airflow DAGs
    hf_image_classification.py
  docker-compose.yml      # Docker compose config
  Makefile                # Utility commands for build/up/down/shell
  README.md
```

## Airflow DAG

A new Airflow DAG named `hf_image_classification` is added in the `dags/` folder.  
It uses the Hugging Face transformers pipeline to classify the image `assets/logo1.png`.  
You can trigger this DAG manually or schedule it in your Airflow setup.
