from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import sys
import os

# Pour pouvoir importer les scripts depuis ml_pipeline/
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'ml_pipeline'))

from ingest_data import ingest_data
from preprocess import preprocess_data
from split_data import split_data
from train_model import train_model
from log_model_mlflow import log_model_to_mlflow

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 1, 1),
    'retries': 1
}

with DAG(
    dag_id='football_analysis_pipeline',
    default_args=default_args,
    description='Pipeline ML pour l’analyse vidéo de football',
    schedule_interval=None,  # Pas d'exécution automatique
    catchup=False
) as dag:

    ingest = PythonOperator(
        task_id='ingest_data',
        python_callable=ingest_data
    )

    preprocess = PythonOperator(
        task_id='preprocess_data',
        python_callable=preprocess_data
    )

    split = PythonOperator(
        task_id='split_data',
        python_callable=split_data
    )

    train = PythonOperator(
        task_id='train_model',
        python_callable=train_model
    )

    log_model = PythonOperator(
        task_id='log_model_mlflow',
        python_callable=log_model_to_mlflow
    )

    # Définir l’ordre des tâches
    ingest >> preprocess >> split >> train >> log_model

