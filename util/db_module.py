import mysql.connector as dbc
from mysql.connector import Error


class DbUtil(object):
    # def __getConnection(self):
    #     return dbc.connect(host='localhost', database='NiCatBT', user='root', password='chenni0427', port=3306)

    # @staticmethod
    # def DoSave(self, sp, **sqlParas):
    #     try:
    #         connection = self.__getConnection()
    #         cursor = connection.cursor()
    #         cursor.callproc(sp, sqlParas)
    #         return cursor.stored_results()
    #     except dbc.Error as error:
    #         print("Failed to execute stored procedure: {}".format(error))
    #     finally:
    #         if (connection.is_connected()):
    #             cursor.close()
    #             connection.close()

    @staticmethod
    def DoQuery(sp, sqlParas=None):
        try:
            cn = dbc.connect(host='localhost', database='NiCatBT',
                             user='root', password='chenni0427', port=3306)
            if sqlParas == None:
                sqlParas = ()
            cursor = cn.cursor()
            cursor.callproc(sp, sqlParas)
            for x in cursor.stored_results():
                result = x.fetchall()
            return result
        except dbc.Error as error:
            print("Failed to execute stored procedure: {}".format(error))
        finally:
            if (cn.is_connected()):
                cursor.close()
                cn.close()
