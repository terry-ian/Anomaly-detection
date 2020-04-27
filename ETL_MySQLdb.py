#import MySQLdb

class MyCatClass(object):
    def __init__(self):
        # 打开数据库连接

        config = {
            'host': 'localhost',
            'port': 3306,
            'user': 'root',
            'passwd': 'root',
            'db': 'test',
            'charset': 'utf8'
        }
        self.__conn_db = MySQLdb.connect(**config)

        # 使用cursor()方法获取操作游标
        self.__cursor = self.__conn_db.cursor()

    # 使用execute方法执行SQL语句
    def excute_db(self,in_sql="SELECT VERSION()"):
        num=self.__cursor.execute(in_sql)
        if num>0:
            data_list = self.__cursor.fetchall()
        return data_list
    def insert_data(self):
        sql_insert='''insert stu_info(name,age) values('哈哈',999)'''
        self.__cursor.execute(sql_insert)
        self.__conn_db.autocommit(True)
        # self.__conn_db.commit()

    def __del__(self):
        self.__cursor.close()


if __name__ == '__main__':
    obj_handle_mycat = MyCatClass()
    print(obj_handle_mycat.excute_db() )