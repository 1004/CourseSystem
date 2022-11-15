"""
老师实体
"""
from db.bean.people import People
from conf import Setting


class TeacherBean(People):
    def __init__(self, user_name, user_age, user_pwd):
        super(TeacherBean, self).__init__(user_name, user_age, user_pwd)

    def get_role(self):
        return Setting.ROLE_TEACHER
