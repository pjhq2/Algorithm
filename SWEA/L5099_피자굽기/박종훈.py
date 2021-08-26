import sys
sys.stdin = open('input.txt')


def baking_pizza(pizza, oven, N, M):
    # 아직 오븐에 넣지 못한 피자들 집어넣기 까지의 과정
    cnt = N
    n = 0
    while cnt < M:
        oven[n][0] //= 2
        if oven[n][0] == 0:
            oven[n] = pizza[cnt]
            cnt += 1
        n = (n + 1) % N
    # 오븐에서 최종 피자가 남을 때까지의 과정
    cnt = N
    complete = [False] * N
    while cnt > 1:
        if complete[n] == False:
            if oven[n][0] != 0:
                oven[n][0] //= 2
            if oven[n][0] == 0:
                complete[n] = True
                cnt -= 1
        n = (n + 1) % N
    # 최종 피자 찾기
    for find_pizza in oven:
        if find_pizza[0] != 0:
            return find_pizza[1]



T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    pizza_temp = list(map(int, input().split()))
    pizza = []
    for i in range(len(pizza_temp)):
        pizza.append([pizza_temp[i], i+1])  # [치즈의 양, 피자 번호]
    oven = [pizza[i] for i in range(N)]

    final_pizza = baking_pizza(pizza, oven, N, M)
    print(f'#{tc} {final_pizza}')
