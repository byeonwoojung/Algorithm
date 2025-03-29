# 프로그래머스 lv2 조이스틱

from collections import deque

def cal(name_list):
    # 각 i에 대해 오른쪽으로 i칸 이동 후 왼쪽으로 len(name_list)-i칸 이동할 때마다 이동횟수와 알파벳 변환 횟수를 저장함
    # ex. move_list[0]은 0칸 이동 후 왼쪽으로 len(name_list)칸 이동한 것임
    # ex. move_list[2]은 2칸 이동 후 왼쪽으로 len(name_list)-2칸 이동한 것임
    move_list = []
    conver = 0  # 총 알파벳 변환 수
    

    # 이동(move)과 알파벳 변환(conver)을 따로 구할 것임
    # '오른쪽 이동 후 왼쪽 이동'과 '완쪽 이동 후 오른쪽 이동'
    # 입력받은 리스트로 작동하는 방식
    # 오른쪽으로 i칸 이동 후에 왼쪽으로 최대 len(name_list)-i칸 이동 (i는 0~len(alpha_queue)-1까지)
    # 1) 오른쪽 i칸 이동한 후에 왼쪽으로 이동하려는데, i+1부터 끝까지가 모두 A이면 move = i
    # 2) 오른쪽 i칸 이동한 후에 왼쪽으로 이동하려는데, i+1부터 끝까지가 하나라도 A가 아니면
    #    move에 2*i 추가한 후에 i+1부터 끝까지만 따로 리스트(not_move)를 만들어서 왼쪽으로 가기 시작!!
    #    끝에서 왼쪽으로 이동하는 방법은 not_move에서 pop한 후, move에 1을 추가하고, 나머지 not_move가 A만 있는지를 비교하는 것임(이번에 이동 후에 나머지가 A만 있으면 거기서 멈춤)
    for i, alpha in enumerate(name_list): # 칸 이동 계산(i 이용), 각 칸의 알파벳 변환(alpha 이용)
        # 알파벳 이동 횟수
        conver += min((ord(alpha) - ord('A')), ord('Z') - ord(alpha) + 1)
        
        # 그 전까지만 오른쪽으로 이동한 것이 더 이득임
        if i != 0 and alpha == 'A':
            pass

        
        move = 0
        # 아예 모두 A만 있으면 move = 0
        if i == 0:
            if set(name_list) == {'A'}:
                move_list = [0]
                break

        # 끝까지 갔으면
        if i == len(name_list) - 1:
            move_list.append(len(name_list)-1)
            break

        
        
        not_move = deque(name_list[i+1:])

        # 1) 오른쪽 i칸 이동한 후에 왼쪽으로 이동하려는데, i+1부터 끝까지가 모두 A이면 move = i임
        if set(not_move) == {'A'}:
            move = i
        
        # 2) 오른쪽 i칸 이동한 후에 왼쪽으로 이동하려는데, i+1부터 끝까지가 하나라도 A가 아니면
        #    move에 2*i 추가한 후에 i+1부터 끝까지만 따로 리스트(not_move)를 만들어서 왼쪽으로 가기 시작!!
        #    끝에서 왼쪽으로 이동하는 방법은 not_move에서 pop한 후, move에 1을 추가하고, 나머지 not_move가 A만 있는지를 비교하는 것임(이번에 이동 후에 나머지가 A만 있으면 거기서 멈춤)
        else:
            move += (2 * i) # 오른쪽 이동하고 되돌아오는 것 (i*2)를 move에 추가
            # 계속 오른쪽에서 하나씩 뽑아내서 나머지가 A만 남기전 까지 또는 나머지가 없을 때까지 1개씩 늘림
            while set(not_move) != {'A'} and not_move:
                not_move.pop()
                move += 1

        # 각 i마다 i칸 오른쪽 이동 후, 왼쪽으로 최대 len(name_list)-i칸 이동 (i는 0~len(alpha_queue)-1까지)했을 때의 move값을 추가함
        move_list.append(move)


    # 알파벳 변환하는 횟수와 모든 i마다 오른쪽 i칸 움직인 후, 왼쪽으로 움직이는 횟수들의 최솟값을 더해줌
    count = conver + min(move_list)

    return count



def solution(name):
    answer = 0
    nameList = list(name)

    
    
    # 오른쪽 이동부터 시작
    right_first = cal(nameList)
    
    # 왼쪽 이동부터 시작
    # 아예 뒤집은 리스트를 만들자
    queue = deque(nameList)
    q = queue.popleft()
    queue.append(q)
    queue.reverse()
    left_first = cal(list(queue))

    
    answer = min(right_first, left_first)
    
    return answer

