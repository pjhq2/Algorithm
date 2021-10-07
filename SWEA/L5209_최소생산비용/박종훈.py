import sys
sys.stdin = open('input.txt')

INF = int(1e9)


def work(cost_list, done, cost, k):
    global result

    if result < cost:
        return
    elif k == N:
        result = cost
        return

    for i in range(N):
        if not done[i]:
            temp = cost
            done[i] = 1
            cost += cost_list[k][i]
            work(cost_list, done, cost, k+1)
            done[i] = 0
            cost = temp


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cost_list = [list(map(int, input().split())) for _ in range(N)]
    done = [0] * N
    result = INF
    work(cost_list, done, 0, 0)
    print('#{} {}'.format(tc, result))
