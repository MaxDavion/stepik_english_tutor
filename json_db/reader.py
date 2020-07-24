import json


DATABASE_FOLDER = 'db'


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
