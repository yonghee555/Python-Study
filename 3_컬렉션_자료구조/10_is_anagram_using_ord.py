import string


def hash_func(astring):
    s = 0
    for one in astring:
        if one in string.whitespace:
            continue
        s = s + ord(one)
    return s


def find_anagram_hash_function(word1, word2):
    return hash_func(word1) == hash_func(word2)


def test_find_anagrem_hash_function():
    word1 = "buffy"
    word2 = "byffu"
    word3 = "bffya"
    assert(find_anagram_hash_function(word1, word2) == True)
    assert(find_anagram_hash_function(word1, word3) == False)
    print("테스트 통과!")


if __name__ == "__main__":
    test_find_anagrem_hash_function()
