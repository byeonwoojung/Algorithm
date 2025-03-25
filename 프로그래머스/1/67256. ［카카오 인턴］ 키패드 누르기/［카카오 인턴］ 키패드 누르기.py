# 2020 카카오 인턴십 키패드
def d(p, q):
    return abs(p[0] - q[0]) + abs(p[1] - q[1])
    
def solution(numbers, hand):
    answer = ''    
    left_loc = '*'
    right_loc = '#'
    num_loc = dict() # 키패드 위치
    
    for i in range(1, 10):
        num_loc[i] = ((i-1) // 3, (i-1) % 3)
    num_loc['*'] = (3, 0)
    num_loc['#'] = (3, 2)
    num_loc[0] = (3, 1)
    
    
    for num in numbers:
        if num % 3 == 1: # 1,4,7
            answer += 'L'
            left_loc = num
        elif num % 3 == 0 and num != 0: # 3,6,9
            answer += 'R'
            right_loc = num
        elif 0 <= num <= 9 or num=='*' or num=='#': # 2,5,8,0, *,#
            # 거리 같을 때
            if d(num_loc[num], num_loc[left_loc]) == d(num_loc[num], num_loc[right_loc]):
                if hand == 'left':
                    answer += 'L'
                    left_loc = num
                    
                else:
                    answer += 'R'
                    right_loc = num
            
            # 왼손에서의 거리가 더 짧을 때
            elif d(num_loc[num], num_loc[left_loc]) < d(num_loc[num], num_loc[right_loc]):
                answer += 'L'
                left_loc = num
            
            # 오른손에서의 거리가 더 짧을 때
            else:
                answer += 'R'
                right_loc = num
        else:
            pass
    
    return answer