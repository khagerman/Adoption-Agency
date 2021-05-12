from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    FloatField,
    BooleanField,
    IntegerField,
    RadioField,
    SelectField,
    TextAreaField,
)
from wtforms.validators import InputRequired, URL, Optional, NumberRange


class AddPetForm(FlaskForm):

    name = StringField(
        "Pet Name", validators=[InputRequired(message="Pet Name can't be blank")]
    )
    species = SelectField(
        "Species", choices=[("cat", "Cat"), ("dog", "Dog"), ("porcupine", "Porcupine")]
    )
    photo_url = StringField("Image Url", validators=[Optional(), URL()])
    age = IntegerField("Age", [Optional(), NumberRange(min=0, max=30)])
    notes = StringField("Notes")


class EditPetForm(FlaskForm):
    photo_url = StringField("Image Url", validators=[Optional(), URL()])
    notes = StringField("Notes")
    available = BooleanField("Available to Adopt?")
