'''

Name: TAN SOON ANN
Email: soonann.tan.2021@scis.smu.edu.sg

'''

from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from twitter.twitter_collector import run_etl

default_args = {
    # COMPLETE THIS PART
}

dag = DAG(
     dag_id="twitter_collector",
     schedule=None,
)

# def print_context(ds=None, **kwargs):
    # """Print the Airflow context and ds variable from the context."""
    # print(kwargs)
    # print(ds)
    # return "Whatever you return gets printed in the logs"

PythonOperator(task_id="twitter_collector_run_etl", python_callable=run_etl)


# CREATE TASK 1


# CREATE TASK 2


# CREATE EXECUTION SEQUENCE
# e.g. Which task runs first, which task runs next...?
