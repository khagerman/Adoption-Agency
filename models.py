from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)


no_img = (
    "https://www.zacspeed.com/wp-content/uploads/2016/05/Image-not-yet-available.jpg"
)


class Pet(db.Model):
    """Pet model."""

    __tablename__ = "pets"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    species = db.Column(db.Text, nullable=False)
    photo_url = db.Column(db.Text, default=no_img)
    age = db.Column(db.Integer, nullable=True)
    notes = db.Column(db.Text, nullable=True)
    available = db.Column(db.Boolean, default=True)

    def image_url(self):
        """Return image for pet"""

        return self.photo_url or no_img
