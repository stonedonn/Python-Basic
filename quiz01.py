def q1():
    s ="Life is too short, You need Python"

    s = s.lower()\
            .replace(",", "")\
            .replace(" ","")

    # list로 변환
    lst = list(s)
    # 중복제거 -> set으로 변환
    chars = set(lst)
    print("chars:",chars)
    # -> 리스트로 형변환
    lst = list(chars)
    lst.sort() # 알파벳 순 정렬
    print("lst")
    print(len(lst),"개의 알파벳이 사용되었습니다")

def q2():
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    slice = lst[3:7]
    slice.reverse()
    lst[3:7] = slice

    print(lst)
    print(lst == [1, 2, 3, 7, 6, 5, 4, 8, 9, 10])

def q3():
    students = [
        {
            "name": "Kim",
            "kor": 80,
            "eng": 90,
            "math": 80
        },
        {
            "name": "Lee",
            "kor": 90,
            "eng": 85,
            "math": 85
        }
    ]


    for student in students:
        total = student.get("kor") + student.get("eng") +\
            student.get("math")
        avg = total / 2
        student['total'] = total
        student['average'] = avg

    print(students)
if __name__ == "__main__":
    # q1()
    # q2()
    q3()