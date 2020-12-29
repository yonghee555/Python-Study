import string


def delete_unique_word(str1):
    table_c = {key: 0 for key in string.ascii_lowercase}
    for i in str1:
        table_c[i] += 1
        
    for key, value in table_c.items:
        if value > 1:
            str1 = str1.replace(key, "")


def test_delete_unique_words():
    str1 = "google"
    assert(delete_unique_word(str1) == "le")
    print('테스트 통과!')


if __name__ == "__main__":
    test_delete_unique_words()
