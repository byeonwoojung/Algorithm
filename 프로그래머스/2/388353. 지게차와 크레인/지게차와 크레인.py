from collections import deque

def jige(queue, request, container, visited, container_rows, container_cols, removed, x, y):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < container_rows and 0 <= ny < container_cols:
            # 아직 방문하지 않은 request이면 -> 방문 처리, 빈 칸 처리, 제거된 것 추가 (큐 추가 X)
            if container[nx][ny] == request and visited[nx][ny] == False:
                if (nx, ny) not in removed:
                    visited[nx][ny] = True
                    container[nx][ny] = '.'
                    removed.add((nx, ny))
            
            # 외부 또는 제거된 칸인데 아직 방문 안 했으면(이전 단계에서 제거됐던 것) -> 방문 처리, 큐 추가
            elif container[nx][ny] == '.' and visited[nx][ny] == False:
                visited[nx][ny] = True
                queue.append((nx, ny))

    return queue, removed, visited, container


def crane(container, removed, request, container_rows, container_cols):
    for x in range(1, container_rows - 1):
        for y in range(1, container_cols - 1):
            if container[x][y] == request[0]:
                removed.add((x, y))
                container[x][y] = '.'
    return removed, container


def solution(storage, requests):
    answer = 0
    rows_num = len(storage)
    cols_num = len(storage[0])
    container = [['.'] * (cols_num + 2) for _ in range(rows_num + 2)]
    
    # 외부 패딩 추가(문자 '.' 넣음)
    for i in range(0, rows_num):
        for j in range(0, cols_num):
            container[i+1][j+1] = storage[i][j]
    
    # 각 문자마다 jige([0, 0] 부터 bfs)와 crane 분기
    removed = set()
    for request in requests:
        req_len = len(request)
        
        if req_len == 1:
            queue = deque([(0, 0)])
            visited = [[False] * (cols_num + 2) for _ in range(rows_num + 2)]
            visited[0][0] = True
            
            while queue:
                x, y = queue.popleft()
                queue, removed, visited, container = jige(queue, request, container, visited, rows_num + 2, cols_num + 2, removed, x, y)  
            
        elif req_len == 2:
            removed, container = crane(container, removed, request, rows_num + 2, cols_num + 2)

    # 남은 컨테이너 수 = 전체 - 제거된 수
    answer = rows_num * cols_num - len(removed)
    return answer