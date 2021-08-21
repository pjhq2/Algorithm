import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):

    N = int(input())
    prices = list(map(int, input().split()))

    cnt = 0
    money = 0
    now = prices[-1]
    for i in range(len(prices)-1, 0, -1):
        if now >= prices[i-1]:
            cnt += 1
            money -= prices[i-1]
        else:
            money += now * cnt
            cnt = 0
            now = prices[i-1]
    else:
        if cnt != 0:
            money += now * cnt

    print(f'#{tc} {money}')
