import json


class FileUtil(object):
    def __init__(self):
        self.r_sign = "r"
        self.w_sign = "w"

    def read(self, path, encoding):
        with open(path, mode=self.r_sign, encoding=encoding) as file:
            return file.read()

    def write(self, path, encoding, content):
        with open(path, mode=self.w_sign, encoding=encoding) as file:
            return file.dump(content)

    def readToJson(self, path, encoding):
        return json.load(self.read(path, encoding))
