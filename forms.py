from flask_wtf import FlaskForm
from wtforms import StringField, RadioField, SubmitField, HiddenField
from wtforms.validators import Length


class RequestForm(FlaskForm):
    title = StringField('Подбор преподавателя')
    subtitle = StringField('Напишите, чего вам нужно и мы подберем отличных ребят')

    goals = RadioField(
        'Какая цель занятий?',
        default="travel")

    free_times = RadioField('Сколько времени есть?', choices=[
        ("1-2 часа в неделю", "1-2 часа в неделю"),
        ("3-5 часов в неделю", "3-5 часов в неделю"),
        ("5-7 часов в неделю", "5-7 часов в неделю"),
        ("7-10 часов в неделю", "7-10 часов в неделю")
    ], default="3-5 часов в неделю")

    name = StringField("Вас зовут", [Length(min=1, message="Имя должно содержать не менее одного символа")])
    phone = StringField("Ваш телефон", [Length(min=7, message="Номер телефона должен содержать не менее 7и символов")])
    submit = SubmitField('Найдите мне преподавателя')



class BookingForm(FlaskForm):
    name = StringField("Вас зовут", [Length(min=1, max=50, message="Имя должно содержать не менее одного символа")])
    phone = StringField("Ваш телефон", [Length(min=7, max=30, message="Номер телефона должен содержать не менее 7и символов")])

    weekday = HiddenField()
    time = HiddenField()
    teacher_id = HiddenField()

    submit = SubmitField('Записаться на пробный урок')