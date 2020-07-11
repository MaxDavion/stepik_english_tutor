import data
import os
import db_manager


def load_goals_with_icons():
    return [{
        "key": i[0],
        "name": i[1],
        "icon": {"travel": "⛱", "study": "🏫", "work": "🏢", "relocate": "🚜"}.get(i[0], "🎁")
    } for i in data.goals.items()]


def create_db(rewrite_if_db_exists=True):
    """ Загрузить первоначальные данные в БД
    :param rewrite_if_db_exists: True - перезатереть базу если она уже существует, False - не перезатирать
    :return:
    """
    if os.path.exists(db_manager.DATABASE_FOLDER) and rewrite_if_db_exists == False:
        return None

    if not os.path.exists(db_manager.DATABASE_FOLDER):
        os.makedirs(db_manager.DATABASE_FOLDER)

    for goal in load_goals_with_icons():
        db_manager.insert_entry("goals.json", data=goal)

    for teacher in data.teachers:
        db_manager.insert_entry("teachers.json", data=teacher)


if __name__ == '__main__':
    create_db()
