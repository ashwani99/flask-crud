from marshmallow import Schema, fields, post_load, ValidationError

from .models import Employee, Device
from .utils import is_mobile_number_valid


def validate_mobile_number(number):
    """ Validate a mobile number string """
    if not is_mobile_number_valid(number):
        raise ValidationError("Please provide a valid mobile number")


class BaseSchema(Schema):
    class Meta:
        strict = True


class DeviceSchema(BaseSchema):
    id = fields.Integer(dump_only=True)
    device_name = fields.String(required=True)

    @post_load
    def make_device_object(self, data, **kwargs):
        return Device(**data)


class EmployeeSchema(BaseSchema):
    id = fields.Integer(dump_only=True)
    firstname = fields.String(required=True)
    lastname = fields.String(required=True)
    email = fields.Email(required=True)
    mobile_number = fields.String(required=True,
                                  validate=validate_mobile_number)
    devices = fields.Nested(DeviceSchema, many=True, dump_only=True)

    @post_load
    def make_employee_object(self, data, **kwargs):
        return Employee(**data)


device_schema = DeviceSchema()
devices_schema = DeviceSchema(many=True)
employee_schema = EmployeeSchema()
employees_schema = EmployeeSchema(many=True)
