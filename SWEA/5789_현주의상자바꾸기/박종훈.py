import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):

    N, Q = map(int, input().split())
    boxes = [0] * N
    for i in range(1, Q+1):
        start, end = map(int, input().split())
        for j in range(start-1, end):
            boxes[j] = i

    result = ' '.join(map(str, boxes))
    print(f'#{tc} {result}')