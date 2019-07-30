from flask import Flask

def create_app():
    app = Flask(__name__)
    app.register_blueprint(simple_page)
    app.register_blueprint(second_page)
    return app