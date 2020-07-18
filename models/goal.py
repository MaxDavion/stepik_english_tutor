from models import db


class Goal(db.Model):
    __tablename__ = "goals"
    id = db.Column(db.Integer, primary_key=True)
    key = db.Column(db.String(50), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    icon = db.Column(db.String, nullable=False)



