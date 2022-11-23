input = "011110"


def find_count_to_turn_out_to_all_zero_or_all_one(string):
    count_to_all_zero = 0
    count_to_all_one = 0

    current_char = string[0]

    if current_char == '0':
        count_to_all_one += 1
    elif current_char == '1':
        count_to_all_zero += 1

    # 하나씩 돌아가면서 판별
    for char in string :
        
        if current_char != char:
            
            if char == '0':
                count_to_all_one += 1
                current_char = char
            if char == '1':
                count_to_all_zero += 1
                current_char = char

    return min(count_to_all_one, count_to_all_zero)  

result = find_count_to_turn_out_to_all_zero_or_all_one(input)
print(result)