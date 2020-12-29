from collections import Counter


def is_anagram(s1, s2):
    counter = Counter()
    for c in s1:
        counter[c] += 1
    for c in s2:
        counter[c] -= 1
    for i in counter.values():
        if i:
            return False
    return True


def test_is_anagram():
    assert(is_anagram("marina", "aniram") is True)
    assert(is_anagram("google", "gouglo") is False)
    print("테스트 통과!")


if __name__ == "__main__":
    test_is_anagram()
