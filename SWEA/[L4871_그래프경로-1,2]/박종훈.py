import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]
    for _ in range(E):
        a, b = map(int, input().split())
        graph[a].append(b)
    start, end = map(int, input().split())

    stack = [start]
    visited = [False] * (V+1)
    arrive = 0
    while stack and arrive == 0:
        now = stack.pop()
        visited[now] = True
        for i in graph[now]:
            if visited[i] == False:
                if i == end:
                    arrive = 1
                    break
                stack.append(i)

    print(f'#{tc} {arrive}')
