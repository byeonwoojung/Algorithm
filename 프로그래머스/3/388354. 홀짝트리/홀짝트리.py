from collections import defaultdict, deque

def tree(graph, related_nodes):
    odd_even_check = 0
    reversed_odd_even_check = 0
    for node in related_nodes:
        # 홀수/짝수 노드인 개수
        if (node % 2) == (len(graph[node]) % 2):
            odd_even_check += 1
        # 역홀수/역짝수 노드인 개수
        elif (node % 2) == ((len(graph[node]) - 1) % 2):
            reversed_odd_even_check += 1
    
    # '홀짝 트리'는 루트(홀짝 일치)가 딱 1개여야 함
    # 나머지는 역홀짝이어야 실제 간선 1개 뺐을 때 홀짝이 됨
    odd_even = 0
    if odd_even_check == 1:
        odd_even += 1

    # '역홀짝 트리'는 역루트(홀짝 불일치)가 딱 1개여야 함
    # 나머지는 홀짝이어야 실제 간선 1개 뺐을 때 역홀짝이 됨
    reversed_odd_even = 0
    if reversed_odd_even_check == 1:
        reversed_odd_even += 1
    
    return odd_even, reversed_odd_even

# 한 트리의 노드들을 모음
def bfs(node, graph, visited):
    related_nodes = set()
    queue = deque([node])
    visited[node] = True
    
    while queue:
        q = queue.popleft()
        for related in graph[q]:
            if visited[related] == False:
                related_nodes.add(related)
                queue.append(related)
                visited[related] = True
                    
    return related_nodes, visited


def solution(nodes, edges):
    graph = defaultdict(list)
    visited = defaultdict(bool)
    answer = []
    
    for node in nodes:
        graph[node] = []
        visited[node] = False
    for edge in edges:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])
    
    related_nodes_list = []
    odd_even_count, reversed_odd_even_count = 0, 0
    # 각 노드마다
    for node in nodes:
        # 아직 방문하지 않은 노드이면(트리에 들어가지 않은 노드)
        if visited[node] == False:
            # 한 트리의 노드들
            related_nodes, visited = bfs(node, graph, visited)
            related_nodes.add(node)
        
            odd_even, reversed_odd_even = tree(graph, related_nodes)
            odd_even_count += odd_even
            reversed_odd_even_count += reversed_odd_even
            
    answer = [odd_even_count, reversed_odd_even_count]
    
    return answer