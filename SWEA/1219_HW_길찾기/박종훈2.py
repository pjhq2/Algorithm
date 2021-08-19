import sys
sys.stdin = open('input.txt')

T = 10
for _ in range(T):
    tc, N = map(int, input().split())
    graph = [[] for _ in range(100)]
    temp = list(map(int, input().split()))
    for i in range(0, len(temp), 2):
        graph[temp[i]].append(temp[i + 1])

    arrive = 0
    visited = [False] * 100
    stack = [0]

    while stack and arrive == 0:
        now = stack.pop()
        visited[now] = True
        for i in graph[now]:
            if visited[i] == False:
                if i == 99:
                    arrive = 1
                    break
                stack.append(i)

    print(f'#{tc} {arrive}')
