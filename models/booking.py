from models import db, teachers_goals_association


class Booking(db.Model):
    __tablename__ = "bookings"
    id = db.Column(db.Integer, primary_key=True)
    phone = db.Column(db.String, nullable=False)
    time = db.Column(db.String, nullable=False)
    weekday = db.Column(db.String(100), nullable=False)

    teacher = db.relationship("Teacher")
    teacher_id = db.Column(db.Integer, db.ForeignKey('teachers.id'))

