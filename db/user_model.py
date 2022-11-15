"""
用户数据层
"""
from db.db_handler import DbHandler
import os
import sys
from conf import Setting


class UserModel:
    def __init__(self):
        self.dbHandler = DbHandler()

    def save(self, people):
        path = os.path.join(Setting.DB_DIR, people.get_role(), people.user_name)
        self.dbHandler.save(path, people)

    def query(self, role, user_name):
        path = os.path.join(Setting.DB_DIR, role, user_name)
        return self.dbHandler.query(path)

    def delete(self, role, user_name):
        path = os.path.join(Setting.DB_DIR, role, user_name)
        if os.path.exists(path):
            os.remove(path)
