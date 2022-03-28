from flask_wtf import FlaskForm
from wtforms import (StringField, TextAreaField)
from wtforms.validators import InputRequired, Length,DataRequired



class searchForm(FlaskForm):
    name = StringField('Search name', validators=[InputRequired(), Length(max=60)])