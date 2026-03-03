from math import ceil

# 한쪽 방향으로 쌓을 때 k번 박스까지 한 줄에서의 box 개수
def to_box_in_row(k, w):
    return (k - 1) % w + 1

def solution(n, w, num):
    answer = 0
    rows = ceil(n / w)  
    num_rows = ceil(num / w)
    
    # 맨 윗 줄의 방향이 num이 있는 줄의 방향과 동일
    if rows % 2 == num_rows % 2:
        # num의 위치보다 맨 윗 줄 마지막 박스가 더 측면으로 갔을 때
        if to_box_in_row(n, w) >= to_box_in_row(num, w):
            answer = rows - num_rows + 1
        else:
            answer = rows - num_rows
            
    # 맨 윗 줄의 방향이 num이 있는 줄의 방향과 반대
    else:
        # num의 위치까지 박스 개수와 맨 윗 줄 박스 개수가 한 행의 개수를 넘을 때
        if to_box_in_row(n, w) + to_box_in_row(num, w) > w :
            answer = rows - num_rows + 1
        else:
            answer = rows - num_rows
        
    
    return answer