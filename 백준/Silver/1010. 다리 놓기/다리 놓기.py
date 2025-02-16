from math import factorial
case = int(input())

for _ in range(case):
    n, m = map(int, input().split(' '))
    if n <= m:
        print(int(factorial(m) / (factorial(m-n)*factorial(n))))