numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9} #전체 집합
evens = {0, 2, 4, 6, 8} #짝수 집합
odds ={1, 3, 5, 7, 9} #홀수 집합
mthree = {3, 6, 9} #3의 배수의 집합

def define_set():
    """
    SET 정의 연습
        set() 함수
        {}
    """
    empty = set() # 빈집합
    print(empty, type(empty))
    empty = {} #주의 : 빈 SET가 아니라 빈 사전
    print(empty, type(empty))

    # 순서가 없고, 인덱스도 없고, 슬라이싱 안되고
    # 길이(요소의 수), 포함 여부(in, not in) 정도만 사용
    print(numbers, "LENGTH", len(numbers))
    print("포함여부:", 2 in numbers, 2 in evens, 2 in odds)

    # 캐스팅 : 다른 순차형으로 셋 만들기
    s = "Python Programming" #문자열 안쪽에 모두 몇개의 알파벳이 사용되었는가?
    chars = set(s.upper())
    print(s, chars)

    # 중복 허용 안함 특성
    # list 등의 중복값 제거에 유용
    lst = "Python Programming Java Programming".upper().split()
    print(lst)

    words = set(lst)
    print(words, len(words))

if __name__ == "__main__":
    define_set()

