# Q. 다음과 같은 문자열을 입력받았을 때, 어떤 알파벳이 가장 많이 포함되어 있는지 반환하시오
# 내가 작성한 코드
def find_alphabet_occurrence_array(string):
    alphabet_occurrence_array = [0] * 26

    string_list = list(string)

    for alphabet in string_list:
        if alphabet.isalpha() == False :
            continue

        alphabet_occurrence_array[ ord(alphabet) - ord('a') ] += 1 

    return alphabet_occurrence_array


print(find_alphabet_occurrence_array("hello my name is sparta"))


# 강의 코드
def find_alphabet_occurrence_array2(string):
    alphabet_occurrence_array2 = [0] * 26

    for char in string:
        if not char.isalpha():
            continue

        arr_index = ord(char) - ord('a')
        alphabet_occurrence_array2[arr_index] += 1


    return alphabet_occurrence_array2


print(find_alphabet_occurrence_array2("hello my name is sparta"))