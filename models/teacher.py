import json
from models import db, teachers_goals_association


class Teacher(db.Model):
    __tablename__ = "teachers"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    about = db.Column(db.String(1000), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    picture = db.Column(db.String, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    goals = db.relationship('Goal', secondary=teachers_goals_association, back_populates='teachers')
    _free = db.Column('free', db.String, nullable=False)

    @property
    def free_time_slots(self):
        return json.loads(self._free)