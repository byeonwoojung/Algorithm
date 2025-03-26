# 백준 18352
# 탐색, 최단거리 -> BFS
# 방문 순서 중요하지 않은데, 거리가 중요함
from collections import deque
import sys

def bfs():
    while queue:
        p = queue.popleft()

        # 해당 점에서 연결된 점들 하나씩 접근
        for q in graph[p]:
            # 갱신되지 않을 때 실행(방문하지 않을 때)
            if distance_list[q] == -1:
                queue.append(q)
                distance_list[q] = distance_list[p] + 1  # 중요!! 현재 거리 + 1을 넣어줌
                
                # 거리가 k인 점을 result에 추가
                if distance_list[q] == k:
                    result.append(q)
    if not result:
        print (-1)

    else:
        result.sort()
        for i in range(len(result)):
            print (result[i])


input = sys.stdin.readline
n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)] # 0번은 빈 리스트

# distance_list : x에서 해당 노드에 최단거리
# 방문 확인도 distance_list 로 함
# 출발점에서 해당 점에 도착하지 못한다고 초기화
distance_list = [-1] * (n + 1) # 0번 인덱스는 가상
distance_list[x] = 0
queue = deque([x])
result = []

# graph 생성
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

bfs()