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
from wtforms.validators import InputRequired, Email, Optional


class AddPetForm(FlaskForm):

    name = StringField(
        "Pet Name", validators=[InputRequired(message="Pet Name can't be blank")]
    )
    species = StringField(
        "Species", validators=[InputRequired(message="Species can't be blank")]
    )
    img = StringField("Image Url")
    age = IntegerField("Age")
    notes = StringField("Notes")


#     # category = RadioField("Category", choices=[
#     #                       ('ic', 'Ice Cream'),  ('chips', 'Potato Chips'),  ('candy', 'Candy/Sweets')])
#     category = SelectField(
#         "Category",
#         choices=[
#             ("ic", "Ice Cream"),
#             ("chips", "Potato Chips"),
#             ("candy", "Candy/Sweets"),
#         ],
#     )


# class EmployeeForm(FlaskForm):
#     name = StringField(
#         "Employee Name", validators=[InputRequired(message="Name cannot be blank")]
#     )
#     state = SelectField("State", choices=[(st, st) for st in states])
#     dept_code = SelectField("Department Code")
