import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = float(input())
    result = ''
    for i in range(-1, -13, -1):
        if N >= 2**i:
            N -= 2**i
            result += '1'
        else:
            result += '0'
        if N == 0:
            break
    else:
        result = 'overflow'

    print(f'#{tc} {result}')