# 프로그래머스 lv2 주식가격
def solution(prices):
    answer = []

    # 각 price마다 위치(i)도 같이 가져옴
    for i, price in enumerate(prices):
        # 마지막 위치에서는 0을 추가하고 종료
        if i == len(prices) - 1:
            answer.append(0)
            break
        
        # 각 price에서 그 이후부터 확인
        for j in range(i+1, len(prices)):
            # 중간에 자신의 price 보다 더 작아지면 앞으로 더 걸린 시간 만큼 저장함
            if price > prices[j]:
                answer.append(j-i)
                break
            
            # 끝까지 가면
            if j == len(prices)-1:
                answer.append(j-i)

    
    return answer
