input = "hello my name is sparta"

# 내가 작성한 코드
def find_max_occurred_alphabet(string):
    
    alphabet_array = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    alphabet_count_list = [0] * 26

    for char in string :

        if not char.isalpha():
            continue

        idx = ord(char) - ord('a')

        alphabet_count_list[idx] += 1

    for num in alphabet_count_list :
        for compare_num in alphabet_count_list :

            if num < compare_num:
                break
        
        else:
            max = num

    alphabet_array_index = alphabet_count_list.index(max)

    return alphabet_array[alphabet_array_index]


result = find_max_occurred_alphabet(input)
print(result)


###################################################################################################################################
# 강의 코드
input2 = "hello my name is sparta"


def find_max_occurred_alphabet2(string):
    alphabet_array2 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

    max_occurrence = 0
    max_alphabet = alphabet_array2[0]

    for alphabet in alphabet_array2:
        occurence = 0
        for char in string:
            if char == alphabet:
                occurence += 1

        if occurence > max_occurrence:
            max_occurrence = occurence
            max_alphabet = alphabet

    return max_alphabet


result = find_max_occurred_alphabet2(input2)
print(result)

#####################################################################################################################################
# 강의 코드 2
input3 = "hello my name is sparta"


def find_max_occurred_alphabet3(string):
    alphabet_occurrence_array = [0] * 26

    for char in string :

        if not char.isalpha():
            continue

        idx = ord(char) - ord('a')

        alphabet_occurrence_array[idx] += 1

    max_occurence = 0
    max_alphabet_index = 0
    for index in range(len(alphabet_occurrence_array)) :

        # 빈도수 배열에서 해당하는 index 의 빈도수를 꺼내옴
        alphabet_occurrence = alphabet_occurrence_array[index]

        # 만약 그 빈도수가 max 빈도수보다 크다면, 
        # max에 그 빈도수를 넣고
        # max index 에 그 index를 넣어라
        if alphabet_occurrence > max_occurence :
            max_occurence = alphabet_occurrence
            max_alphabet_index = index

    # 아스키코드로 변환 -> 문자로 변환
    return chr(max_alphabet_index + ord('a')) 

result = find_max_occurred_alphabet3(input)
print(result)