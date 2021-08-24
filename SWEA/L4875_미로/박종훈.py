import sys
sys.stdin = open('input.txt')

dx = (0, 0, -1, 1)
dy = (-1, 1, 0, 0)


def go(y, x):
    global result
    if miro[y][x] == '3':
        result = 1
        return
    if result == 0:
        visited[y][x] = True
        for i in range(4):
            if 0 <= y+dy[i] < N and 0 <= x+dx[i] < N and visited[y+dy[i]][x+dx[i]] == False and miro[y+dy[i]][x+dx[i]] != '1':
                go(y+dy[i], x+dx[i])


T = int(input())

for tc in range(1, T+1):
    result = 0
    N = int(input())
    visited = [[False] * N for _ in range(N)]
    miro = [input() for _ in range(N)]
    # 시작점 찾기
    for i in range(N):
        for j in range(N):
            if miro[i][j] == '2':
                start = (i, j)
    # DFS
    go(start[0], start[1])

    print(f'#{tc} {result}')
