import random

def rockPaperScissors(me):
    computer = random.randint(0, 2)
    res = me - computer
    res_string = ""

    if me == 0:
        if res == -2:
            res_string = "승리"
        elif res == -1:
            res_string = "패"
        else:
            res_string = "무승부"
    elif me == 1:
        if res == 1:
            res_string = "승리"
        elif res == -1:
            res_string = "패"
        else:
            res_string = "무승부"
    else:
        if res == 1:
            res_string = "승리"
        elif res == 2:
            res_string = "패"
        else:
            res_string = "무승부"

    return res_string

rsp_dic = {"가위": 0,
           "바위": 1,
           "보": 2,
           "0" : 0,
           "1" : 1,
           "2" : 2
           }

if __name__ == "__main__":
    win, lose, same, cnt = 0,0,0,0
    games = int(input("몇 판을 진행하시겠습니까?: "))

    while games > 0:
        me = input("가위 바위 보: ")
        if me in rsp_dic:
            num = rsp_dic[me]
            games -= 1
            cnt += 1
        else:
            print("다시 입력해주세요")
            continue

        res = rockPaperScissors(num)

        if res == "승리":
            win += 1
        elif res == "패":
            lose += 1
        else:
            same += 1

        print(cnt, "번째 판 나의", res)
        print(win,"승", same,"무", lose,"패")

    print("게임이 끝났습니다. ")