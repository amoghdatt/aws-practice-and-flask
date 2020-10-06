from flask_wtf import Form
from wtforms import TextAreaField, BooleanField
from wtforms_components import EmailField
from wtforms.validators import DataRequired, Length


class FeedbackForm(Form):
    email = EmailField("what's your email address?",
                       [DataRequired(), Length(3, 254)])
    feedback_message = TextAreaField("Enter your feedback",
                                     [DataRequired(), Length(1, 819)])
    anonymous = BooleanField("submit anonymous feedback")
