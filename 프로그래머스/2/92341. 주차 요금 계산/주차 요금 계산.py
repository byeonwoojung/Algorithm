from collections import defaultdict, deque


def solution(fees, records):
    answer = []
    parking_time = defaultdict(list)  # 값의 기본 타입을 list로 지정
    sum_time_list = list()
    
    for record in records:
        split_records = list()
        split_records.append(int(record.split(":")[0]))
        split_records += record.split(":")[1].split()

        # 각 차의 입차와 출차 시간을 분으로 계산해서 추가
        # parking_time을 defaultdict로 선언하여 value를 append로 추가 가능
        parking_time[split_records[2]].append(60*split_records[0]+int(split_records[1]))

        # 차 번호로 정렬
        # parking_time을 딕셔너리로 바꿔서 정렬하여 parking_time_dic에 저장
        parking_time_dic = sorted(dict(parking_time).items(), key=lambda x: x[0])

    # 각각의 차마다 계산
    for key, value in parking_time_dic:
        time_list = list()
        queue = deque(value)

        # 각 차마다 time을 하나씩 꺼내어, 순차적으로 In 하는 시간, Out 하는 시간으로 정의
        # 더이상 꺼낼 것이 없을 때는 Out 하는 시간을 23:59(1439분)으로 설정
        while queue:
            in_time = queue.popleft()
            if queue:
                out_time = queue.popleft()
            else:
                out_time = 1439
            time_list.append(out_time - in_time)
        
        sum_time_list.append(sum(time_list))

    # fee 계산
    for sum_time in sum_time_list:
        if sum_time - fees[0] < 0:
            answer.append(fees[1])
            continue

        if (sum_time - fees[0])%fees[2] == 0:
            r = 0
        else:
            r = fees[3]
        answer.append(fees[1] + ((sum_time - fees[0])//fees[2])*fees[3] + r)

    return answer