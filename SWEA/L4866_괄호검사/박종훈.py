import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    chars = input()
    stack = []
    result = 1
    for char in chars:
        if char == '(' or char == '{':
            stack.append(char)

        if char == ')':
            try:
                x = stack.pop()
                if x != '(':
                    raise ValueError
            except:
                result = 0
                break
        elif char == '}':
            try:
                x = stack.pop()
                if x != '{':
                    raise ValueError
            except:
                result = 0
                break

    if len(stack) != 0:
        result = 0

    print(f'#{tc} {result}')
