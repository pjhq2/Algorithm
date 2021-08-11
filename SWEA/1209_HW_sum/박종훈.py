import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):

    matrix = []
    for _ in range(100):
        matrix.append(list(map(int, input().split())))

    total = 0
    # 가로 합
    for i in range(100):
        total = max(total, sum(matrix[i]))
    # 세로 합
    for i in range(100):
        temp = 0
        for j in range(100):
            temp += matrix[j][i]
        total = max(total, temp)
    # 대각 합
    temp1 = temp2 = 0
    for i in range(100):
        temp1 += matrix[i][i]
        temp2 += matrix[99-i][i]
    total = max(total, temp1, temp2)

    print(f'#{tc} {total}')