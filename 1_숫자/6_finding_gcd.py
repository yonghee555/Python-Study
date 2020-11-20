def finding_gcd(a, b):
    while(b != 0):
        result = b
        a, b = b, a % b
    return result

def testing_find_gcd():
    num1, num2 = 21, 12
    assert(finding_gcd(num1, num2) == 3)
    print("테스트 통과!")

if __name__ == "__main__":
    testing_find_gcd()