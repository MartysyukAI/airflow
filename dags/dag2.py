from datetime import datetime, timedelta
from airflow.models import DAG
from airflow.operators.bash import BashOperator


default_args = {
    'owner': 'etl_user',
    'depends_on_past': False,
    'start_date': datetime(2025, 3, 13),
    #'retry_date': timedelta(minutes=0.1)
}

dag = DAG('dag2', default_args=default_args, schedule_interval=None, catchup=True,
          max_active_tasks=3, max_active_runs=1, tags=['Test', 'My first dag'])

# '0 1 * * *'