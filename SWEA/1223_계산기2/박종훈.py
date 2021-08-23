import sys
sys.stdin = open('input.txt')

T = 10

for tc in range(1, T+1):
    N = int(input())
    sik = list(input().split('+'))

    total = 0
    for i in sik:
        if len(i) == 1:
            total += int(i)
        elif len(i) > 1:
            temp = 1
            for j in i:
                if j != '*':
                    temp *= int(j)
            total += temp

    print(f'#{tc} {total}')
