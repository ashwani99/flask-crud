# simple-flask-crud

Flask CRUD app that stores employees and their devices

This application has the following endpoints

| URL endpoint | Method type | Description |
|---|---|---|
| `/employees` | `GET` | Get list of all the employees |
| `/employees` | `POST` | Create a new employee |
| `/employee/<:id>` | `GET` | Get details of a particular employee with given `id`|
| `/employee/<:id>`| `PUT` | Update employee details with given `id` |
| `/device` | `POST` | Create a new device |
| `/device/<:id>` | `GET` | Get details of particular device with given `id` |
| `/device/<:id>` | `PUT` | Update device details with given `id` |
| `/device/<:device_id>/assign/<:emp_id>` | `PUT` | Assign device with `device_id` to employee with `emp_id` |
| `/device/<:device_id>/assign/<:emp_id>` | `DELETE` | Un-assign device with `device_id` from employee with `emp_id` |

# License
GNU GPL 3.0