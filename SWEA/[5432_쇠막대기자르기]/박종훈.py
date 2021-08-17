import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):

    states = input()

    x = 0
    total = 0
    for i in range(len(states)):
        if states[i] == '(':
            x += 1
        else:
            if states[i-1] == '(':  # 레이저
                x -= 1
                total += x
            if states[i-1] == ')':  # 레이저 X
                x -= 1
                total += 1
            print(total, end=' ')

    print(f'#{tc} {total}')
