from celery import Celery

app = Celery('tasks', broker='redis://localhost:6379/0')

@app.task
def run_upgrade():
    return {'status': 'upgrade_triggered', 'timestamp': str(datetime.now())}
