"""
整体view 层
"""
from core.view.admin_view import AdminView


class MainView:
    def __init__(self):
        self.admin_view = AdminView()

    def run(self):
        print("欢迎来到课程系统:")
        self.__real_run()
        print("退出课程系统")

    def __real_run(self):
        dict = {
            "1": ["管理员", 'in_admin_view'],
            "2": ["教师", 'in_teacher_view'],
            "3": ["学生", 'in_student_view']
        }
        while True:
            for k, v in dict.items():
                print(f"{k}:{v[0]}")
            print("q: 退出系统")
            role = input('请输入角色编号: ').strip()
            if role == 'q':
                break
            elif role in dict:
                fun_name = dict.get(role)[1]
                if hasattr(self, fun_name):
                    getattr(self, fun_name)()
                else:
                    print("能力注册有误")
            else:
                print("编码输入有误,重新输入")

    # 管理员角色view
    def in_admin_view(self):
        self.admin_view.run()

    # 老师角色
    def in_teacher_view(self):
        pass

    # 学生角色
    def in_student_view(self):
        pass
