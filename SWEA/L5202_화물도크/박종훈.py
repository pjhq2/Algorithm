import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    times = sorted([list(map(int, input().split())) for _ in range(N)], key=lambda x: (x[1], x[0]))

    result = start = 0
    for time in times:
        if time[0] >= start:
            result += 1
            start = time[1]

    print(f'#{tc} {result}')
