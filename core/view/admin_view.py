"""
管理员视图层
    1. 注册
    2. 登录
    3. 创建学校
    4. 删除学校
    5. 新增班级
    6. 删除班级
    7. 新增课程
    8. 删除课程
"""
from interface.user_service import UserService
from conf import Setting


class AdminView:
    user_name = None

    def __init__(self):
        self.userService = UserService()

    def run(self):
        print("欢迎来到管理员视图")
        self.__real_run()
        print("退出管理员视图")

    def __real_run(self):
        dict = {
            'q': ['退出管理员页面'],
            '1': ['注册', self.admin_register],
            '2': ['登录', self.admin_login],
            '3': ['创建学校', self.admin_create_school()]
        }
        while True:
            print("指令如下：")
            for k, v in dict.items():
                print(f"{k}:{v[0]}")
            code = input("请输入指令").strip()
            if code == 'q':
                break
            elif code in dict:
                dict.get(code)[1]()
            else:
                print("指令有错")

    def admin_register(self):
        print("欢迎来到管理员注册视图")
        while True:
            user_name = input("请输入用户名:").strip()
            user_pwd = input("请输入吗密码:").strip()
            user_repeat_pwd = input("请再一次输入密码").strip()
            user_age = input("请输入年龄").strip()
            flag, obj = self.userService.register(Setting.ROLE_ADMIN, user_name, user_pwd, user_repeat_pwd, user_age)
            if flag:
                print("注册成功")
                break
            else:
                print(f"注册失败:{obj}")

    def admin_login(self):
        print("欢迎来到登录视图")
        while True:
            user_name = input("请输入用户名:").strip()
            user_pwd = input("请输入吗密码:").strip()
            flag, obj = self.userService.login(Setting.ROLE_ADMIN, user_name, user_pwd)
            if flag:
                print("登录成功")
                AdminView.user_name = obj.user_name
                break
            else:
                print(f"登录失败:{obj}")

    def admin_create_school(self):
        ...

    def admin_create_grade(self):
        ...

    def admin_create_course(self):
        ...
