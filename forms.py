from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, IntegerField, validators

class User(FlaskForm):
    email = StringField("email", validators=[validators.Length(500)])