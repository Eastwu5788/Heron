from flask import blueprints

common = blueprints.Blueprint("common", __name__)

from . import image
from . import location
from . import video
from . import audio
