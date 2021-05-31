# pip install pymongo
from pymongo import MongoClient

# 접속 함수
def connect():
    client = MongoClient("mongodb://localhost:27017")
    return client

# 접속 테스트
def test_connect():
    conn = connect()
    # print(dir(conn))
    print("데이터베이스:")
    for db in conn.list_database_names():
        print(db)


# 컬렉션 확인
def test_collection():
    # 접속
    conn = connect()
    # 사용할 데이터베이스 선택
    db = conn['mydb'] # use mydb
    # 컬렉션 선택
    coll = db['pymongo']
    return coll


def test_insert():
    # 컬렉션 확보
    coll = test_collection()

    # 한개 문서 삽입
    x = coll.insert_one({
        "name": "홍길동",
        "address": "서울"
    }) # 새로 생성된 Document의 _id를 반환

    # 결과 확인
    print(x.inserted_id)


def test_insert_many():
    coll = test_collection()

    # 여러 문서 삽입시에는 []로 문서 전달
    xs = coll.insert_many([
        { "name": "고길동", "address": "서울", "method": "insert_many" },
        { "name": "장길산", "method": "insert_many"},
        { "name": "임꺽정", "job": "도적"}
    ])
    # insert_many -> insered_ids
    print(xs.inserted_ids)
    print(len(xs.inserted_ids), "개 레코드 삽입되었음")

from datetime import datetime

def test_update():
    # address == "서울"인 문서
    # method -> update, modified_at -> 현재 시간
    coll = test_collection()

    xs = coll.update_many({ "address": "서울" },  # 조건
                          { '$set': {
                              "method": "update",
                              "modified_at": datetime.now()
                          }}
                          )
    print(xs.matched_count, "개가 매칭 되었습니다.") # 조건에 맞는 문서의 개수
    print(xs.modified_count, "개가 갱신 되었습니다.") # 실제 변경된 문서 개수


def test_select_by_filter(filter={}, projection={}):
    """
    db.collection.find({ 조건 }, { projection })
        프로젝션은 값 1:표시, 값 0, 표시 안함
    """
    coll = test_collection()
    docs = coll.find(filter, projection)

    for doc in docs:
        print(doc)


if __name__ == "__main__":
    # test_connect()
    # test_insert()
    # test_insert_many()
    # test_update()
    test_select_by_filter(projection={
        "name": 1, "address": 1, "_id": 0
    }) # filter={}, projection={}
    # SELECT * FROM 테이블 WHERE 컬럼 LIKE ->
    # 정규식을 이용, 패턴 전달