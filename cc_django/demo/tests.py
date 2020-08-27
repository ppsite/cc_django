import logging
from celery import shared_task

# Create your tests here.

logger = logging.getLogger('root')


@shared_task(ignore_result=True)
def demo_task(x, y):
    print(x + y)
