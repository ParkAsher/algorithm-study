finding_target = 14
finding_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]


def is_existing_target_number_binary(target, array):
    current_min = 0
    current_max = len(array-1)

    # 중간 index
    current_guess = (current_min + current_max) // 2

    while current_min <= current_max:

        if array[current_guess] == target :
            ## 시도한 값이 타겟이라면 (찾았다면)
            return True

        elif array[current_guess] < target :
            # 시도한 값이 타겟보다 작다면 타겟은 위쪽 범위에 있다.
            current_min = current_guess + 1     # 최솟값을 시도값 다음 값으로

        else :
            # 시도한 값이 타겟보다 크다면 타겟은 아래 범위에 있다.
            current_max = current_guess - 1     # 최대값을 시도값 앞의 값으로

        # 중간 index 재설정
        current_guess = (current_min + current_max) // 2

    return False


result = is_existing_target_number_binary(finding_target, finding_numbers)
print(result)