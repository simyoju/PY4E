# ๐Q1. ์ซ์๋ฅผ ์๋ ฅ ๋ฐ๊ณ  ๊ทธ ์ซ์์ ๊ตฌ๊ตฌ๋จ์ ์ถ๋ ฅํ๋ ํจ์๋ฅผ ๋ง๋ค์ด ๋ด์๋ค. ๋ค๋ง ์๋์ ์กฐ๊ฑด์ ๋ง์กฑํด ์ฃผ์ธ์.
# ์กฐ๊ฑด 1: ํ ์ ๋ฒ์งธ๋ง ์ถ๋ ฅํ๊ธฐ
# ์กฐ๊ฑด 2: ๊ฐ์ด 50์ดํ์ธ ๊ฒ๋ง ์ถ๋ ฅํ๊ธฐ

def gugudan(num):
    odd_list = []
    res = 0
    for th in range(1,10):
        res = num*th
        if res <= 50 and th%2:
            odd_list.append(res)
    return odd_list

def printGugudan(dan, list):
    print(dan, "๋จ")
    for i in list:
        print(dan, "X", i//dan, "=", i)

if __name__ == "__main__":
    number = int(input("๋ช ๋จ์ ๋ณด์ฌ๋๋ฆด๊น์? :"))
    printGugudan(number, gugudan(number))
