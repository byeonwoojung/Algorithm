from collections import deque


def bfs():
    while queue:
        # queue에서 하나 뽑아옴 (각 원소는 위치와 queue에 추가된 날이 들어있음)
        x, y, day = queue.popleft()
        
        # queue가 빌 때까지, queue의 각 원소가 익은 날을 day_set에 계속 업데이트 함
        ripe(x, y, day)

    # 모두 익지 못하는 상황에 -1 출력 (bfs 끝까지 진행했는데도 0이 있는 상황)
    for i, row in enumerate(tomato_map):
        # 해당 row에 0이 하나라도 있으면 -1로 반환
        if 0 in row:
            return -1
    
    return max(day_set)


def ripe(rx, ry, rday):
    # 현재 queue의 원소가 익은 날을 day_set에 저장함
    day_set.add(rday)
    
    for i in range(4):
        if (0 <= rx + dx[i] < m) and (0 <= ry + dy[i] < n):
            # 익지 않은 토마토가 상하좌우에 있을 때
            if tomato_map[rx + dx[i]][ry + dy[i]] == 0:
                # 상하좌우의 토마토가 익음
                tomato_map[rx + dx[i]][ry + dy[i]] = 1

                # 다음 queue의 원소를 다음 날로 설정해 함께 저장
                # rday += 1로 쓰면, 한 원소에 대해 상하좌우를 탐색할 때 같은 rday가 아니게 됨
                queue.append([rx + dx[i], ry + dy[i], rday + 1])



n, m = map(int, input().split())
tomato_map = [list(map(int, input().split())) for _ in range(m)]
queue = deque()
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
day_set = set()

for i in range(m):
    for j in range(n):
        if tomato_map[i][j] == 1:
            queue.append([i, j, 0]) # 초기 1의 위치, 0일차
            day_set.add(0)


print (bfs())
