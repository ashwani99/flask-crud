from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship


db = SQLAlchemy()


class Employee(db.Model):
    id = Column(Integer, primary_key=True)
    firstname = Column(String(255), nullable=False)
    lastname = Column(String(255), nullable=False)
    email = Column(String(254), unique=True, nullable=False)
    mobile_number = Column(String(15), nullable=False)

    devices = relationship("Device", backref="device_assignee")
    
    def __init__(self, firstname, lastname, email, mobile_number, **kwargs):
        """ Initiate a `Employee` object """
        db.Model.__init__(self, firstname=firstname, lastname = lastname,
                                email=email, mobile_number=mobile_number)

    def __repr__(self):
        """ Represent `Employee` instance as a unique string """
        return "<Employee({email!r})>".format(email=self.email)

    def assign_device(self, device):
        """ Assign a device to an `Employee` """
        if device not in self.devices:
            self.devices.append(device)
            return True
        return False

    def unassign_device(self, device):
        """ Un-assign a device to an `Employee` """
        if device in self.devices:
            self.devices.remove(device)
            return True
        return False


class Device(db.Model):
    id = Column(Integer, primary_key=True)
    emp_id = Column(Integer, ForeignKey("employee.id"))
    device_name = Column(String(255), nullable=False)

    def __init__(self, device_name, **kwargs):
        """ Initiate a `Device` object """
        db.Model.__init__(self, device_name=device_name)

    def __repr__(self):
        """ Represent `device` instance as a unique string """
        return "<Device({id!r})>".format(id=self.id)

    @property
    def is_assigned(self):
        """ Checks if the device is assigned or not """
        return self.device_assignee is not None

