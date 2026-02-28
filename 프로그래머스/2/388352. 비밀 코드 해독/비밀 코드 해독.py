from itertools import combinations

def solution(n, q, ans):
    answer = 0
    nums = [i for i in range(1, n+1)]
    candidates = combinations(nums, 5)
        
    # 1~n까지 5개를 뽑은 모든 조합 롤링
    for candidate in candidates:
        ok = True
        
        # 각 candidate마다 모든 q에 대해 원소 겹치는 개수가 ans 개수와 다르면 통과 X
        for _q, _ans in zip(q, ans):
            if len(set(candidate) & set(_q)) != _ans:
                ok = False
                break
        
        # 해당 candidate가 통과이면
        if ok == True:
            answer += 1  
    
    return answer