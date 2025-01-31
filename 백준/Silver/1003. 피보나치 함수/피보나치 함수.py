d = [0]*100
d[0] = 1
d[1] = 1
t = int(input())
for _ in range(t):
    n = int(input())
    if n>=2:
        for i in range(2,n+1):
            d[i] = d[i-1] + d[i-2]
        print (d[n-2],d[n-1])
    elif n==1:
        print (0, d[n])
    elif n==0:
        print (d[n],0)