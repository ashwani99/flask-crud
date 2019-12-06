from flask import current_app
from flask_mail import Mail, Message
from celery import Celery

from config import Config

mail = Mail()
celery = Celery(__name__, broker=Config.CELERY_BROKER_URL)
# celery.conf.update()

@celery.task(bind=True)
def send_async_email(self, mail_body):
    """ Sends a e-mail notification """
    msg = Message(subject="Important email from CRUD app",
                  recipients=["user@example.com"],
                  body=mail_body,
                  sender="admin-crud@example.com")
    from app import app
    with app.app_context():
        mail.send(msg)