from flask import Flask
from app.simple_page import simple_page
from second.secondapp import second_page

app = Flask(__name__)
app.register_blueprint(simple_page)
app.register_blueprint(second_page)