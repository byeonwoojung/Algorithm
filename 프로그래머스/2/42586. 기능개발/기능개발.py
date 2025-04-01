# 프로그래머스 lv2 기능개발
from collections import deque

def solution(progresses, speeds):
    answer = []
    # 배포까지 걸리는 날
    days_queue = deque([(100 - progress - 1)//speeds[i] + 1 for i, progress in enumerate(progresses)])
    
    while days_queue:
        day = days_queue.popleft()
        count = 1
        # 마지막 기능개발 시간이면 answer에 추가하고 끝
        if not days_queue:
            answer.append(count)
            break

        
        # 그 다음 기능개발 시간이 더 적으면 다 배포하고 빼버림
        while day >= days_queue[0]:
            days_queue.popleft()
            count += 1
            # 그 다음 기능개발 시간이 없으면 끝
            if not days_queue:
                break
        
        answer.append(count)
    
    return answer
