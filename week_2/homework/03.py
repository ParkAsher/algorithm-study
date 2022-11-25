numbers = [1, 1, 1, 1, 1]
target_number = 3
count = 0

def get_count_of_ways_to_target_by_doing_plus_or_minus(array, curr_idx , curr_sum, target):
    
    # 종료조건
    if curr_idx == len(array) :
        if curr_sum == target:
            global count
            count += 1
        
        return

    get_count_of_ways_to_target_by_doing_plus_or_minus(array, curr_idx + 1, curr_sum + array[curr_idx], target)
    get_count_of_ways_to_target_by_doing_plus_or_minus(array, curr_idx + 1, curr_sum - array[curr_idx], target)
     

get_count_of_ways_to_target_by_doing_plus_or_minus(numbers, 0,0, target_number)
print(count)  # 5를 반환해야 합니다!
