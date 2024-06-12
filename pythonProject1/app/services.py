from app import db
from app.models import User

#CRUD create read update delete
def create_user(first_name, last_name):
    new_user = User(first_name=first_name, last_name=last_name)
    db.session.add(new_user)
    db.session.commit()

def get_all_users():
    return User.query.all()

# def update_user_first_name(old_first_name, new_first_name):
#     user_to_update = User.query.filter_by(first_name=old_first_name).first()
#     if user_to_update:
#         user_to_update.first_name = new_first_name
#         db.session.commit()
#
# def delete_user(first_name):
#     user_to_delete = User.query.filter_by(first_name=first_name).first()
#     if user_to_delete:
#         db.session.delete(user_to_delete)
#         db.session.commit()
