import sys
sys.stdin = open('input.txt')

# T = int(input())
T = 10

for _ in range(1, T + 1):

    tc = int(input())

    # 기본값 설정
    N = 100
    data = [list(map(int, input().split())) for _ in range(N)]
    # 도착점의 좌표 (col, row) 설정
    for idx in range(len(data[N - 1])):
        if data[N - 1][idx] == 2:
            row = idx
    col = N - 1

    while col >= 1:

        left = False

        # 유효 범위 and 왼쪽이 1일 때
        while 0 <= row - 1 < N and data[col][row - 1] == 1:
            row -= 1
            left = True

        # 왼쪽으로 이동한 적이 없다면
        if left == False:
            # 유효 범위 and 오른쪽이 1일 때
            while 0 <= row + 1 < N and data[col][row + 1] == 1:
                row += 1

        col -= 1  # 이동을 마치면 위쪽으로 한 칸 이동

    print(f'#{tc} {row}')