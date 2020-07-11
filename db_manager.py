import json
import os

DATABASE_FOLDER = 'db'


def insert_request(**kwargs):
    insert_entry(
        filename="requests.json",
        data={
            'goals': kwargs.get('goals'),
            'free_times': kwargs.get('free_times'),
            'name': kwargs.get('name'),
            'phone': kwargs.get('phone')
        })


def insert_booking(**kwargs):
    insert_entry(
        filename="booking.json",
        data={
            'name': kwargs.get('name'),
            'phone': kwargs.get('phone'),
            'time': kwargs.get('time'),
            'teacher_id': kwargs.get('teacher_id'),
            'weekday': kwargs.get('weekday')
        })


def insert_entry(filename, data):
    # Если нет файла, то создаем его в начальном состоянии (пустым списокм записей)
    if not os.path.exists(f"{DATABASE_FOLDER}/{filename}"):
        with open(f"{DATABASE_FOLDER}/{filename}", "w") as file:
            json.dump([], file)

    with open(f"{DATABASE_FOLDER}/{filename}", "r", encoding='utf8') as f:
        all_entries = json.load(f)

    all_entries.append(data)

    with open(f"{DATABASE_FOLDER}/{filename}", "w") as file:
        json.dump(all_entries, file, indent=4, ensure_ascii=False)


def get_all_teachers(filter_by_id=None, filter_by_goal=None):
    with open(f"{DATABASE_FOLDER}/teachers.json", "r", encoding='utf8') as f:
        result = json.load(f)

    if filter_by_id:
        result = [i for i in result if i["id"] == filter_by_id]
    if filter_by_goal:
        result = [i for i in result if filter_by_goal in i["goals"]]

    return result


def get_all_goals(filter_by_key=None):
    with open(f"{DATABASE_FOLDER}/goals.json", "r", encoding='utf8') as f:
        result = json.load(f)

    if filter_by_key:
        result = [i for i in result if i["key"] == filter_by_key]

    return result
