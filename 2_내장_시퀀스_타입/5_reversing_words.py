def reversing_words_brute(string):
    word, sentence = [], []
    for character in string:
        if character != " ":
            word.append(character)
        else:
            if word:
                sentence.append("".join(word))
            word = []

    if word != "":
        sentence.append("".join(word))
    sentence.reverse()
    return " ".join(sentence)

if __name__ == "__main__":
    print(reversing_words_brute("네이버 가고 싶다"))
