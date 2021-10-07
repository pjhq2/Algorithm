import sys
sys.stdin = open('input.txt')


def work(P_ij, done, percent, k):
    global result

    if result >= percent:
        return
    elif k == N:
        result = percent
        return

    for i in range(N):
        if not done[i]:
            temp = percent
            done[i] = 1
            percent *= P_ij[k][i]/100
            work(P_ij, done, percent, k+1)
            done[i] = 0
            percent = temp


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    P_ij = [list(map(int, input().split())) for _ in range(N)]
    done = [0] * N
    result = 0
    work(P_ij, done, 1, 0)
    answer = round((100 * result), 6)
    print('#{} {:.6f}'.format(tc, answer))
