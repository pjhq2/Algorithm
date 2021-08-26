import sys
from collections import deque
sys.stdin = open('input.txt')

def bfs(v, visited):
    queue = deque([v])
    visited[v] = 0
    while queue:
        now = queue.popleft()
        for i in graph[now]:
            if i == G:
                return visited[now] + 1
            if visited[i] > visited[now]:
                queue.append(i)
                visited[i] = visited[now] + 1
    return 0


T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]
    for i in range(E):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    S, G = map(int, input().split())
    INF = int(1e9)
    visited = [INF] * (V+1)

    print('#{} {}'.format(tc, bfs(S, visited)))
