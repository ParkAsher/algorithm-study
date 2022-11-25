input = "abcba"


def is_palindrome(string):

    n = len(string)

    # 0 ~ n-1
    for idx in range(n) :
        if string[idx] != string[n-1 -idx] :
            return False

    return True


print(is_palindrome(input))