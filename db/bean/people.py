"""
人基础实体
"""
from abc import ABC, abstractmethod


class People(ABC):
    def __init__(self, user_name, user_age, user_pwd):
        self.user_name = user_name
        self.user_age = user_age
        self.user_pwd = user_pwd

    @abstractmethod
    def get_role(self):
        pass
