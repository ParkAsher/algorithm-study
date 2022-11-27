s = "(())()"


def is_correct_parenthesis(string):

    stack = []

    for i in range(len(string)) :

        if string[i] == "(":
            stack.append(i)

        elif string[i] == ")":            
            if len(stack) == 0:
                return False
            stack.pop()

    if len(stack) != 0 :
        return False
    else:
        return True
    

print(is_correct_parenthesis(s))  # True 를 반환해야 합니다!