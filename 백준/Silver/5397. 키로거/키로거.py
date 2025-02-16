n = int(input())

for i in range(n):
    test_case = input()
    left_stack = []
    right_stack = []

    for chr in test_case:
        if chr not in '-<>':
            left_stack.append(chr)
        elif chr == '-' and left_stack:
            left_stack.pop()
        elif chr == '<' and left_stack:
            right_stack.append(left_stack.pop())
        elif chr == '>' and right_stack:
            left_stack.append(right_stack.pop())
            
    print(''.join(left_stack + right_stack[::-1]))
