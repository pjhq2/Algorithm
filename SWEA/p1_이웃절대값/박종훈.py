import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):

    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    # 상하좌우
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    total = 0
    for i in range(N):
        for j in range(N):
            for k in range(4):
                if 0 <= i+dx[k] < N and 0 <= j+dy[k] < N:
                    total += abs(matrix[i][j] - matrix[i+dx[k]][j+dy[k]])

    print(f'#{tc} {total}')