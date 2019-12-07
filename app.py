from flask import Flask

from models import db
from mail import mail, celery
from config import Config
from resources import api
from exceptions import ApiException


# initialising Flask
app = Flask(__name__)
app.config.from_object(Config)
handle_exception = app.handle_exception
handle_user_exception = app.handle_user_exception

# setting up extensions
api.init_app(app)
db.init_app(app)
mail.init_app(app)

with app.app_context():
    db.create_all()


@app.errorhandler(ApiException)
def serialize_exceptions(e):
    return e.to_json()

app.handle_exception = handle_exception
app.handle_user_exception = handle_user_exception

if __name__ == '__main__':
    app.run(debug=True)