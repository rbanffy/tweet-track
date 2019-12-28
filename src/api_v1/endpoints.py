"""
# API endpoints

The API endpoints, /person, {service}/id/{id}, and
{service}/screen_name/{screen_name}
"""

from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
import http

endpoints = Blueprint(
    'person', __name__,
    template_folder='templates')

@endpoints.route('/person/<person_id>')
def person(person_id: int):
    return 'A person'
    # abort(http.HTTPStatus.NOT_FOUND)
