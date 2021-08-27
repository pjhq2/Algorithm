import sys
sys.stdin = open('input.txt')

T = 10

# 1: N극, 2: S극, 위에 N극  있고 아래에 S극 있다.
for tc in range(1, T+1):
    N = int(input())
    temp = [list(map(int, input().split())) for _ in range(N)]

    # 전치행렬로 변환, 왼쪽이 N극 오른쪽이 S극
    table = list(zip(*temp))
    table_2 = [[] for _ in range(N)]

    # table에서 0 빼기
    for i in range(N):
        for j in range(N):
            if table[i][j] != 0:
                table_2[i].append(table[i][j])
    # 계산
    total = 0
    for i in range(N):
        check = False
        for magnetic in table_2[i]:
            if magnetic == 1:
                check = True
            if check == True and magnetic == 2:
                total += 1
                check = False

    print(f'#{tc} {total}')
