#-*-coding:utf-8-*-
import  pymysql

def  db_text():
    db = pymysql.connect(host = "localhost", port = 3307, user = "root", password =  "root", database = "python_text",
                         charset = "utf8")
    cursor = db.cursor()
    cursor.execute("select version()")
    data = cursor.fetchone()
    print(data)
    db.close()

def main():
    db_text()

if __name__=="__main__":
    main()
