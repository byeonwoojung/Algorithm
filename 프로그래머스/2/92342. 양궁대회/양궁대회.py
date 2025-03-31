# 카카오 2022 블라인드 채용 양궁 대회

from itertools import combinations_with_replacement as combis_rep

def solution(n, info):
    answer = []

    combis = list(combis_rep([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], n))


    max_combis = []
    max_dif = 0
    
    for combi in combis:
        ryan = [0] * 11
        for num in combi:
            ryan[10 - num] += 1

        # print (ryan)

        score_dif = 0
        
        for i in range(11):
            # 둘 다 0개씩 맞추면 아무도 점수를 가져가지 않음
            if ryan[i] == 0 and info[i] == 0:
                continue
            
            dif = ryan[i] - info[i]
            if dif > 0:
                # i점을 가져감
                score_dif += (10-i)
            else:
                score_dif -= (10-i)

        # max보다 더 큰 score_dif이면 갱신(최대인 조합도 갱신)
        if max_dif < score_dif:
            # 현재의 조합을 넣음
            max_dif = score_dif # max 갱신
            max_combis = [ryan] # 현재의 combi가 아닌 ryan을 넣어야 함

        # max와 같은 score_dif이면 최대인 조합에 추가함
        # score_dif > 0 : 비기는 경우는 추가하지 않음
        elif max_dif == score_dif and score_dif > 0:
            max_combis.append(ryan)
    

    # 이길 수 있는 방법이 없을 때
    if max_combis == []:
        return [-1]

    # sorted 중요!!
    # x[i]가 일단 0보다 커야 함!! (맞춰야 하니까)
    # x[10] 0점 맞춘 것은 제외
    # 정렬 기준은 x[9], ... , x[0]을 순차적으로
    answer = sorted(max_combis, key = lambda x: tuple(x[i] for i in range(9, -1, -1) if x[i] > 0))
    
    return answer[0]
