import sys
sys.stdin = open('input.txt')

# 상하좌우
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def dfs(x, y, visited, number):
    global result
    if x == N-1 and y == N-1 and result > number:
        result = number
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N and not visited[ny][nx] and number+zido[ny][nx] < result:
            visited[ny][nx] = True
            dfs(nx, ny, visited, number+zido[ny][nx])
            visited[ny][nx] = False


T = int(input())
for tc in range(1, T+1):
    s = time()
    N = int(input())
    zido = [list(map(int, input().split())) for _ in range(N)]
    visited = [[False] * N for _ in range(N)]
    result = int(1e9)
    dfs(0, 0, visited, zido[0][0])
    print(f'#{tc} {result}')
