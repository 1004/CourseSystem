"""
数据操作类
"""
import os
import pickle


class DbHandler:

    def save(self, path, data):
        if not os.path.exists(os.path.dirname(path)):
            os.makedirs(os.path.dirname(path))

        with open(path, mode='wb') as f:
            pickle.dump(data, f)

    def query(self, path):
        if not os.path.exists(path):
            return None

        with open(path, mode='rb') as f:
            return pickle.load(f)
