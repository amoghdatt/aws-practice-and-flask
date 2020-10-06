from flask import Blueprint, render_template
from snakeeyes.blueprints.feedback import forms

feedback = Blueprint('feedback', __name__, template_folder='templates')


@feedback.route('/', methods=['GET', 'POST'])
def index():
    form = forms.FeedbackForm()
    return render_template('index.html', form=form)
