import pymysql
import pandas as pd
from pandas import Series,DataFrame


# 也可以使用字典进行连接参数的管理
config = {
    'host': 'remotemysql.com',
    'port': 3306,
    'user': 'DVpSg4fy2F',
    'passwd': '3V6Bb9tZQo',
    'db': 'DVpSg4fy2F',
    'charset': 'utf8'
}

#sql写入rowdata表格中语句
def sql_insert(url,postdate,bank,title,content):
    db = pymysql.Connect(**config)
    cursor = db.cursor() # 创建一个游标对象
    # 插入语句
    sql = "INSERT INTO bank_webcrawler(url,postdate,bank,title,content) "  "VALUES ('%s','%s','%s','%s','%s')" % (url,postdate,bank,title,content)
    try:
        cursor.execute(sql)  # 执行 SQL 插入语句
    except:
        db.rollback()  # 如果发生错误则回滚
    db.commit() # 提交到数据库执行

    #finally:
    cursor.close() #关闭游标
    db.close() #关闭连接

#sql查询语句	
def sql_select(sqlcontent):
    db = pymysql.Connect(**config)
    df = pd.read_sql(sqlcontent, con=db)  
    db.close() #关闭连接
    return(df)



#一对多
df1=DataFrame({'key':['b','b','a','c','a','a','b'],'data1':range(7)})
df2=DataFrame({'key':['a','b','d'],'data2':range(3)})

pd.merge(df1,df2,on='key')


