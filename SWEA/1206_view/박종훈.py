import sys
sys.stdin = open('input.txt')

# T = int(input())
T = 10


def view_count(buildings):
    cnt = 0
    for i in range(2, len(buildings)-2):  # 3번째 빌딩부터 마지막-2 빌딩까지
        for building_height in range(buildings[i], 0, -1):  # 빌딩 높이에서 -1씩 하면서
            view = True
            for k in [i-2, i-1, i+1, i+2]:  # 주변 건물이 전부 더 낮으면 view == True
                if building_height <= buildings[k]:
                    view = False
                    break
            if view == True:  # view == True일 때 cnt += 1
                cnt += 1
            elif view == False:  # view == False라면 나가기
                break
    return cnt


for tc in range(1, T+1):
    building_length = int(input())
    buildings = list(map(int, input().split()))

    result = view_count(buildings)
    print(f'#{tc} {result}')
