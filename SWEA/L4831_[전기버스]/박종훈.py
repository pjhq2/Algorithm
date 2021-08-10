"""
테스트 케이스가 별로 없어서 정답이 아닐 확률이 높습니다 ㅠㅠ

"""

import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):

    K, N, M = map(int, input().split())
    oilstops = list(map(int, input().split()))

    now = 0
    refill = 0
    prev = 0
    passing = False

    for oilstop in oilstops:
        
        if oilstop - now > K and passing == False:  # 갈 수 없는 경우
            refill = 0
            break

        if oilstop - now <= K and passing == False:  # 갈 수 있는 경우 + 첫 번째 oilstop일 때
            passing = True

        if oilstop - now > K and passing == True:  # 갈 수 없는 경우 + 첫 번째 oilstop이 아닐 때

            # 이전 위치에서 refill
            now = prev
            refill += 1
            passing = False

            # 이전 위치에서 refill한 뒤에 현재 oilstop에 대한 평가
            if oilstop - now > K:
                refill = 0
                break
            else:
                passing = True  # 갈 수 있는 경우 + 첫 번째 oilstop이 아닌 경우

                # 도착할 수 있으면 충전하고 골인!
                if oilstop + K >= N:
                    refill += 1
                    break

        prev = oilstop  # 모든 조건문 평가 이후에 현재 위치를 저장

    print(f'#{tc} {refill}')
