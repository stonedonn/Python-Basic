# 모듈 임포트
import sqlite3, os
from sqlite3 import Error


# 접속 함수
def create_connection(db_file):
    # ./database 디렉터리 생성
    if not os.path.exists("./database"): # 현재 디렉터리 아래 database 디렉터리가 없으면
        os.makedirs("./database")

    # 접속
    try:
        conn = sqlite3.connect(db_file)  # db_file 데이터베이스 전송-> connection 객체 반환
        print(sqlite3.version) #
    except Error as e:
        print(e, type(e))
        return None # 접속 실패시 None 리턴
    return conn

def test_connection(db_file):
    conn = create_connection(db_file)
    print(type(conn))
    conn.close()

def test_create_table(db_file):
    # 접속
    conn = create_connection(db_file)   #Connection
    # 커서 획득
    cursor = conn.cursor() # Cursor 객체 반환
    # sql 작성
    ddl = """CREATE TABLE IF NOT EXISTS
    customer (
        id integer primary key autoincrement,
        name varchar(20),
        category integer,
        region varchar(10))
    """

    # sql 실행
    cursor.execute(ddl)
    # 접속 해제
    conn.close()


if __name__ == "__main__":
    db_file = "./database/mysqlite.db"
    # test_connection(db_file)
    test_create_table(db_file)