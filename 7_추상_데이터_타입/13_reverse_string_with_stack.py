from stack import Stack

def reverse_string_with_stack(str1):
    s = Stack()
    revStr = ''

    for c in str1:
        s.push(c)

    for _ in range(s.size()):
        revStr += s.pop()

    return revStr

if __name__ == "__main__":
    str1 = "Hello!"
    print(str1)
    print(reverse_string_with_stack(str1))