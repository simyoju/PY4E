import random

if __name__ == "__main__":
    numbers = []
    visited = []
    count = 1

    for _ in range(3):
        numbers.append(random.randint(0, 100))

    while True:
        print(count, "차 시")
        print(numbers)

        predictionNumber = int(input("숫자를 예측해주세요: "))


        if predictionNumber in numbers:
            print("숫자를 맞추셨습니다!")
            if predictionNumber == min(numbers):
                print(predictionNumber, "는 최솟값입니다")
            elif predictionNumber == max(numbers):
                print(predictionNumber, "는 최대값입니다.")
            else:
                print(predictionNumber, "는 중간값입니다.")
            print("게임 종")
            break
        else:
            if count%5 == 0:
                print(predictionNumber,"는 없습니다.")
                if predictionNumber in visited:
                    print("이미 예측에 사용한 숫자입니다.")
                elif predictionNumber < min(numbers):
                    print("최솟값은 ", predictionNumber,"보다 작습니다.")
                elif predictionNumber > max(numbers):
                    print("최댓값은 ", predictionNumber, "보다 크니다.")

        count += 1
        visited.append(predictionNumber)