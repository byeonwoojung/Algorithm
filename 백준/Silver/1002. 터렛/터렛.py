from math import sqrt

n = int(input())

for _ in range(n):
    x1, y1, r1, x2, y2, r2 = map(int, input().split(' '))
    
    # 원의 중심 간의 거리
    d = sqrt((x1-x2)**2 + (y1-y2)**2)

    # 중심 같을 때
    if x1 == x2 and y1 == y2:
        if r1 == r2:
            print (-1)
            continue
        print (0)
        
    # 중심 다를 때
    else:
        # 내접
        if min(r1, r2) + d == max(r1, r2):
            print (1)

        # 외접
        elif d == r1 + r2:
            print (1)

        # 작은 원이 큰 원 안에 존재 (내접 제외))
        elif d + min(r1, r2) < max(r1, r2):
            print (0)
        
        # 작은 원이 큰 원 밖에 존재 (외접 제외)
        elif r1 + r2 < d:
            print (0)

        # 두 점에서 만날 때 (내접 제외)
        elif r1 + r2 > d:
            print (2)