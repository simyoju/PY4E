# 📌Q1. 숫자를 입력 받고 그 숫자의 구구단을 출력하는 함수를 만들어 봅시다. 다만 아래의 조건을 만족해 주세요.
# 조건 1: 홀 수 번째만 출력하기
# 조건 2: 값이 50이하인 것만 출력하기

def gugudan(num):
    odd_list = []
    res = 0
    for th in range(1,10):
        res = num*th
        if res <= 50 and th%2:
            odd_list.append(res)
    return odd_list

def printGugudan(dan, list):
    print(dan, "단")
    for i in list:
        print(dan, "X", i//dan, "=", i)

if __name__ == "__main__":
    number = int(input("몇 단을 보여드릴까요? :"))
    printGugudan(number, gugudan(number))
