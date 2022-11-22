# Q. 다음과 같이 숫자로 이루어진 배열이 있을 때, 이 배열 내에서 가장 큰 수를 반환하시오.
input = [3, 5, 6, 1, 2, 4]

# 방법1
def find_max_num(array):
    for num in array:

        for compare_num in array:

            if num < compare_num:
                break;

        else:
            return num

result = find_max_num(input)
print(result)

