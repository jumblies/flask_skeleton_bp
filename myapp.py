#imports from root project directory
from flask import Flask
from simple.simple_page import simple_page
from second.secondapp import second_page

# Application factory
# imports modules above.
def create_app():
    app = Flask(__name__)
    app.register_blueprint(simple_page)
    app.register_blueprint(second_page)
    return app

# calls __init__.py which is serving as both init and application factory. 
app = create_app()