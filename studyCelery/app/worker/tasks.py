import time
from celery import shared_task


@shared_task(queue='celery', rate_limit='9/m')
def add(x, y, msg=''):
    return f"{msg}{x+y}"


@shared_task(queue='celery')
def dumb():
    return


@shared_task(queue='celery')
def xsum(numbers):
    return sum(numbers)


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
