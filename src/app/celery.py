from celery import Celery

celery_app = Celery("tasks", broker="pyamqp://guest@localhost//")

if __name__ == "__main__":
    celery_app.start()