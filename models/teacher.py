from models import db


class Teacher(db.Model):
    __tablename__ = "teachers"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    about = db.Column(db.String(1000), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    picture = db.Column(db.String, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    goals = db.Column(db.String, nullable=False)
    free = db.Column(db.String, nullable=False)

