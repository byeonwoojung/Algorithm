from collections import deque

# queue에 빨간 공 위치, 파란 공 위치, 현재 카운트를 함께 저장해야 함
# 현재 위치까지의 현재 카운트를 저장해놔야 카운트 안 섞임

def bfs(queue, board):
    
    while queue:
        rx, ry, bx, by, count = queue.popleft()
        if count > 10:
            break
        
        for i in range(4):
            # new_rx 등을 이용해야 원래 rx 등에 덮어 씌워지지 않음
            new_rx, new_ry, r_m_cnt = move(rx, ry, dx[i], dy[i])
            new_bx, new_by, b_m_cnt = move(bx, by, dx[i], dy[i])

            # 파란 공이 홀로 들어가는 것은 제외하고, 다른 벙향으로 움직인 것 찾으러 감
            # 큐에도 추가하지 않음
            if board[new_bx][new_by] == 'O':
                continue

            # 빨간 공이 홀에 빠지면 현재까지 기울인 횟수 반환
            if board[new_rx][new_ry] == 'O':
                return count

            
            # 빨간 공과 파란 공 한쪽으로 움직였는데 위치가 서로 같을 때, 더 움직인 공의 위치를 한 칸 되돌려줘야 함
            if new_rx == new_bx and new_ry == new_by:
                if r_m_cnt > b_m_cnt:
                    new_rx -= dx[i]
                    new_ry -= dy[i]
                else:
                    new_bx -= dx[i]
                    new_by -= dy[i]

            # 방문한 곳은 다시 방문하지 않기 위해 작성
            if (new_rx, new_ry, new_bx, new_by) not in visited:
                visited.add((new_rx, new_ry, new_bx, new_by))
                queue.append([new_rx, new_ry, new_bx, new_by, count + 1])
    
    return -1


    
# 빨간 공, 파란 공 중력에 의해 한쪽으로 끝까지 이동하는 함수
# m_count : 중력에 의해 한쪽 방향으로 움직인 횟수
def move(x, y, mx, my):
    m_count = 0
    # 어느 공이 벽에 부딪히거나, 홀에 빠지기 전까지 반복
    while board[x + mx][y + my] != '#':
        x += mx
        y += my
        m_count += 1
        # 변환된 x와 y에서 홀이면 그대로 반환
        if board[x][y] == 'O':
            return x, y, m_count
        

    
    # 끝까지 이동했을 때 위치와 한쪽 방향으로 움직인 횟수 반환
    # 빨간 공과 파란 공 한쪽으로 움직였을 때 위치가 서로 같으면 더 움직인 공의 위치를 한 칸 되돌려줘야 함
    return x, y, m_count



m, n = map(int, input().split())
board = [list(input().strip()) for _ in range(m)]
queue = deque()
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


for i, row in enumerate(board):
    if 'R' in row:
        rx, ry = i, row.index('R')
    if 'B' in row:
        bx, by = i, row.index('B')

count = 1
queue.append([rx, ry, bx, by, count])
visited = set((rx, ry, bx, by))

result = bfs(queue, board)
print (result)