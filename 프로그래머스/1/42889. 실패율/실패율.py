def solution(N, stages):
    answer = []
    fail = [0] * (N+1)      # 각 스테이지의 fail
    fail_acc = [0] * N  # 현재 스테이지까지의 fail 누적합
    fail_per = [[i, 0] for i in range(1, N+1)] # [스테이지 번호, 0]
    
    
    for stage in stages:
        if stage <= N:
            fail[stage-1] += 1
    
    for i in range(N):
        for j in range(i): # 현재 스테이지까지
            fail_acc[i] += fail[j]
        # 실패 누적합 == stages의 길이 == 총 인원수
        if fail_acc[i] == len(stages):
            fail_per[i][1] = 0
        else:
            if i == 0:
                fail_per[i][1] = fail[i] / len(stages)
            else:
                fail_per[i][1] = fail[i] / (len(stages)-fail_acc[i])
        
    print (fail_per)
    for i, j in sorted(fail_per, key=lambda x: (-x[1], x[0])):
        answer.append(i)
    
    return answer