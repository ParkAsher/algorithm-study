## 요세푸스
## 내 풀이
def josephus_problem2(n, k):
    result_arr = []

    queue = list(range(1, n + 1))

    count = 1
    while queue :

        if (count % k == 0) :
            first = queue.pop(0)
            result_arr.append(first)

        else : 
            first = queue.pop(0)
            queue.append(first)      

        count += 1
                    
    return print("<", ", ".join(map(str, result_arr)), ">", sep='')

josephus_problem2(10, 3)


# 강의 노트 풀이
def josephus_problem(n, k):
    result_arr = []

    next_index = k - 1
    people_arr = list(range(1, n + 1))

    while people_arr:
        result = people_arr.pop(next_index)
        result_arr.append(result)
        if len(people_arr) != 0:
            next_index = (next_index + (k - 1)) % len(people_arr)

    print("<", ", ".join(map(str, result_arr)), ">", sep='')

josephus_problem(10, 3)
