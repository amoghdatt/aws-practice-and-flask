from flask import Blueprint, render_template

test = Blueprint('test', __name__, template_folder='templates')


@test.route('/')
def index():
    return render_template('test.html')
