from flask_mail import Mail, Message
import re

mail = Mail()

def is_mobile_number_valid(number):
    """ Utility function to validate a mobile number """
    mobile_number_re = re.compile(r"^[6-9]\d{9}$")
    return mobile_number_re.match(number) is not None


def send_async_email(mail_body):
    """ Sends a e-mail asynchronously """
    msg = Message(subject="Important email from CRUD app",
                  recipients=["user@example.com"],
                  body=mail_body,
                  sender="admin-crud@example.com")
    mail.send(msg)