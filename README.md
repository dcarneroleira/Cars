# CARS API
Your python version must be 3.8.10 or higher
## How starts the API
Create and activate a virtual environment:

(Linux)

If you need, install:
```
sudo apt-get install python3-venv
```
Create and activate in Linux:
```
python3 -m venv .venv
```
```
source .venv/bin/activate
```
(Windows)
```
python -m venv .venv
```
```
.venv\scripts\activate
```
Install requirements:
```
pip install -r requirements.txt
```

Migrate the database:
```
cd cars
```
```
python manage.py migrate items
```

Run the API:
```
python manage.py runsever
```

## Testing the API
After you have the server running, you can open Postman(if you have it intalled) and try the collection **Cars API(Test)**

If you want to try POST, PUT or DELETE; you must create a superuser before.

Run this command and remember your username and password:
```
python manage.py createsuperuser
```
Once you create your superuser you can create, update and delete instances.
