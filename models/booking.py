from models import db, teachers_goals_association


class Booking(db.Model):
    __tablename__ = "bookings"
    id = db.Column(db.Integer, primary_key=True)
    phone = db.Column(db.String(50), nullable=False)
    name = db.Column(db.String(50), nullable=False)
    time = db.Column(db.String, nullable=False)
    weekday = db.Column(db.String(100), nullable=False)

    teacher = db.relationship("Teacher")
    teacher_id = db.Column(db.Integer, db.ForeignKey('teachers.id'))

    @classmethod
    def add(cls, **kwargs) -> 'Booking':
        new_entry = cls(
                phone=kwargs.get('phone'),
                name=kwargs.get('name'),
                time=kwargs.get('time'),
                weekday=kwargs.get('weekday'),
                teacher=kwargs.get('teacher')
            )
        db.session.add(new_entry)
        return new_entry

    def commit(self):
        db.session.commit()
