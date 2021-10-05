import sys
sys.stdin = open('input.txt')

# 아래쪽, 오른쪽
dx = [0, 1]
dy = [1, 0]

INF = int(1e9)


def dfs(x, y, visited):
    if x == N-1 and y == N-1:
        return

    for i in range(2):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N and visited[y][x] + zido[ny][nx] < visited[ny][nx]:
            visited[ny][nx] = visited[y][x] + zido[ny][nx]
            dfs(nx, ny, visited)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    zido = [list(map(int, input().split())) for _ in range(N)]
    visited = [[INF] * N for _ in range(N)]

    visited[0][0] = zido[0][0]
    dfs(0, 0, visited)

    print(f'#{tc} {visited[N-1][N-1]}')
