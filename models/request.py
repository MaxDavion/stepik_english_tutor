from models import db, teachers_goals_association


class Request(db.Model):
    __tablename__ = "requests"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    phone = db.Column(db.String(50), nullable=False)
    free_times = db.Column(db.String(100), nullable=False)

    goal = db.relationship("Goal")
    goal_id = db.Column(db.Integer, db.ForeignKey('goals.id'))




