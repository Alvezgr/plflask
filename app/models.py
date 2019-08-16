"""Module for user model"""

from flask_login import UserMixin
from .firestore_service import get_user

class UserData:
    """UserData class"""

    def __init__(self, username, password):
        self.username = username
        self.password = password


class UserModel(UserMixin):
    """the property user model"""
    def __init__(self, user_data):
        """
        :params user_data: UserData
        """
        self.id = user_data.username
        self.password = user_data.password

    @staticmethod
    def query(user_id):
        """the query method"""

        user_doc = get_user(user_id)
        user_data = UserData(
            username=user_doc.id,
            password=user_doc.to_dic()['password']
        )
        return UserModel(user_data)