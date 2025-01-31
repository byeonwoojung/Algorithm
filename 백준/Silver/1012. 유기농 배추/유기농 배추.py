from collections import deque

def bfs(start_x, start_y):
    queue = deque([(start_x, start_y)])
    visited[start_x][start_y] = False

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            if 0 <= x+dx[i] <= m-1 and 0 <= y+dy[i] <= n-1 and visited[x+dx[i]][y+dy[i]] == 1:
                visited[x+dx[i]][y+dy[i]] = 0
                queue.append([x+dx[i], y+dy[i]])


dx = [-1, 1, 0, 0] # 상하좌우 순
dy = [0, 0, -1, 1] # 상하좌우 순

case = int(input())

for _ in range(case):
    m, n, k = map(int, input().split(' '))
    
    visited = [[0] * (n+1) for _ in range(m+1)]

    dots = list()
    for _ in range(k):
        a, b = map(int, input().split(' '))
        visited[a][b] = 1
        dots.append([a, b])
        
    count = 0

    for dot in dots:
        if visited[dot[0]][dot[1]] == 1:
            bfs(dot[0], dot[1])
            count += 1

    print (count)