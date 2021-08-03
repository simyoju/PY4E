def isPrime(num):
    ans = False
    sumDivisor = 0

    for i in range(2, num):
        if num%i == 0:
            sumDivisor += 1

    if sumDivisor == 0:
        ans = True
    return ans

if __name__ == "__main__":
    prev_num = int(input("첫 번째 수를 입력하세요: "))
    next_num = int(input("두 번째 수를 입력하세요: "))

    if prev_num <= 0 or next_num <= 0:
        print("입력 범위가 잘못되어 종료합니다.")
    else:
        if prev_num > next_num:
         prev_num, next_num = next_num, prev_num
        cnt = 0
        list = [i for i in range(prev_num, next_num+1)]

        for num in list:
            if num != 1 and isPrime(num):
                cnt += 1

        print("범위 내 소수 개수는: ",cnt)