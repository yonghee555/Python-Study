def reverser(string1, p1=0, p2=None):
    if len(string1) < 2:
        return string1
    p2 = p2 or len(string1) -1
    while p1 < p2:
        string1[p1], string1[p2] = string1[p2], string1[p1]
        p1 += 1
        p2 -= 1

def reversing_words_sentence_logic(string1):
    reverser(string1)
    p = 0
    start = 0
    while(p < len(string1)):
        if string1[p] == " ":
            reverser(string1, start, p-1)
            start = p + 1
        p += 1

    reverser(string1, start, p-1)
    return "".join(string1)


if __name__ == "__main__":
    print(reversing_words_sentence_logic(list("파이썬 정말 재미있다")))