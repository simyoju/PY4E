#print(f"{1000:,}")

# num = int(input("숫자를 입력해주세요:"))
# print(f"{num:,}")


def make_comma(num):
    frontNum = num[:-3]
    backNum = ',' + num[-3:]

    if len(frontNum)>3:
        frontNum = make_comma(frontNum)
    return frontNum+backNum


if __name__ == "__main__":
    numForDef = input("숫자를 입력해주세요:")
    print(make_comma(numForDef))