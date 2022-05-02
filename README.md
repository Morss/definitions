Python with Flask and Jinja templated html frontend example.

Install requirements
```
$ python -m pip install -r requirements.txt
```

To run in DEV mode (using a bash shell, e.g. git bash):
```
$ FLASK_APP=main.py FLASK_ENV=development python -m flask run --port 5000
```

To run in PROD mode (port 8080):
```
$ python main.py
```

Docker
```
$ docker build -t pythonflask/example .
$ docker run -p 8080:8080 pythonflask/example 
```