import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):

    Forth = list(input().split())

    stack = []
    for x in Forth:
        if x.isnumeric():
            stack.append(int(x))
        elif x != '.':
            if len(stack) < 2:  # 예외 처리
                result = 'error'
                break
            b = stack.pop()
            a = stack.pop()
            if x == '+':
                stack.append(a+b)
            elif x == '-':
                stack.append(a-b)
            elif x == '*':
                stack.append(a*b)
            elif x == '/':
                if b == 0:  # 예외 처리
                    result = 'error'
                    break
                stack.append(a//b)
        elif x == '.':
            if len(stack) != 1:  # 예외 처리
                result = 'error'
                break
            result = stack.pop()

    print(f'#{tc} {result}')
