if __name__ == "__main__":
    prev_num = int(input("첫 번째 수를 입력하세요: "))
    next_num = int(input("두 번째 수를 입력하세요: "))

    middle_value = int((prev_num+next_num)/2)
    # 1, 2, 3, 4, 5

    for i in range(prev_num, next_num+1):
        if i%2 == 0:
            if i == middle_value:
                print(i, "중앙값")
            print(i,"짝수")


