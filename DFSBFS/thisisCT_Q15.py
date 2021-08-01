# 백준 18352번
from collections import deque
import sys

N, M, K, X = map(int, sys.stdin.readline().split())
array = [[] for _ in range(N+1)]

for _ in range(M):
    A, B = map(int, sys.stdin.readline().split())
    array[A].append(B)

min_length = [-1 for _ in range(N + 1)]
min_length[X] = 0

order = deque([X])
while order:
    now = order.popleft()
    for next_node in array[now]:
        if min_length[next_node] == -1:
            min_length[next_node] = min_length[now] + 1
            order.append(next_node)

valid = False
for idx, l in enumerate(min_length):
    if l == K:
        print(idx)
        valid = True
if not valid:
    print(-1)