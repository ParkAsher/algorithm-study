input = [4, 6, 2, 9, 1]

def selection_sort(array):
    
    n = len(array)

    # 총 도는 횟수
    for i in range(n) :

        min_data_index = i     # 최소값 위치를 맨 앞에 숫자의 위치로 초기화        
        for j in range(i, n) :  # 맨 앞부터 끝까지 비교해서 최솟값의 위치찾는 반복문

            if array[j] < array[min_data_index] :
                min_data_index = j 

        array[i], array[min_data_index] = array[min_data_index], array[i]  # 최솟값을 자리에 넣어주기        

    return array


selection_sort(input)
print(input) # [1, 2, 4, 6, 9] 가 되어야 합니다!


print(selection_sort([3,-1,17,9]))