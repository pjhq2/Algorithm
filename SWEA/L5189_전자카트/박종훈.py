# 순열(O(N!)), 외판원 순회(O(2^N)), 백트래킹 가능
import sys
from itertools import permutations
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    area = [list(map(int, input().split())) for _ in range(N)]
    index = list(range(1, N))
    cases = list(permutations(index, N-1))

    result = int(1e9)
    for case in cases:
        start = 0
        total = 0

        i = 0
        while i < len(case) and total < result:
            end = case[i]
            total += area[start][end]
            start = end
            i += 1
        if i == len(case):
            total += area[case[-1]][0]

        if total < result:
            result = total

    print(f'#{tc} {result}')
