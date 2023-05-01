from db.run_sql import run_sql
from flask import Blueprint
from flask import request, template_rendered, redirect

locations_blueprint = Blueprint("studio", __name__)