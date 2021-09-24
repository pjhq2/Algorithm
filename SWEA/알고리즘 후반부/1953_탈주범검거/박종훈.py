import sys
sys.stdin = open('input.txt')


# 우하좌상
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
# 터널 구조물 유형
pipe = [
    [0, 0, 0, 0],
    [1, 1, 1, 1],  # 상하좌우
    [0, 1, 0, 1],  # 상하
    [1, 0, 1, 0],  # 좌우
    [1, 0, 0, 1],  # 상우
    [1, 1, 0, 0],  # 하우
    [0, 1, 1, 0],  # 하좌
    [0, 0, 1, 1],  # 상좌
]

T = int(input())
for tc in range(1, T+1):
    N, M, R, C, L = map(int, input().split())
    # 지도 정보
    tunnel = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * M for _ in range(N)]  # 시간 체크 겸 방문 체크

    Q = [(R, C)]
    visited[R][C] = 1

    ans = 0
    while Q:
        r, c = Q.pop(0)
        ans += 1
        if visited[r][c] >= L: continue

        # 4방향 탐색
        for d in range(4):
            curr_p = tunnel[r][c]
            nr = r + dr[d]
            nc = c + dc[d]

            # 다음 좌표가 맵을 벗어났다면 쳐내기
            if nr < 0 or nr >= N or nc < 0 or nc >= M: continue
            # 현재 바라보는 방향으로 길이 없으면 쳐내기
            if pipe[curr_p][d] == 0: continue

            nd = (d+2)%4
            np = tunnel[nr][nc]
            # 방문 했거나 다음 좌표의 파이프가 현재 좌표와 연결되지 않는다면 쳐내기
            if visited[nr][nc] or pipe[np][nd] == 0: continue

            visited[nr][nc] = visited[r][c] + 1
            Q.append((nr, nc))

    print(f'#{tc} {ans}')


# pipe를 다르게 놓고 풀 수 있다.
# dfs로도 풀 수 있다.