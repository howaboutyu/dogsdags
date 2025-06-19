"""
An example Airflow DAG implementing a simple machine learning pipeline
using the TaskFlow API.
This pipeline loads the Iris dataset, splits it, trains a RandomForest model,
and evaluates its accuracy.
"""
from airflow import DAG
from airflow.decorators import task
from airflow.utils.dates import days_ago

default_args = {
    'owner': 'airflow',
    'start_date': days_ago(1),
}

with DAG(
    dag_id='ml_pipeline_example',
    default_args=default_args,
    description='An example ML pipeline DAG',
    schedule_interval=None,
    catchup=False,
) as dag:

    @task()
    def load_data():
        from sklearn.datasets import load_iris
        data = load_iris(as_frame=False)
        X, y = data.data, data.target
        return {'X': X.tolist(), 'y': y.tolist()}

    @task()
    def split_data(data):
        from sklearn.model_selection import train_test_split
        import numpy as np

        X = np.array(data['X'])
        y = np.array(data['y'])
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )
        return {
            'X_train': X_train.tolist(),
            'X_test': X_test.tolist(),
            'y_train': y_train.tolist(),
            'y_test': y_test.tolist(),
        }

    @task()
    def train_model(split):
        from sklearn.ensemble import RandomForestClassifier
        import pickle, base64
        import numpy as np

        X_train = np.array(split['X_train'])
        y_train = np.array(split['y_train'])
        clf = RandomForestClassifier(n_estimators=10, random_state=42)
        clf.fit(X_train, y_train)
        model_bytes = pickle.dumps(clf)
        model_b64 = base64.b64encode(model_bytes).decode()
        return model_b64

    @task()
    def evaluate_model(split, model_b64):
        import pickle, base64, numpy as np

        X_test = np.array(split['X_test'])
        y_test = np.array(split['y_test'])
        model_bytes = base64.b64decode(model_b64.encode())
        clf = pickle.loads(model_bytes)
        score = clf.score(X_test, y_test)
        print(f"Model test accuracy: {score}")
        return score

    # Task pipeline
    data = load_data()
    split = split_data(data)
    model = train_model(split)
    evaluate_model(split, model)