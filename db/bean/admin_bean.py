"""
管理员实体
"""
from db.bean.people import People
from conf import Setting


class AdminBean(People):
    def __init__(self, user_name, user_age, user_pwd):
        super(AdminBean, self).__init__(user_name, user_age, user_pwd)

    def get_role(self):
        return Setting.ROLE_ADMIN


if __name__ == '__main__':
    a = AdminBean('kk', 2)
    print(a.__dict__)
