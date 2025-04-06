# 프로그래머스 lv2 피로도

from itertools import permutations

def solution(k, dungeons):
    answer = -1
    
    n = len(dungeons)
    index = [i for i in range(n)]
    index_perms = permutations(index, n)
    count_list = []
    
    # 던전 탐험 순서 조합마다
    for index_perm in index_perms:
        new_k = k    # 던전 탐험 순서 조합마다 현재 피로도 세팅
        count = 0    # 던전 탐험 순서 조합마다 탐험 가능 횟수 count 세팅
        
        for i in index_perm:
            if new_k >= dungeons[i][0]:      # 현재 피로도가 최소 필요 피로도 이상이면 (당연히 소모 피로도보다도 많을 것)
                count += 1                   # 던전 탐험 고고
                new_k = new_k - dungeons[i][1] # 피로도 업데이트
        count_list.append(count)
    
    answer = max(count_list)
    return answer
