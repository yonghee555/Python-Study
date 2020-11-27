def reversing_words_slice(word):
    new_word = []
    words = word.split(" ")
    new_word = words[::-1]
    return " ".join(new_word)

if __name__ == "__main__":
    print(reversing_words_slice("파이썬 알고리즘 정말 재미있다"))