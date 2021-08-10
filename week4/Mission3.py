
def wrong_guest_book(guest_book):
    makingTxt = open("mission3.txt", "w", encoding="UTF-8")
    makingTxt.write(guest_book)
    makingTxt.close()

    fhand = open("mission3.txt")
    answer = []
    for line in fhand:
        line = line.split(',')

        name = line[0].strip()
        call_number = line[1].rstrip()
        
        if call_number[:3] != '010':
            answer.append('잘못 쓴 사람: ' + name + '\n' +'잘못 쓴 번호: ' + call_number)
        elif '-' not in call_number:
            answer.append('잘못 쓴 사람: ' + name + '\n' + '잘못 쓴 번호: ' + call_number)
        elif len(call_number) != 13:
            answer.append('잘못 쓴 사람: ' + name + '\n' + '잘못 쓴 번호: ' + call_number)

    return answer


if __name__ == "__main__":
    guest_book = """김갑,123456789
    이을,010-1234-5678
    박병,010-5678-111
    최정,111-1111-1111
    정무,010-3333-3333"""

    answer = wrong_guest_book(guest_book)

    for a in answer:
        print(a)

