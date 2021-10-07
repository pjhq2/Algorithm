import sys
sys.stdin = open('input.txt')


def binary_search(array, target):
    global cnt
    if not array:
        return

    l, r = 0, len(array)-1
    check = 0  # 0: 초기 상태, 1: 왼쪽 본 상태, 2: 오른쪽 본 상태
    while l <= r:
        m = (l + r) // 2
        if array[m] == target:
            cnt += 1
            return
        elif array[m] < target:  # 오른쪽
            l = m + 1
            if check == 0 or check == 1:
                check = 2
            else:
                return
        elif array[m] > target:  # 왼쪽
            r = m - 1
            if check == 0 or check == 2:
                check = 1
            else:
                return


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    N_list = sorted(list(map(int, input().split())))
    M_list = list(map(int, input().split()))

    cnt = 0
    for m in M_list:
        binary_search(N_list, m)
    print(f'#{tc} {cnt}')
