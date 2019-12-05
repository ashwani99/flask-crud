from flask import Flask
from flask_restful import Api
from flask_mail import Mail

from models import db
from utils import mail
from config import Config
from resources import EmployeeCollection, EmployeeeResource, EmployeeDeviceResource, \
    DeviceAssignmentAction
from exceptions import ApiException


app = Flask(__name__)
app.config.from_object(Config)
api = Api(app)

db.init_app(app)
with app.app_context():
    db.create_all()
mail.init_app(app)

api.add_resource(EmployeeCollection, '/employees')
api.add_resource(EmployeeeResource, '/employee/<int:id>')
api.add_resource(EmployeeDeviceResource, '/device', '/device/<int:id>')
api.add_resource(DeviceAssignmentAction, '/device/<int:device_id>/assign/<int:emp_id>')

@app.errorhandler(ApiException)
def serialize_exceptions(e):
    return e.to_json()


if __name__ == '__main__':
    app.run(debug=True)