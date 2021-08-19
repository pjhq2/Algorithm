import sys
sys.stdin = open('input.txt')


def dfs(graph, now):
    global arrive
    if arrive == 1:  # 찾았으면 남아있는 재귀 멈추기
        return
    if now == 99:
        arrive = 1
    for i in graph[now]:
        dfs(graph, i)


T = 10
for _ in range(T):
    tc, N = map(int, input().split())
    graph = [[] for _ in range(100)]
    temp = list(map(int, input().split()))
    for i in range(0, len(temp), 2):
        graph[temp[i]].append(temp[i+1])

    arrive = 0
    dfs(graph, 0)
    print(f'#{tc} {arrive}')