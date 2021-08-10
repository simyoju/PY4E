

def count_word(text, word):
    textSaved = open("text.txt", "w", encoding="UTF-8")
    textSaved.write(a)
    textSaved.close()

    fhand = open("text.txt")

    count = 0
    charCombi = ''
    for line in fhand:
        for w in line:
            charCombi = charCombi + w
            print(charCombi)

            if w == '\n' or w == ' ':
                charCombi = ''

            if charCombi == word:
                count += 1

            if len(charCombi) == len(word):
                charCombi = charCombi[1:]

    return count

if __name__ == "__main__":
    a = """
    안녕하세요. 
    반갑습니다.파이썬 공부는 정말 재밌습니다.습니다습니다
    """
    print(count_word(a, "습니"))
