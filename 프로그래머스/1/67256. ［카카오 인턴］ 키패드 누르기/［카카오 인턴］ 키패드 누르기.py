def d(card1, card2):
    return abs(card1[0] - card2[0]) + abs(card1[1] - card2[1])
    
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
        if num % 3 == 1:
            answer += 'L'
            left_loc = num
        elif num % 3 == 0 and num != 0:
            answer += 'R'
            right_loc = num
        elif 0 <= num <= 9 or num=='*' or num=='#':
            if d(num_loc[num], num_loc[left_loc]) == d(num_loc[num], num_loc[right_loc]):
                if hand == 'left':
                    answer += 'L'
                    left_loc = num
                    
                else:
                    answer += 'R'
                    right_loc = num
            elif d(num_loc[num], num_loc[left_loc]) < d(num_loc[num], num_loc[right_loc]):
                answer += 'L'
                left_loc = num
            else:
                answer += 'R'
                right_loc = num
        else:
            pass
    
    return answer