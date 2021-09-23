import sys
import heapq
sys.stdin = open('input.txt')


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    tree = []
    for i in map(int, input().split()):
        heapq.heappush(tree, i)

    result = 0
    while N > 1:
        N //= 2
        result += tree[N-1]

    print(f'#{tc} {result}')
