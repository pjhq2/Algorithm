import sys
sys.stdin = open('input.txt')


def in_order(n):
    global result
    if left[n]:
        in_order(left[n])
    result += alphabet[n]
    if right[n]:
        in_order(right[n])


T = 10
for tc in range(1, T+1):
    N = int(input())
    alphabet = [0] * (N+1)
    left = [0] * (N+1)
    right = [0] * (N+1)

    for _ in range(1, N+1):
        line = input().split()
        if len(line) >= 2:
            alphabet[int(line[0])] = line[1]
        if len(line) >= 3:
            left[int(line[0])] = int(line[2])
        if len(line) >= 4:
            right[int(line[0])] = int(line[3])

    result = ''
    in_order(1)
    print(f'#{tc} {result}')
