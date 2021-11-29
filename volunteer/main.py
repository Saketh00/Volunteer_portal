import psycopg2
import sys

def user_list():
    dbconn=psycopg2.connect("dbname=volunteer")
    cursor=dbconn.cursor()
    cursor.execute("select * from users")
    udetails=cursor.fetchall()
    print(udetails[0])


def Insert():
    dbconn=psycopg2.connect("dbname=volunteer")
    cursor=dbconn.cursor()
    f=open("sql/insert.sql")
    sql_code=f.read()
    f.close()
    cursor.execute(sql_code)
    dbconn.commit()

def Create():
    dbconn=psycopg2.connect("dbname=volunteer")
    cursor=dbconn.cursor()
    f=open("sql/000_create.sql")
    sql_code=f.read()
    f.close()
    cursor.execute(sql_code)
    dbconn.commit()

def main(arg):
    if arg == "Create":
        Create()
    elif arg=="Insert":
        Insert()
    elif arg=="ListUser":
        user_list()
    else:
        print(f"Unknown command {arg}")

if __name__=="__main__":
    main(sys.argv[1])