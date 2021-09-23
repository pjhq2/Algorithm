import sys
sys.stdin = open('input.txt')


def solution(n):
    global result
    result += 1
    for i in tree[n]:
        if i:
            solution(i)


T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())
    nodes = list(map(int, input().split()))

    i = 0
    tree = [[0, 0] for _ in range(E+2)]
    while i+1 < len(nodes):
        if tree[nodes[i]][0]:
            tree[nodes[i]][1] = nodes[i+1]
        else:
            tree[nodes[i]][0] = nodes[i+1]
        i += 2

    result = 0
    solution(N)
    print(f'#{tc} {result}')
