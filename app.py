from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import AddPetForm


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///pets_db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True
app.config["SECRET_KEY"] = "jkjkjkjkjkkjgghg"
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False
debug = DebugToolbarExtension(app)

connect_db(app)


@app.route("/")
def home_page():
    """Render home page"""
    pets = Pet.query.all()
    return render_template("home.html", pets=pets)


@app.route("/add", methods=["GET", "POST"])
def add_pet():
    """Renders snack form (GET) or handles snack form submission (POST)"""
    form = AddPetForm()
    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data
        new_pet = Pet(
            name=name, species=species, photo_url=photo_url, age=age, notes=notes
        )
        db.session.add(new_pet)
        db.session.commit()
        return redirect("/")
    else:
        return render_template("add_pet_form.html", form=form)


# @app.route("/employees/new", methods=["GET", "POST"])
# def add_employee():
#     form = EmployeeForm()
#     depts = db.session.query(Department.dept_code, Department.dept_name)
#     form.dept_code.choices = depts
#     if form.validate_on_submit():
#         name = form.name.data
#         state = form.state.data
#         dept_code = form.dept_code.data

#         emp = Employee(name=name, state=state, dept_code=dept_code)
#         db.session.add(emp)
#         db.session.commit()
#         return redirect("/phones")
#     else:
#         return render_template("add_employee_form.html", form=form)


@app.route("/<int:id>/", methods=["GET", "POST"])
def edit_pet(id):
    pet = Pet.query.get_or_404(id)
    form = AddPetForm(obj=pet)
    if form.validate_on_submit():
        pet.name = form.name.data
        pet.species = form.species.data
        pet.photo_url = form.photo_url.data
        pet.age = form.age.data
        pet.notes = form.notes.data
        db.session.commit()
        return redirect("/")
    else:
        return render_template("edit_pet_form.html", form=form, pet=pet)


#     @app.route("/<int:id>/edit", methods=["GET", "POST"])
# def edit_employee(id):
#     emp = Employee.query.get_or_404(id)
#     form = EmployeeForm(obj=emp)
#     depts = db.session.query(Department.dept_code, Department.dept_name)
#     form.dept_code.choices = depts

#     if form.validate_on_submit():
#         emp.name = form.name.data
#         emp.state = form.state.data
#         emp.dept_code = form.dept_code.data
#         db.session.commit()
#         return redirect("/phones")
#     else:
#         return render_template("edit_employee_form.html", form=form)
