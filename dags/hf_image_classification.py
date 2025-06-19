from airflow import DAG
from airflow.decorators import task
from airflow.utils.dates import days_ago
from transformers import pipeline
from PIL import Image
import os

default_args = {
    'owner': 'howaboutyu',
    'start_date': days_ago(1),
}

with DAG(
    dag_id='hf_image_classification',
    default_args=default_args,
    description='Hugging Face image classification DAG',
    schedule_interval='@daily',
    catchup=False,
) as dag:

    @task()
    def load_classifier():
        return pipeline("image-classification")

    @task()
    def classify_image(classifier):
        image_path = os.path.join(os.getcwd(), 'assets', 'logo1.png')
        image = Image.open(image_path)
        results = classifier(image)
        # For demo, print results
        print("Image classification results:")
        for res in results:
            print(f"- {res['label']} (score: {res['score']})")
        return results

    classifier = load_classifier()
    classify_image(classifier)
