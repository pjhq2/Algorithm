import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):

    N, K = list(map(int, input().split()))
    matrix = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    
    # 가로
    for row in matrix:
        cnt = 0
        temp = list()
        for i in range(len(row)):
            if row[i] == 1:
                cnt += 1
            else:
                temp.append(cnt)
                cnt = 0
        temp.append(cnt)
        result += temp.count(K)

    # 세로
    for i in range(N):
        cnt = 0
        temp = list()
        for col_idx in range(len(matrix)):
            if matrix[col_idx][i] == 1:
                cnt += 1
            else:
                temp.append(cnt)
                cnt = 0
        temp.append(cnt)
        result += temp.count(K)

    print(f'#{tc} {result}')
