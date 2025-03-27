# 백준 2178 미로 탐색
from collections import deque

def bfs():
    while queue:
        x, y, d = queue.popleft()
        
        # 현재 위치에서 상하좌우 탐색
        for i in range(4):            
            if (1 <= x + dx[i] <= n) and (1 <= y + dy[i] <= m):
                # 다음 이동하는 곳이 (n, m)아면 next_distance를 반환
                if x + dx[i] == n and y + dy[i] == m:
                    return d + 1 # 다음 움직였을 때의 거리이므로 +1
                
                # 방문하지 않으면 방문 처리하고, queue에 추가
                # 다음 거리를 추가
                if visited[x + dx[i]][y + dy[i]] == 1:
                    visited[x + dx[i]][y + dy[i]] = 0 # 방문 처리
                    queue.append((x + dx[i], y + dy[i], d+1))
                    



n, m = map(int, input().split())
visited = [[0] * (m+1)] # 0번 인덱스는 0으로 설정
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for _ in range(n):
    # 붙어있는 값들은 list로 바꾸면 각 값들마다 원소로 하여 리스트에 들어감
    # 0열의 값은 움직일 수 없는 칸으로 설정
    visited.append([0] + list(map(int, input())))
visited
queue = deque([(1, 1, 1)])
print (bfs())
