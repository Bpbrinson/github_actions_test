from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email

class Contact(FlaskForm):
    name = StringField("Name: ", [DataRequired()])
    email = StringField("Email: ", [DataRequired(), Email()])
    message = TextAreaField("Message: ", [DataRequired()])
    submit = SubmitField("Submit")