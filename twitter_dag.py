'''

Name: PUT YOUR FULL NAME HERE
Email: PUT YOUR SMU EMAIL ADDRESS HERE

'''

from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
from datetime import timedelta
from datetime import datetime

default_args = {
    # COMPLETE THIS PART
}

dag = DAG(
    # COMPLETE THIS PART
)


# CREATE TASK 1


# CREATE TASK 2


# CREATE EXECUTION SEQUENCE
# e.g. Which task runs first, which task runs next...?