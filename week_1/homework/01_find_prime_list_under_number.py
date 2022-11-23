input = 20


def find_prime_list_under_number(number):

    list = []
    # 2 ~ number까지 반복
    for num in range(2, number):
        isPrime = True      # 소수인지 확인하는 트리거

        # 2는 무조건 소수
        if num == 2 :
            list.append(num)
            continue

        for i in range(2, num):

            # 2부터 자신까지 중에 자신이외의 수로 나누어지면 소수가 아니다
            if num % i == 0:
                isPrime = False     # 소수가 아니면 판별하는 반복문을 빠져나가고 isPrime 을 False로 만든다
                break

        # 위의 판별하는 반복문을 돌고 나와서도 isPrime 이 true이면 리스트에 소수를 넣는다
        if isPrime == True:
            list.append(num);
              
    return list


result = find_prime_list_under_number(input)
print(result)