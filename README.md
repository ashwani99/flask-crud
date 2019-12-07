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

There is a [postmand collection](/postman/Flask\ CRUD\ APP.postman_collection.json) available with all requests. You can import the collection in your [Postman](https://www.getpostman.com/) application using the JSON file.

## Local environment setup

### Technology components
- Database - SQLite
- Web framework - Flask
- Task queue - Redis

### Dependencies
- Python 3.6
- SQLite
- Redis

### Steps
Make sure you have the dependencies mentioned above installed before proceeding. Then, follow the below mentioned steps.

- Clone the repository and move into `flask-crud` directory

```sh
git clone https://github.com/ashwani99/flask-crud
cd flask-crud
```

- Spin up a virtual environment (preferably) and install the python dependencies

```sh
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

- Setup environment variables for flask CLI and database URL (SQLite is used here)
```
export FLASK_APP=app:app
export FLASK_DEBUG=0 # set it to 1 if you want to run flask in debug mode
export DATABASE_URL='sqlite:///app.db'
```

- Start `redis` (if not running already) and start `celery`
```sh
sudo service redis start
celery worker -A app.celery
```

- Serve the application on flask local development server
```
flask run --port=5000
```

That's it! The API will be serving on `http://127.0.0.1:5000`

## License
GNU GPL 3.0