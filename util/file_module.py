import json


class FileUtil(object):
    def read(self, path, encoding):
        with open(path, mode="r", encoding=encoding) as file:
            return file.read()

    def write(self, path, encoding, content):
        with open(path, mode="w", encoding=encoding) as file:
            return file.dump(content)

    def readToJson(self, path, encoding):
        return json.load(self.read(path, encoding))
