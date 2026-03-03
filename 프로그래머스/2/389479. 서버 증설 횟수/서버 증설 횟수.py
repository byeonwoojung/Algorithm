from collections import deque
import copy

def cal_min_server(player, m):
    return player // m

def solution(players, m, k):
    answer = 0
    
    servers = list()
    for i, player in enumerate(players):
        # 이번에 필요한 최소 서버
        min_server = cal_min_server(player, m)
        
        # 처음일 때
        if len(servers) == 0 and min_server > 0:
            servers.append((1, min_server))
            answer += min_server
            continue
        
        # 이전 것도 없고, 아무 것도 추가할 것 없을 때
        elif len(servers) == 0 and min_server == 0:
            continue
        
        # 업데이트 (시간 지난 서버 버리기)
        new_servers = list()
        recent_server = 0
        for time, server in servers:
            if time < k:
                time += 1
                new_servers.append((time, server))
                recent_server += server
        
        # 이번 시간에 추가 필요한 서버
        need_server = min_server - recent_server
        if need_server > 0:
            new_servers.append((1, need_server))
            answer += need_server
        
        servers = copy.deepcopy(new_servers)
        
    return answer