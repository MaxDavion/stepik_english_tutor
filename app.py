import os
import random
from flask import Flask, render_template, request
from flask_script import Manager
import forms
# import db_manager
from flask import Flask
from flask_migrate import Migrate, MigrateCommand
from models import db
from models.teacher import Teacher
from models.goal import Goal
from sqlalchemy.sql.expression import func


app = Flask(__name__)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
db.reflect(app=app)
manager = Manager(app)
migrate = Migrate(app, db)
# db.create_all()
manager.add_command('db', MigrateCommand)


@app.route('/')
def main():
    return render_template(
        "index.html",
        goals=Goal.query.all(),
        teachers=Teacher.query.order_by(func.random()).limit(6).all()
    )


@app.route('/goals/<goal>/')
def goals(goal):
    return render_template(
        "goal.html",
        goal=Goal.query.filter(Goal.key == goal).first(),
        teachers=Teacher.query.filter(Teacher.goals.any(key=goal)).all()
    )


@app.route('/profiles/<int:teacher_id>/')
def profile(teacher_id):
    return render_template(
        "profile.html",
        teacher=Teacher.query.get_or_404(teacher_id)
    )


@app.route('/request/', methods=['POST', 'GET'])
def teacher_request():
    form = forms.RequestForm()
    form.goals.choices = [(i.key, i.name) for i in Goal.query.all()]
    if request.method == 'POST':
        if form.validate_on_submit():
            db_manager.insert_request(**form.data)
            return render_template('request_done.html', form=form)

    return render_template('request.html', form=form)


@app.route('/booking/<int:teacher_id>/<weekday>/<time>', methods=["POST", "GET"])
def booking(teacher_id, weekday, time):
    form = forms.BookingForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            db_manager.insert_booking(**form.data)
            return render_template("booking_done.html", form=form)

    return render_template(
        "booking.html",
        teacher=db_manager.get_all_teachers(filter_by_id=teacher_id)[0],
        weekday=weekday,
        time=time,
        form=form
    )


@app.template_filter('as_rus_weekday')
def as_rus_weekday(day):
    """ Вернуть день недели """
    return {'mon': 'Понедельник', 'tue': 'Вторник', 'wed': 'Среда',
            'thu': 'Четверг', 'fri': 'Пятница', 'sat': 'Суббота',
            'sun': 'Воскресенье'}[day]


# @app.template_filter('as_goal_title')
# def as_goal_title(goal):
#     """ Вернуть название переданной цели """
#     return db_manager.get_all_goals(filter_by_key=goal)[0]['name']


if __name__ == '__main__':
    app.run()