import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):

    N = int(input())
    matrix = [[0] * 10 for _ in range(10)]

    for _ in range(N):
        x1, y1, x2, y2, color = map(int, input().split())
        for i in range(x1, x2+1):
            for j in range(y1, y2+1):
                matrix[j][i] += 1

    cnt = 0
    for i in range(10):
        for j in range(10):
            if matrix[j][i] >= 2:
                cnt += 1

    print(f'#{tc} {cnt}')