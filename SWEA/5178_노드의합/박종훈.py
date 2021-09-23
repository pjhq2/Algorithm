import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    tree = [0] * (N+1)
    for _ in range(M):
        line = list(map(int, input().split()))
        tree[line[0]] = line[1]

    for i in range(N, 0, -1):
        if not tree[i]:  # 값이 없으면
            if i*2+1 <= N:
                tree[i] = tree[i*2] + tree[i*2+1]
            elif i*2 <= N:
                tree[i] = tree[i*2]

    print(f'#{tc} {tree[L]}')
