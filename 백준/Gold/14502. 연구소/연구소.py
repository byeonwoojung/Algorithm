from collections import deque
from itertools import combinations
import copy

# 모든 조합의 벽 세우기
def wall(empty_count):
    walls_combi = list(combinations(empty_loc, 3))
    
    for walls in walls_combi:
        new_lab = copy.deepcopy(lab)
        new_queue = deque(queue) # 새로운 큐 생성
        new_lab[walls[0][0]][walls[0][1]] = 1
        new_lab[walls[1][0]][walls[1][1]] = 1
        new_lab[walls[2][0]][walls[2][1]] = 1
        
        # 벽 세운 후의 lab에서 bfs 실행하여 빈 칸 개수를 set에 추가
        empty_count.add(bfs_empty_count(new_lab, walls, new_queue))

    # 빈 칸(0)인 곳의 개수들 중의 최댓값 반환
    return max(empty_count)

def bfs_empty_count(nlab, walls, nqueue):    
    while nqueue:
        x, y = nqueue.popleft()
        for i in range(4):
            # 0일 때, 2로 바꾸고 큐에 추가
            if (0 <= x + dx[i] < m) and (0 <= y + dy[i] < n) and nlab[x + dx[i]][y + dy[i]] == 0:
                nlab[x + dx[i]][y + dy[i]] = 2
                nqueue.append([x + dx[i], y + dy[i]])

    # 빈 칸(0)인 곳의 개수
    n_empty_count = sum(row.count(0) for row in nlab)
    
    return n_empty_count


m, n = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(m)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
queue = deque()
empty_loc = list()
empty_count = set()


for i in range(m):
    for j in range(n):
        if lab[i][j] == 2:
            queue.append([i, j])
        if lab[i][j] == 0:
            empty_loc.append((i, j))
        

print (wall(empty_count))