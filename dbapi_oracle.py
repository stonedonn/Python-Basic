# pip install cx_Oracle
import cx_Oracle     #모듈 임포트

def create_connection():
    # dsn 작성
    dsn = cx_Oracle.makedsn("localhost",
                            1521,
                            "xe") #서버주소, 포트 ,SID(서비스명)

    # 접속
    db = cx_Oracle.connect("hr", "hr", dsn)  # 계정, 암호, 데이터소스이름
    return db

def test_connect():
    # 접속
    conn = create_connection()
    print(type(conn))
    conn.close()

def test_basic_query():
    # hr.employees 모든 레코드 반환
    conn = create_connection() # Connection
    cursor = conn.cursor()   # Cursor


    # SQL 실행
    sql = "SELECT * FROM employees"
    cursor.execute(sql)

    # print(cursor)
    print("fetchone")
    print(cursor.fetchone())
    print("fetchmany")
    print(cursor.fetchmany(2))

    for row in cursor.fetchall():
        print(row)

    conn.close()
if __name__ == "__main__":
    #test_connect()
    test_basic_query()