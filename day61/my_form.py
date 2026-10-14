from flask_wtf import FlaskForm
from wtforms import StringField, validators
from wtforms.fields.simple import PasswordField, SubmitField


class MyForm(FlaskForm):
        email = StringField(name="email", label="Email Address",  validators=[validators.input_required(), validators.email()])
        password = PasswordField(name="password", label="Password", validators=[validators.input_required(), validators.length(8)])
        button = SubmitField(name='login', label="Login")