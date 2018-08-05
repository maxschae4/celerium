import os
from celery import Celery


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "base.settings")

app = Celery("base")
app.config_from_object("django.conf:settings", namespace="CELERY")
# autodiscover_tasks looks for a tasks.py in the django "INSTALLED_APPS"
app.autodiscover_tasks()

# debug task
@app.task(bind=True)
def debug_task(self):
    print("Request: {0!r}".format(self.request))
