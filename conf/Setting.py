"""
基础设置类
"""
import os
import sys

'''角色'''
ROLE_ADMIN = "admin"  # 管理员
ROLE_TEACHER = "teacher"  # 老师
ROLE_STU = "student"  # 学生

'''路径'''
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DB_DIR = os.path.join(BASE_DIR, 'db', 'data')
