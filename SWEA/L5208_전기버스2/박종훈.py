import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    charges = list(map(int, input().split()))
    N = charges[0]
    now = 1  # 현재 1번 정류장
    battery_now = charges[now]
    cnt = 0

    # 딱 시작할 때 battery_now 만큼 갈 수 있음
    while now < N:  # 정류장이 N보다 작을 때
        if now + battery_now < N:  # 정류장에서 갈 수 있는 거리가 N보다 작다면 (충전해야겠지)
            # 갈 수 있는 범위에서 한번 충전해야 하는데, 미래 기댓값이 가장 큰 곳에서 충전해야겠지
            charge_now = temp = 0  # 초기값
            save_index = now
            i = 1
            while i <= battery_now:
                if charges[now+i] + i >= temp:
                    charge_now = charges[now+i]
                    temp = charges[now+i] + i
                    save_index = now + i
                i += 1

            now = save_index  # 현재 save_index번 정류장
            battery_now = charge_now  # battery_now에 charge_now 저장
            cnt += 1
        else:
            break

    print(f'#{tc} {cnt}')
