def check_id(id_number):
    gender = ''
    year = int(id_number[:2])
    mon = int(id_number[2:4])
    gender_number = int(id_number[7])

    if id_number[6] != '-' or len(id_number) != 14:
        print('잘못된 번호입니다.')

    if year <= 21:
        chk = input('2000년 이후 출생자입니까? 맞으면 o 아니면 x: ')
        if chk == 'o':
            if gender_number not in [3, 4]:
                print('잘못된 번호입니다.\n올바른 번호를 넣어주세요.\n')
                return 0
            else:
                if gender_number == 3:
                    gender = '남자'
                else:
                    gender = '여자'
        else:
            if gender_number == 1:
                gender = '남자'
            else:
                gender = '여자'
    else:
        if gender_number == 1:
            gender = '남자'
        else:
            gender = '여자'

    return print(f'{year}년{mon}월{gender}')

if __name__ == "__main__":
    while True:
        id_number = input('주민번호를 입력해주세요: (입력을 그만하고 싶으면 q를 눌러주세요.) ')
        if id_number == 'q':
            break
        answer = check_id(id_number)
        if answer == 0:
            continue

        print('\n')