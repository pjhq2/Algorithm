import sys
sys.stdin = open('input.txt')

# 상하좌우
dx = (0, 0, -1, 1)
dy = (-1, 1, 0, 0)


def dfs(miro, x, y, visited):
    global result
    visited[y][x] = True
    for i in range(4):
        if 0 <= x+dx[i] < N and 0 <= y+dy[i] < N and visited[y+dy[i]][x+dx[i]] == False and miro[y+dy[i]][x+dx[i]] != '1':
            if miro[y+dy[i]][x+dx[i]] == '3':
                result = 1
                return
            dfs(miro, x+dx[i], y+dy[i], visited)


T = 10
for _ in range(1, T+1):
    tc = int(input())
    N = 16
    miro = [input() for _ in range(N)]
    start = (1, 1)
    visited = [[False] * N for _ in range(N)]

    result = 0
    dfs(miro, start[0], start[1], visited)

    print('#{} {}'.format(tc, result))
