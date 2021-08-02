# 백준 14502, 삼성코테 기출
from collections import deque
from itertools import combinations
from copy import deepcopy

N, M = map(int, input().split())
zido = []
result = 0

for i in range(N):
    zido.append(input().split())

walls = list(combinations(range(N*M), 3))

def BFS(y, x, zido_copy, visited):
    # 상하좌우
    dx = (0, 0, -1, 1)
    dy = (-1, 1, 0, 0)
    visited[y][x] = True
    q = deque([[y, x]])
    while q:
        y, x = q.popleft()
        for i in range(4):
            if x + dx[i] >= 0 and y + dy[i] >= 0 and x + dx[i] <= M-1 and y + dy[i] <= N-1 and visited[y+dy[i]][x+dx[i]] == False and zido_copy[y+dy[i]][x+dx[i]] == '0':
                q.append([y+dy[i], x+dx[i]])
                zido_copy[y+dy[i]][x+dx[i]] = '2'
                BFS(y+dy[i], x+dx[i], zido_copy, visited)

for wall in walls: # 벽 만드는 모든 경우에 대하여
    cnt = 0
    visited = [[False for _ in range(M)] for _ in range(N)]
    # 지도에 벽 3개 만들기
    zido_copy = deepcopy(zido)
    wall_cnt = 0
    for i in range(3):
        if zido_copy[wall[i] // M][wall[i] % M] == '0':
            zido_copy[wall[i] // M][wall[i] % M] = '1'
            wall_cnt += 1
    # 벽 3개를 만들지 않는 경우, 건너뛰기
    if wall_cnt != 3:
        continue
    # 만들어진 지도에서 BFS 돌리기
    for m in range(M):
        for n in range(N):
            if zido_copy[n][m] == '2':
                BFS(n, m, zido_copy, visited)
    # BFS 돌린 후 0의 개수 찾기
    for m in range(M):
        for n in range(N):
            if zido_copy[n][m] == '0':
                cnt += 1
    # 저장 및 초기화
    result = max(result, cnt)

print(result)