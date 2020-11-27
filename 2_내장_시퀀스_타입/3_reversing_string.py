def revert(s):
    if s:
        s = s[-1] + revert(s[:-1])
    return s

def revert2(string):
    return string[::-1]

if __name__ == "__main__":
    str = "안녕 세상!"
    print(revert(str))
    print(revert2(str))