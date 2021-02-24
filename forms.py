from wtforms import SelectField, StringField, PasswordField, SubmitField, Form, IntegerField
from wtforms.validators import DataRequired, Email
from flask_wtf import Flaskform

class registration_form(Form):
    email = StringField("Please input your email", validators=[DataRequired(), Email()])
    username = StringField("Please input your Username", validators=[DataRequired()])
    password = PasswordField("input password", validators=[DataRequired()])
    submit = SubmitField("Submit")