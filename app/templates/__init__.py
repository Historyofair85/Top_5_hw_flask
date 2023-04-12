from flask import Flask

app = Flask(__name__)


# import all of the routes file into the current packages
from . import routes