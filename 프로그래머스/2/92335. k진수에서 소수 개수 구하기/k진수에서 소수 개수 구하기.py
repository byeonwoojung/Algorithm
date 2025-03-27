
from math import ceil, sqrt
def solution(n, k):
    answer = -1
    
    # n을 k진수로 나타내기
    n_to_k = ''
    x = n

    # n이 0이면 0으로 반환
    if n == 0:
        return 0
    
    if x < k:
        n_to_k = str(x)
    else:
        while x >= k:
            # 나머지가 0이므로 n_to_k에 넣을 값 없음
            if x == k:
                break
            n_to_k = str(x%k) + n_to_k
            x = x//k
            if x // k == 0:
                n_to_k = str(x) + n_to_k

    if x == 0:
        return 0
    
    # 소수 세기
    count = 0
    
    prime_split = n_to_k.split('0')
    for num in prime_split:
        # 0으로 스플릿할 때 빈문자열 있을 수 있음
        if num == '':
            continue
        
        num = int(num)
        if num == 2 or num == 3 or num == 5 or num == 7:
            count += 1
        elif num >= 11:
            # 루트 num까지 나눠보는데 중간에 나눠지면 소수가 아님
            for i in range(2, ceil(sqrt(num))+1):
                if num % i == 0:
                    break
                # 마지막 순서까지 안 나눠졌으면 소수임
                if i == ceil(sqrt(num)):
                    count += 1
        # num == 1일 때는 pass         
        else:
            pass
    
    answer = count
    
    return answer