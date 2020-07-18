"""empty message

Revision ID: ecdd38a14c4b
Revises: 
Create Date: 2020-07-18 15:32:22.198889

"""
from alembic import op
import sqlalchemy as sa
from models import db
from models.teacher import Teacher
from models.goal import Goal
import db_manager
import json

# revision identifiers, used by Alembic.
revision = 'ecdd38a14c4b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('goals',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('key', sa.String(length=50), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('icon', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('teachers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('about', sa.String(length=1000), nullable=False),
    sa.Column('rating', sa.Integer(), nullable=False),
    sa.Column('picture', sa.String(), nullable=False),
    sa.Column('price', sa.Integer(), nullable=False),
    sa.Column('goals', sa.String(), nullable=False),
    sa.Column('free', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###

    goals = []
    for goal in db_manager.get_all_goals():
        goals.append(
            Goal(
                key=goal['key'],
                name=goal['name'],
                icon=goal['icon']
            ))
    db.session.add_all(goals)
    db.session.commit()

    teachers = []
    for teacher in db_manager.get_all_teachers():
        teachers.append(
            Teacher(
                id=teacher['id'],
                name=teacher['name'],
                about=teacher['about'],
                rating=teacher['rating'],
                picture=teacher['picture'],
                price=teacher['price'],
                goals=" ".join(teacher['goals']),
                free=json.dumps(teacher['free'])
            ))
    db.session.add_all(teachers)
    db.session.commit()


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('teachers')
    op.drop_table('goals')
    # ### end Alembic commands ###