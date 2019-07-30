from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound


# important.  Do not have another index with the same name.  It causes errors.
second_page = Blueprint('second_page', __name__, static_folder='static',
                        template_folder='templates')

@second_page.route('/second')
def show():
    try:

        return render_template('secondindex.html')
    except TemplateNotFound:
        abort(404)
