# backend/common/tasks.py
import time

from celery import shared_task


@shared_task
def long_running_task():

    time.sleep(10)

    print("Task completed.")

    return "Done"


@shared_task
def cleanup():

    time.sleep(10)

    print("Cleanup completed.")

    return "Done"
