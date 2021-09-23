import sys
sys.stdin = open('input.txt')


def in_order(n):
    global num
    if n <= N:
        in_order(2*n)
        tree[n] = num
        num += 1
        in_order(2*n+1)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    tree = [0] * (N+1)
    num = 1
    in_order(1)
    print(f'#{tc} {tree[1]} {tree[N//2]}')
