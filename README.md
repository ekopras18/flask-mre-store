## Flask
Flask is a lightweight WSGI web application framework. It is designed to make getting started quick and easy, with the ability to scale up to complex applications. It began as a simple wrapper around Werkzeug and Jinja and has become one of the most popular Python web application frameworks.

Flask offers suggestions, but doesn't enforce any dependencies or project layout. It is up to the developer to choose the tools and libraries they want to use. There are many extensions provided by the community that make adding new functionality easy.

```bash
# save this as app.py
from flask import Flask, request
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'

```

```bash
$ flask run
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

## Setup App

0. setup your env
- install python3
- intsall pip
- setup env : pip venv project_env
<!-- pip freeze > requirements.txt -->
1. pip install -r requirements.txt

2. dont forget to setup connection

models.py

```bash
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'secret'
app.config['MYSQL_DB'] = 'db_name'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
```

3. import db 'database-v3-final.sql'

4. run app (go to directory app)

```bash

$ python3 app.py

```

## if error

```bash

from flask_uploads import UploadSet, configure_uploads, IMAGES
  File "/opt/homebrew/lib/python3.11/site-packages/flask_uploads.py", line 26, in <module>
from werkzeug import secure_filename, FileStorage
ImportError: cannot import name 'secure_filename' from 'werkzeug' (/opt/homebrew/lib/python3.11/site-packages/werkzeug/__init__.py)"

```
In flask_uploads.py

change 

```bash
from werkzeug import secure_filename, FileStorage
```
to 

```bash
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage
```

## User Demo

login administrator

user : admin@mrestore.com
pass : mrestore


login user

user : ekopras@gmail.com
pass : ekopras


