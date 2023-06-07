from datetime import timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
from datetime import datetime
from twitter_etl import run_etl

default_args = {
    'owner': 'fara',
    'depends_on_past': False,
    'start_date': datetime(2023, 6, 7),
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1)
}

dag = DAG(
    'twitter_dag',
    default_args=default_args,
    description='',
    schedule_interval=timedelta(days=1),
)

run_etl = PythonOperator(
    task_id='Twitteretl',
    python_callable=run_etl,
    dag=dag, 
)

run_etl

 
