from itertools import product
from collections import deque

def solution(numbers, target):
    answer = 0
    index = [0, 1]
    index_products = product(index, repeat=len(numbers)) # numbers 개수만큼 0, 1의 중복순열을 모두 구함

    # 하나의 조합을 꺼냄
    for idxs in index_products:
        # numbers의 각 요소를 접근하는데
        # idxs에서 꺼낸 idx가 0이면, numbers의 요소는 양수로
        # idxs에서 꺼낸 idx가 0이면, numbers의 요소는 음수로 new_numbers에 차곡차곡 저장
        new_numbers = [numbers[i] if idx==0 else -numbers[i] for i, idx in enumerate(idxs)]

        # 저장한 new_numbers의 합계가 target과 같으면 answer += 1
        if sum(new_numbers) == target:
            answer += 1
    
    
    return answer