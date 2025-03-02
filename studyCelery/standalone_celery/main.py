from celery import Celery

# app = Celery('worker',
#              broker='redis://redis:6379/0',
#              backend='redis://redis:6379/0',
#              include=['worker.tasks'])
# OR
app = Celery('worker',
             include=['worker.tasks'])

app.config_from_object('celeryconfig')

app.conf.task_route = {
    'worker.tasks.add': {
        'queue': 'celery3',
    },
    'worker.tasks.mul': {
        'queue': 'celery4',
    },
    'worker.tasks.xsum': {
        'queue': 'celery5',
    }
}

if __name__ == '__main__':
    app.start()
