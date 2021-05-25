def q1():
    score1 = int(input("점수1:"))
    score2 = int(input("점수2:"))

    average = (score1 + score2) / 2

    if score1 >= 50 and \
        score2 >= 50 and \
        average >= 60:
        message = "합격"
    else:
        message = "불합격"

    print(message)


def q2():
    for dan in range(2, 10):    # 2 ~ 9 단
        print(dan, "단")
        for num in range(1, 10):    # 1 ~ 9
            print("{} x {} = {}".format(dan, num, dan * num))


def q3():
    balance = 0 # 잔액 변수

    while True: # 무한루프
        method = input("method:")
        method = method.lower()

        if method == "q":
            break   # 루프 종료

        if method != "d" and method != "w":
            print("?")
            continue

        # d, w만 남음
        # 금액 입력
        amount = int(input("Amount:"))

        # if method == "d":   # 입금
        #     balance += amount
        # else:   # 출금
        #     balance -= amount
        balance += amount if method == "d" else -amount

        print("Balance:", balance)

    print("프로그램 종료")


if __name__ == "__main__":
    # q1()
    # q2()
    q3()