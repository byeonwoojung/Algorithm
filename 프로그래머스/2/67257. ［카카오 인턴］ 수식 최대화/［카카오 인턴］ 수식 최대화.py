import re
from itertools import permutations

def cal(ex_split, op):
    print(ex_split, op)
    while op in ex_split:
        if op == "+":
            left = ex_split[:ex_split.index('+')-1]
            right = ex_split[ex_split.index('+')+2:]
            mid = int(ex_split[ex_split.index('+')-1]) + int(ex_split[ex_split.index('+')+1])
            ex_split = left + [mid] + right
            temp = []
            for ex_split_element in ex_split:
                if str(ex_split_element) != '':
                    temp.append(ex_split_element)
        elif op == '-':
            left = ex_split[:ex_split.index('-')-1]
            right = ex_split[ex_split.index('-')+2:]
            mid = int(ex_split[ex_split.index('-')-1]) - int(ex_split[ex_split.index('-')+1])
            ex_split = left + [mid] + right
            temp = []
            for ex_split_element in ex_split:
                if str(ex_split_element) != '':
                    temp.append(ex_split_element)
        elif op == '*':
            left = ex_split[:ex_split.index('*')-1]
            right = ex_split[ex_split.index('*')+2:]
            mid = int(ex_split[ex_split.index('*')-1]) * int(ex_split[ex_split.index('*')+1])
            ex_split = left + [mid] + right
            temp = []
            for ex_split_element in ex_split:
                if str(ex_split_element) != '':
                    temp.append(ex_split_element)
    
    return ex_split



def solution(expression):
    answer = 0
    ops_permutations = permutations(['+', '*', '-'], 3)
    results = set()
    
    
    for ops in ops_permutations:
        ex_split = re.split(r"(\D+)", expression)
        while any(re.search(r"[+\-*]\-", item) for item in ex_split):
            if '*-' in ex_split:
                ex_split[ex_split.index('*-')+1] = ex_split[ex_split.index('*-')][1] + ex_split[ex_split.index('*-')+1]
                ex_split[ex_split.index('*-')] = ex_split[ex_split.index('*-')][0]
            if '--' in ex_split:
                ex_split[ex_split.index('--')+1] = ex_split[ex_split.index('--')][1] + ex_split[ex_split.index('--')+1]
                ex_split[ex_split.index('--')] = ex_split[ex_split.index('--')][0]
            if '+-' in ex_split:
                ex_split[ex_split.index('+-')+1] = ex_split[ex_split.index('+-')][1] + ex_split[ex_split.index('+-')+1]
                ex_split[ex_split.index('+-')] = ex_split[ex_split.index('+-')][0]
        for op in ops:
            ex_split = cal(ex_split, op)
            print (ex_split)
        results.add(abs(int(ex_split[0])))

    return max(results)