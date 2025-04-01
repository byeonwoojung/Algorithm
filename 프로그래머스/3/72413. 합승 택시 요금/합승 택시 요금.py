# 2021 카카오 블라인드 합승 택시 요금

# n: 도시수, s: 출발지점
# a와 b : A와 B의 집 번호(도착 지점)
# fares: 지점 사이의 예상 택시요금 ([c지점, d지점, 예상 택시 요금]들을 모은 2차원 형태)
# -> (c지점 => d지점)의 예상 택시 요금과 (d지점 => c지점)의 예상 택시 요금을 따로 저장해야 함

import heapq

INF = float('inf')

# 현재 start 지점에서 end 지점까지의 최단 거리
def dijk(start, n, graph):
    fare = [INF for _ in range(n + 1)]
    fare[start] = 0      # 현재 출발점에서 이동 안 했으니까 예상 요금 0임
    
    queue = []
    heapq.heappush(queue, (0, start))

    while queue:
        dist, now = heapq.heappop(queue)

        if fare[now] < dist:
            continue

        for node, now_fare in graph[now]:
            cost = dist + now_fare
            if cost < fare[node]:
                fare[node] = cost
                heapq.heappush(queue, (cost, node))
    
    return fare  # 현재 출발점으로부터 각 노드별 예상 요금들 저장한 것 반환 (가상의 점 포함)



def solution(n, s, a, b, fares):
    answer = 0

    graph = [[] for _ in range(n + 1)] # 0번은 가상 지점
    for node1, node2, fare  in fares:
        graph[node1].append((node2, fare)) # 출발 도시 : (도착지점, 예상 요금)
        graph[node2].append((node1, fare)) # 출발 도시 : (도착지점, 예상 요금)

    # 출발점으로부터 각 노드에 대한 최소 요금 (함께 타고 갈 때)
    # fare_together은 모든 노드에 대한 최소 요금들이 다 저장되어 있음
    fare_together = dijk(s, n, graph)
    print(fare_together)

    # 각 노드에서 출발하여 A의 집까지의 최소 요금 (A 혼자 갈 때)
    # 각 노드에서 출발하여 B의 집까지의 최소 요금 (B 혼자 갈 때)
    fare_A = [INF] * (n + 1)
    fare_B = [INF] * (n + 1)
    for start in range(1, n+1):
        fare_from_start = dijk(start, n, graph)
        fare_A[start] = fare_from_start[a] # i지점에서 A까지의 최소 요금
        fare_B[start] = fare_from_start[b] # i지점에서 B까지의 최소 요금

    print (fare_A)
    print (fare_B)
    # 각 지점까지 최소 요금으로 함께 타고 가고, 그 지점 각 집까지 갈 때의 최소 요금을 모두 합한 것들에 대한 최솟값
    min_now = INF
    for i in range(1, n+1):
        if fare_together[i] != INF and fare_A[i] != INF and fare_B[i] != INF:
            min_now = min(min_now, fare_together[i] + fare_A[i] + fare_B[i])
    
    answer = min_now
    return answer
