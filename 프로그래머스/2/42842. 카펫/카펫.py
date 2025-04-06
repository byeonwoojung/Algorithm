def solution(brown, yellow):
    # yellow의 가로, 세로 길이 찾기
    for i in range(1, int(yellow**0.5)+1):
        # i가 yellow의 약수일 때만
        if int(yellow/i) * i == yellow:
            m = max(int(yellow/i), i)
            n = min(int(yellow/i), i)
            
            # 카펫의 조건이 만족할 경우
            if m + n == brown/2 -2:
                return [m+2, n+2]

