import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):

    N = int(input())
    matrix = [[0] * N for _ in range(N)]
    cnt = 0
    dir = 0
    x = -1
    y = 0

    for num in range(1, N**2 + 1):

        if dir == 0:  # 오른쪽 방향
            if 0 <= x + 1 < N and matrix[y][x + 1] == 0:
                x += 1
            else:
                dir = (dir + 1) % 4
        if dir == 1:  # 아래 방향
            if 0 <= y + 1 < N and matrix[y + 1][x] == 0:
                y += 1
            else:
                dir = (dir + 1) % 4
        if dir == 2:  # 왼쪽 방향
            if 0 <= x - 1 < N and matrix[y][x - 1] == 0:
                x -= 1
            else:
                dir = (dir + 1) % 4
        if dir == 3:  # 위 방향
            if 0 <= y - 1 < N and matrix[y - 1][x] == 0:
                y -= 1
            else:
                dir = (dir + 1) % 4
                if 0 <= x + 1 < N and matrix[y][x + 1] == 0:  # 순환 구조
                    x += 1

        matrix[y][x] = num  # 숫자 저장

    print(f'#{tc}')
    for i in range(N):
        print(*matrix[i])