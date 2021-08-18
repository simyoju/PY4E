import random

if __name__ == "__main__":
    numbers = []
    count = 0
    winLoseCheck = False

    while len(numbers) < 31:
        myTurn = input("숫자를 입력하세요: ")
        winLoseCheck = True

        if len(myTurn.split()) > 3:
            print("숫자는 3개까지만 입력이 가능합니다. 다시 입력해주세요!")
            continue
        elif len(myTurn) == 1:
            numbers.append(myTurn)
        else:
            numbers += myTurn.split()
        print("마이 턴: ", myTurn)

        computerNumOfTimes = random.randint(1, 3)

        for i in range(computerNumOfTimes):
            computerTurn = int(numbers[-1])+1
            print("컴퓨터 턴: ", computerTurn)
            numbers.append(computerTurn)
            if computerTurn >= 31:
                break

        winLoseCheck = False

    if winLoseCheck:
        print("나의 패배")
    else:
        print("컴퓨터의 패")
