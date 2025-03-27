# 백준 2178 미로 탐색
# visited의 각 점에서 1일 때만 이동 가능하게 한 후, 다음 점의 거리는 현재의 점의 거리 + 1로 넣음!!
from collections import deque

def bfs():
    while queue:
        x, y = queue.popleft()
        
        # 현재 위치에서 상하좌우 탐색
        for i in range(4):            
            if (1 <= x + dx[i] <= n) and (1 <= y + dy[i] <= m):
                # 다음 이동하는 곳이 (n, m)아면 현재 거리 + 1를 출력하고 반환
                if x + dx[i] == n and y + dy[i] == m:
                    print (visited[x][y] + 1)     # 다음 거리 출력이 아니고, 현재 거리 +1 출력임
                    return
                
                # 방문하지 않으면 방문 처리(다음 거리를 넣음)하고, queue에 추가
                if visited[x + dx[i]][y + dy[i]] == 1 and ((x+dx[i], y+dy[i]) != (1, 1)):
                    visited[x + dx[i]][y + dy[i]] = visited[x][y] + 1 # 방문 처리하면서 다음 점의 거리는 현재의 거리 + 1로 넣기
                    queue.append((x + dx[i], y + dy[i]))
                    


n, m = map(int, input().split())
visited = [[0] * (m+1)] # 0번 인덱스는 0으로 설정
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for _ in range(n):
    # 붙어있는 값들은 list로 바꾸면 각 값들마다 원소로 하여 리스트에 들어감
    # 0열의 값은 움직일 수 없는 칸으로 설정
    visited.append([0] + list(map(int, input())))


queue = deque([(1, 1)])
bfs()
