from __future__ import (
    unicode_literals,
    print_function,
    absolute_import,
    division,
)

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

from .camera import (
    VideoCamera
)

# from .lampu import (
# 	lampu_on,
# 	lampu_off
# )

# from .kirim import (
# 	mail
# )

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:database.db'
db = SQLAlchemy(app)

from my_app.catalog.views import catalog
app.register_blueprint(catalog)
db.create_all()