"""
用户逻辑层
    1. 注册
    2. 登录
    3. 查询用户信息
"""
from db.user_model import UserModel
from conf import Setting
from db.bean.admin_bean import AdminBean
from db.bean.teacher_bean import TeacherBean
from db.bean.student_bean import StudentBean


class UserService:
    def __init__(self):
        self.userModel = UserModel()

    def register(self, role, user_name, user_pwd, repeat_pwd, user_age):
        if len(user_name) == 0 or len(role) == 0 or len(user_pwd) == 0 or len(repeat_pwd) == 0:
            return False, "信息输入有误"
        if user_pwd != repeat_pwd:
            return False, "2次密码不正确"
        if not user_age.isdigit():
            return False, "年龄必须是数字"

        oldObj = self.userModel.query(role, user_name)
        if oldObj:
            return False, "用户已经存在"
        obj = None
        if role == Setting.ROLE_ADMIN:
            obj = AdminBean(user_name, user_age, user_pwd)
        elif role == Setting.ROLE_STU:
            obj = StudentBean(user_name, user_age, user_pwd)
        elif role == Setting.ROLE_TEACHER:
            obj = TeacherBean(user_name, user_age, user_pwd)

        if obj:
            self.userModel.save(obj)
            return True, "注册成功"
        else:
            return False, "角色不对"

    def login(self, role, user_name, user_pwd):
        obj = self.userModel.query(role, user_name)
        if not obj:
            return False, "用户未注册"
        elif obj.user_pwd != user_pwd:
            return False, "密码不正确"
        else:
            return True, obj
