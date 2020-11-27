def reversing_words(str1):
    words = str1.split(" ")
    rev_set = " ".join(reversed(words))
    return rev_set

def reversing_words2(str1):
    words = str1.split(" ")
    words.reverse()
    return " ".join(words)

if __name__ == "__main__":
    str1 = "파이썬 알고리즘 정말 재미있다"
    print(reversing_words(str1))
    print(reversing_words2(str1))