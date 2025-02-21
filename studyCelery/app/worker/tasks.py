import time
from celery import shared_task
from celery.signals import task_prerun, task_postrun


@shared_task(queue='celery')#, rate_limit='9/m')
def add(x, y, msg=''):
    return f"{msg}{x+y}"


@shared_task(queue='celery')
def dumb():
    return


@shared_task(queue='celery')
def xsum(numbers):
    return sum(numbers)


@task_prerun.connect
def task_prerun_handler(sender, task_id, task, args, kwargs, **kwargs_extra):
    print(f"Sender {sender} | sender_type: {type(sender)}")
    print(f"Task {task} | task_id {task_id} | task_name: {task.name}")


@task_postrun.connect
def task_postrun_handler(sender, task_id, task, args, kwargs, retval, state, **kwargs_extra):
    print(f"Sender: {sender} | Complete task: {task_id} | Return {retval} | Task State: {state}")


def simulating_task_signal():
    add.apply_async([4, 4])


@shared_task(queue='celery')
def t1():
    time.sleep(1)
    return 1


@shared_task(queue='celery:1')
def t2():
    time.sleep(2)
    return 2


@shared_task(queue='celery:2')
def t3():
    time.sleep(3)
    return 3