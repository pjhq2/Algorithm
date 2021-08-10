import sys
sys.stdin = open('input.txt')

# T = int(input())
T = 10

for tc in range(1, T+1):

    dump = int(input())
    boxes = list(map(int, input().split()))
    min_height, max_height = 101, 0

    # 상자 max_height 정하기
    for i in range(max(boxes)-1, min(boxes)-1, -1):
        cnt = 0
        for box in boxes:
            if box > i:  # 기준 높이보다 box 높이가 더 높다면 그 차이만큼 cnt에 더하기
                cnt += box - i
        if cnt > dump:  # 상자가 남을 경우
            max_height = i + 1
            break
        elif cnt == dump:  # 딱 맞아 떨어질 경우
            max_height = i
            break

    # 상자 min_height 정하기
    for i in range(min(boxes), max(boxes)+1):
        cnt = 0
        for box in boxes:
            if i > box:  # 기준 높이보다 box 높이가 더 낮다면 그 차이만큼 cnt에 더하기
                cnt += i - box
        if dump < cnt:  # 빈 공간이 남을 경우
            min_height = i - 1
            break
        elif dump == cnt:  # 딱 맞아 떨어질 경우
            min_height = i
            break

    result = max_height - min_height
    print(f'#{tc} {result}')
