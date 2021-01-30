from stack import Stack

def dec2bin_with_stack(num_dec):
    s = Stack()
    num_bin = ""

    while num_dec > 0:
        s.push(num_dec % 2)
        num_dec = num_dec // 2

    while not s.isEmpty():
        num_bin += str(s.pop())

    return num_bin

if __name__ == "__main__":
    print(dec2bin_with_stack(9))