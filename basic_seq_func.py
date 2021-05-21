def using_range():
    #range 객체 범위생성
    #인자가 1개 : 0부터 인자 경계 이전
    seq = range(10) # 0~9까지
    print(seq,type(seq))

    # 인자가 2개: 시작경게, 끝경계
    seq2 = range(2, 10) # 2~9까지
    print(seq2)
    print(list(seq2))

    # 인자가 3개: 시작경계, 끝경계, 증감값
    seq3 = range(2, 10, 2) # 2~ 9까지 2씩 증가
    print(seq3)
    print(list(seq3))

    # 증감값이 음수: 큰 숫자-> 작은 숫자
    seq4 = range(0, -10, -1) # 0이, -10초과 역순 정수
    print(seq4)
    print(list(seq4))

    # 실제 값은 가지고 있지 않지만 순차 객체
    print(seq, "LENGTH:", len(seq))

    # 포함여부 확인 가능
    print(5 in seq)
    # 인덱스를 이용, 내부 데이터 접근 가능
    print(seq[0], seq[1], seq[2]) # 정인덱싱
    print(seq[-1], seq[-2], seq[-3]) # 역인덱싱

    # 슬라이싱 가능
    print(seq[2:5])
    # 불변 객체 -> 인덱스 이용 치환, 슬라이싱을 이용한 치환 등은 불가

    # range 객체를 이용한 for 루프 예제
    for i in range(10): # 시작 0, 끝 9, 간격 1
        print(i, end=" ")
    else:
        print()


def using_enumerate():
    """
    enumrate 함수 : 순차형에서 현재 아이템과 함께 내부 인덱스도 함께 필요할 때 사용
    """
    colors = ["red", "yellow", "blue", "white", "grey"]

    i = 0
    for color in colors: # 항목값은 확인할 수 있지만, 인덱스는 확인불가
        print("COLOR {0}: {1}".format(i, color))
        i += 1
    print("=============enumrate")
    for index, color in enumerate(colors): #(index, 항목) -> unpacking
        print("COLOR {}: {}".format(index, color))

def using_zip():
    # zip 객체 : 여러 개의 순차 자료형을 동시에 루프 시키는 객체
    english = "Sun", "Mon", "Tue", "Wed"
    korean = "일요일", "월요일", "화요일", "수요일", "목요일"
    engkor = zip(english, korean) #묶이는 조합의 길이는 짧은 쪽으로 맞춰짐

    print(engkor, type(engkor))

    # 기본 순회
    for pair in engkor: # 조합의 튜플 반환
        print(pair, type(pair))

    # zip 객체는 일회성 객체이다 -> 위에서 한번 순회하고 없어짐 다시 선언
    engkor = zip(english, korean)

   # 언패킹 순회
    for eng, kor in engkor: # 조합의 튜플 -> 언패킹
        print(eng, "->", kor)

    # 인덱스, 영어, 한국어
    engkor = zip(english, korean)
    for index, (eng, kor) in enumerate(engkor):
        print(index, eng, kor)

    # zip 객체를 이용, dict를 생성가능
    print(dict(zip(english,korean)))



if __name__ == "__main__":
    # using_range()
    # using_enumerate()
    using_zip()