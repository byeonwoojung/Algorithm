# 프로그래머스 양과 늑대 (매우 어렵다...)
# DFS (이진탐색 가능)
# 방문했던 곳도 다시 방문하면서 모든 경우의 수를 탐색해야 함
# queue.append([node, move_nodes[:i] + move_nodes[i+1:] + node_tree[node], num_sheep, num_wolf + 1]) 이 부분을 기억하자!!


from collections import deque

def dfs():
    nodes, max_sheep = stack.pop()
    for node in nodes:
        if info[node] == 0:
            max_sheep += 1
    node_max_sheep[node] = max_sheep
        
    stack.append(stack)
    
    return 
    

# info : 각 i번째 노드에 양(0) 또는 늑대(1)가 있음(리스트)
# edges : 각 i번째 노드와 연결된 노드가 있음(리스트이고, 단방향으로 되어 있음, 되돌아오는 것은 고민해보자.)
def solution(info, edges):
    answer = 0
    node_tree = {i:[] for i in range(len(info))}

    # 트리모양에 대한 딕셔너리 코드화
    for s, e in edges:
        node_tree[s].append(e)

    # [0번 노드, 연결된 노드들, 양 1마리, 늑대 1마리]를 넣어 초기화
    queue = deque([[0, node_tree[0], 1, 0]])

    while queue:
        new_node, move_nodes, num_sheep, num_wolf = queue.pop() # 스택 형식 -> DFS
        
        # 기존의 양의수보다 현재 경로의 양의 수가 많으면 갱신
        if answer < num_sheep:
            answer = num_sheep
        
        # 현재의 점도 다시 갈 수 있음
        for i, node in enumerate(move_nodes):
            # 늑대가 있다면
            if info[node] == 1:
                # 현재 모아온 양의 수가 다음 늑대의 수(현재 늑대의 수 + 1)보다 크면
                if num_sheep > num_wolf + 1:
                    # 늑대 있는 곳으로 일단 가서 (num_wolf + 1)
                    # 지금 늑대 있는 곳으로 가기 전의 노드에서 그 전에 방문했던 노드들과 다른 연결된 노드들, 지금 양 있는 곳에서 연결된 노드들을 모두 같이 넣어줌
                    queue.append([node, move_nodes[:i] + move_nodes[i+1:] + node_tree[node], num_sheep, num_wolf + 1])
            
            # 양이 있다면 
            else:
                # 양 있는 곳으로 일단 가서 (num_sheep + 1)
                # 지금 양 있는 곳으로 가기 전의 노드에서 그 전에 방문했던 노드들과 다른 연결된 노드들, 지금 양 있는 곳에서 연결된 노드들을 모두 같이 넣어줌
                queue.append([node, move_nodes[:i] + move_nodes[i+1:] + node_tree[node], num_sheep + 1, num_wolf])
    
    return answer