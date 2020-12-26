import os
import json
import mysql.connector as dbc
from mysql.connector import Error
from NiCatApp_PYTHON import settings


class DbUtil:
    def __init__(self):
        # Opening JSON file
        f = open(os.path.join(
            settings.BASE_DIR, "statsic", "DbConfig.json"))
        # returns JSON object as a dictionary
        cfg = dict(json.load(f))
        # Closing file
        f.close()

        self.host = cfg.get("host")
        self.database = cfg.get("database")
        self.user = cfg.get("user")
        self.password = cfg.get("password")
        self.port = cfg.get("port")

    def __connect__(self):
        self.con = dbc.connect(host=self.host, database=self.database,
                               user=self.user, password=self.password, port=self.port)

        self.cur = self.con.cursor()

    def fetch(self, sp, sqlParas=None):
        try:
            self.__connect__()
            if sqlParas == None:
                sqlParas = ()
            self.cur.callproc(sp, sqlParas)
            for x in self.cur.stored_results():
                result = x.fetchall()
            return result
        except:
            raise Exception("connect database error.")
        finally:
            self.__disconnect__()

    def __disconnect__(self):
        if self.con.is_connected:
            if self.cur is not None:
                self.cur.close()
            if self.con is not None:
                self.con.close()
