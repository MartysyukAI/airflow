from datetime import datetime, timedelta
from airflow.models import DAG
from airflow.operators.bash import BashOperator
from airflow.hooks.base_hook import BaseHook

connection = BaseHook.get_connection("main_postgresql_connection")

default_args = {
    'owner': 'etl_user',
    'depends_on_past': False,
    'start_date': datetime(2025, 3, 14),
    #'retry_date': timedelta(minutes=0.1)
}
dag = DAG('dag2', default_args=default_args, schedule_interval='0 * * * *', catchup=True,
          max_active_tasks=3, max_active_runs=1, tags=['Test', 'My first dag'])

task1 = BashOperator(
    task_id='task1',
    bash_command='python3 /airflow/scripts/dag2/task1.py --date {{ ds }} ' + f'--host {connection.host} '
                                                                             f'--dbname {connection.schema} '
                                                                             f'--user {connection.login} '
                                                                             f'--jdbc_password {connection.password} '
                                                                             f'--port 5432',
    dag=dag)

task2 = BashOperator(
    task_id='task2',
    bash_command='python3 /airflow/scripts/dag2/task2.py',
    dag=dag)

task1 >> task2
