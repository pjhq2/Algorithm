import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):

    busstops = [0] * 5001

    N = int(input())
    AB = []  # A 이상 B 이하인 정류장을 다님
    for _ in range(N):
        AB.append(map(int, input().split()))
    for a, b in AB:
        for i in range(a, b+1):
            busstops[i] += 1

    P = int(input())
    C = []
    for _ in range(P):
        C.append(int(input()))

    result = []
    for c in C:
        result.append(busstops[c])
    result = ' '.join(map(str, result))
    print(f'#{tc} {result}')
