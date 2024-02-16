'''

Name: TAN SOON ANN
Email: soonann.tan.2021@scis.smu.edu.sg

'''

from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from twitter.twitter_collector import run_etl
from twitter.twitter_mongo_loader import run_mongo_loader

default_args = {
    # COMPLETE THIS PART
}

dag = DAG(
     dag_id="twitter_mongo_pipeline",
     schedule=None,
     default_args=default_args,
)

# CREATE TASK 1
op_twitter = PythonOperator(
    task_id="twitter_collector_run_etl",
    python_callable=run_etl,
    dag=dag,
)

# CREATE TASK 2
op_mongo = PythonOperator(
    task_id="twitter_collector_run_mongo_loader",
    python_callable=run_mongo_loader,
    dag=dag,
)


# CREATE EXECUTION SEQUENCE
# e.g. Which task runs first, which task runs next...?
op_twitter >> op_mongo

