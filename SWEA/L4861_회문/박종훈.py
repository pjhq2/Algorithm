import sys
sys.stdin = open('input.txt')


def func(array, n, m):
    result = []
    for i in range(n):
        for j in range(n-m+1):
            if array[i][j:j+m] in array[i][::-1]:
                result.append(array[i][j:j+m])
    return ''.join(result)


T = int(input())

for tc in range(1, T+1):

    N, M = list(map(int, input().split()))
    matrix = [input() for _ in range(N)]
    result = []
    # 가로
    answer = func(matrix, N, M)
    if len(answer) == M:
        result.append(answer)
    # 세로
    col_matrix = []
    for i in range(N):
        temp = ''
        for j in range(N):
            temp += matrix[j][i]
        col_matrix.append(temp)
    answer = func(col_matrix, N, M)
    if len(answer) == M:
        result.append(answer)

    print('#{} {}'.format(tc, *result))
