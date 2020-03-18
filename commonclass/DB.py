import psycopg2
from  commonclass.readConfig import readConfig
from  commonclass.readexcel import doExcel

class sqlclass:
    def ExcuteSql(db,sql):
        if (db == "" or sql == ""):
            return
        DB = doExcel.getDB(sql);
        DBname = DB
        host = readConfig.getValue(DBname,'db_host')
        user = readConfig.getValue(DBname,'db_user')
        password = readConfig.getValue(DBname,'db_pass')
        port = readConfig.getValue(DBname,'db_port')
        conn = psycopg2.connect(
            host = host,
            port = int(port),
            password = password,
            uesr = user,
            DBname = DBname,
            charset = 'utf-8')
        print("Opened database successfully")
        cursor  = conn.cursor()
        try:
         cursor.execute(sql)
         print("正在执行sql："+sql)
         conn.commit()
         print("执行成功！")
        except:
         print("执行出错了，请检查sql：" + sql)
         conn.rollback();
         conn.close()
        return cursor.fetchone()


