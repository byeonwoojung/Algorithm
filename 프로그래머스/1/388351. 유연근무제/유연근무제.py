def check(time_h, time_m, sche_h, sche_m):
    if time_h * 60 + time_m <= sche_h * 60 + sche_m + 10:
        return True
    return False

def solution(schedules, timelogs, startday):
    answer = 0
    
    for sche, timelog in zip(schedules, timelogs):
        today = startday
        sche_h, sche_m = sche // 100, sche % 100

        ok = True
        for time in timelog:
            time_h, time_m = time // 100, time % 100
            
            if (today - 1) % 7 + 1 in [6, 7]:
                today += 1
                continue
                
            ok = check(time_h, time_m, sche_h, sche_m)
            if ok == False:
                break
            
            today += 1

        if ok == True:
            answer += 1
    
    return answer