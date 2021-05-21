def define_dict():
    """
    사전 생성 연습
    """
    # 빈 사전
    dct = dict()
    print(dct,type(dct))
    # Literal : {} 이용
    dct = {"basketball": 5, "baseball": 9}

    # 사전 객체는 순서가 없고, 인덱스가 아닌 키를 이용해 내용에 접근
    dct['volleyball'] = 6

    print(dct)
    # 길이 확인 가능, 포함 여부 확인 가능 -> 대상은 키 목록을 대상으로 함
    # 연결, 반복 지원 안함
    print("LENGTH of dct:", len(dct))
    print("soccer 키가 있는가?", "soccer" in dct)
    print("baseball 키가 있는가?","baseball" in dct)

    # 키의 목록, 값의 목록
    print("키의 목록:",dct.keys(), type(dct.keys()))
    print("값의 목록:",dct.values(),type(dct.keys()))
    print("(키, 값) 쌍튜플의 목록:", dct.items(),type(dct.items()))

    # 응용
    # 포함 여부는 key를 대상으로 한다
    # 사전의 값의 포함여부를 확인?
    # dct의 값 중에서 9 값이 포함되어 있는가 ?
    print("9 in 값 목록?", 9 in dct.values())

if __name__ == "__main__":
    define_dict()