import sys
sys.stdin = open('input.txt')

# 상하좌우
dx = (0, 0, -1, 1)
dy = (-1, 1, 0, 0)


def bfs(miro, x, y, visited):
    global result
    queue = [(x, y)]
    visited[y][x] = 0

    while queue:
        x, y = queue.pop(0)
        for i in range(4):
            if 0 <= x+dx[i] < N and 0 <= y+dy[i] < N and miro[y+dy[i]][x+dx[i]] != '1' and visited[y+dy[i]][x+dx[i]] == -1:
                if miro[y+dy[i]][x+dx[i]] == '3':
                    result = visited[y][x]
                    return
                visited[y+dy[i]][x+dx[i]] = visited[y][x] + 1
                queue.append((x+dx[i], y+dy[i]))



T = int(input())

for tc in range(1, T+1):
    N = int(input())
    miro = [input() for _ in range(N)]

    for i in range(N):
        if '2' in miro[i]:
            y, x = (i, miro[i].index('2'))
            break

    result = 0
    visited = [[-1] * N for _ in range(N)]
    bfs(miro, x, y, visited)
    print(f'#{tc} {result}')
