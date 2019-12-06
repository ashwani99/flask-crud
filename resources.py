from flask import request, jsonify, make_response
from flask_restful import Api, Resource
from sqlalchemy.exc import IntegrityError
from marshmallow import ValidationError

from models import Employee, Device, db
from serializers import employee_schema, employees_schema, device_schema, \
    devices_schema
from exceptions import ApiException
from mail import send_async_email


class EmployeeCollection(Resource):
    def get(self):
        """ Get all the employees """
        emps = Employee.query.all()
        return make_response(jsonify(employees_schema.dump(emps)), 200)
        
    def post(self):
        """ Create a new employee """
        try:
            emp = employee_schema.load(request.json)
        except ValidationError as e:
            raise ApiException(e.messages, 400)

        try:
            db.session.add(emp)
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            raise ApiException(dict(email="This email is already registered"), 409)
        
        return make_response(jsonify(employee_schema.dump(emp)), 201)


class EmployeeeResource(Resource):
    def get(self, id):
        """ Get all the employees """
        emp = Employee.query.get(id)
        if emp is None:
            raise ApiException(dict(message=[f"Not able to find any employee with id {id}"]),
                               404)

        return make_response(jsonify(employee_schema.dump(emp)), 200)
    
    def put(self, id):
        """ Update a employee's details """
        try:
            emp_new = employee_schema.load(request.json)
        except ValidationError as e:
            raise ApiException(e.messages, 400)
        
        emp = Employee.query.get(id)
        if emp is None:
            raise ApiException(dict(message=[f"Not able to find any employee with id {id}"]),
                               404)
        
        try:
            emp.__init__(**emp_new.__dict__)
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            raise ApiException(dict(email="This email is already registered"), 400)

        return make_response('', 204)


class EmployeeDeviceResource(Resource):
    def get(self, id):
        """ Get a device details """
        device = Device.query.get(id)
        if device is None:
            raise ApiException(dict(message=[f"Not able to find any device with id {id}"]),
                               404)
        return make_response(jsonify(device_schema.dump(device)), 200)

    def post(self):
        """ Create a new device """
        try:
            device = device_schema.load(request.json)
        except ValidationError as e:
            raise ApiException(e.messages, 400)

        db.session.add(device)
        db.session.commit()

        return make_response(jsonify(device_schema.dump(device)), 201)

    def put(self, id):
        """ Update device details """
        device = Device.query.get(id)
        if device is None:
            raise ApiException(dict(message=[f"Not able to find any device with id {id}"]),
                               404)

        try:
            device = device_schema.load(request.json)
        except ValidationError as e:
            raise ApiException(e.messages, 400)
        
        device.__init__(**device.__dict__)
        db.session.commit()
        return make_response('', 204)


class DeviceAssignmentAction(Resource):
    def put(self, device_id, emp_id):
        """ Assign device to an employee """
        device = Device.query.get(device_id)
        if device is None:
            raise ApiException(dict(message=[f"Not able to find any device with id {id}"]),
                               404)
        emp = Employee.query.get(emp_id)
        if device is None:
            raise ApiException(dict(message=[f"Not able to find any employee with id {id}"]),
                               404)
        
        try:
            is_notify = emp.assign_device(device)
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            raise ApiException()

        if is_notify:
            send_async_email.delay('email sent random text')

        return make_response(jsonify(success=True, status="assigned"), 204)


    def delete(self, device_id, emp_id):
        """ Un-assign device from an employee """
        device = Device.query.get(device_id)
        if device is None:
            raise ApiException(dict(message=[f"Not able to find any device with id {id}"]),
                               404)
        emp = Employee.query.get(emp_id)
        if device is None:
            raise ApiException(dict(message=[f"Not able to find any employee with id {id}"]),
                               404)
        
        try:
            is_notify = emp.unassign_device(device)
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            raise ApiException()

        if is_notify:
            send_async_email.delay('email sent random text')
        
        return make_response(jsonify(success=True, status="un-assigned"), 204)


api = Api()
api.add_resource(EmployeeCollection, '/employees')
api.add_resource(EmployeeeResource, '/employee/<int:id>')
api.add_resource(EmployeeDeviceResource, '/device', '/device/<int:id>')
api.add_resource(DeviceAssignmentAction, '/device/<int:device_id>/assign/<int:emp_id>')
