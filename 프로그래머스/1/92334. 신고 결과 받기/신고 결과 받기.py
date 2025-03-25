def solution(id_list, report, k):
    answer = []
    sos = dict()
    
    for id in id_list:
        sos[id] = [set(), set(), 0, 0]  # 유저 id : [신고한 id set, 해당 유저 신고한 id set, 신고 당한 횟수, 메일 받은 횟수]

    for report_one in report:
        user_id, sos_id = report_one.split() # [유저 id, 신고한 id]
        sos[user_id][0].add(sos_id)
        sos[sos_id][1].add(user_id)
        sos[sos_id][2] = len(sos[sos_id][1])

    for user_id, sos_list in sos.items():
        if sos_list[2] >= k:
            for u_id in sos_list[1]:
                sos[u_id][3] += 1
    
    answer = [y[3] for x, y in sos.items()]
    
    return answer