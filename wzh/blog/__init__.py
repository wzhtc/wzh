from flask import Blueprint
from flask_mongoengine import MongoEngine

blog = Blueprint(
    'blog',
    __name__,
    template_folder='templates',
    static_folder='static'
)

from . import views