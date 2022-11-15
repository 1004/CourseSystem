"""
学生实体
"""
from db.bean.people import People
from conf import Setting


class StudentBean(People):
    def __init__(self, user_name, user_age, user_pwd):
        super(StudentBean, self).__init__(user_name, user_age, user_pwd)

    def get_role(self):
        return Setting.ROLE_STU
