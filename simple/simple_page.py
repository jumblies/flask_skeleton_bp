from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
from simple.helper import test

simple_page = Blueprint('simple_page', __name__, static_folder='static',
                        template_folder='templates')

@simple_page.route('/')
def show():
    try:
        result = test()
        return render_template('simple_index.html', result=result)
    except TemplateNotFound:
        abort(404)
