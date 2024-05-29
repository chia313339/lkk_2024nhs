from flask import Flask
from app.route import *

def create_app():
    app = Flask(__name__)
    app.jinja_env.variable_start_string = '[['
    app.jinja_env.variable_end_string = ']]'
    app.add_url_rule('/', 'index', index, methods=['GET', 'POST'])
    app.add_url_rule('/about', 'about', about, methods=['GET', 'POST'])
    app.add_url_rule('/inbody', 'inbody', inbody, methods=['GET', 'POST'])

    app.register_error_handler(404, page_not_found)
    return app