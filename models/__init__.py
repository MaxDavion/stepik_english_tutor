from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

teachers_goals_association = db.Table('teachers_goals',
    db.Column('teacher_id', db.Integer, db.ForeignKey('teachers.id')),
    db.Column('goal_id', db.Integer, db.ForeignKey('goals.id'))
)