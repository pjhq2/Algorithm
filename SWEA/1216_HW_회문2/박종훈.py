import sys
sys.stdin = open('input.txt')

T = 10
for _ in range(1, T+1):

    tc = int(input())
    N = 100
    matrix = []
    for x in range(N):
        matrix.append(input())

    result = 1
    # 가로
    for n in range(N):
        # 홀수 판별
        for i in range(N):
            di = 1
            total = 1
            while i+di < N and i-di >= 0:
                if matrix[n][i+di] == matrix[n][i-di]:
                    di += 1
                else:
                    break
            total = 1 + 2 * (di - 1)
            result = max(result, total)
            # 짝수 판별
            if i+1 < N and matrix[n][i] == matrix[n][i+1]:
                di = 1
                total = 2
                while i+1+di < N and i-di >= 0:
                    if matrix[n][i+1+di] == matrix[n][i-di]:
                        di += 1
                    else:
                        break
                total = 2 + 2 * (di - 1)
                result = max(result, total)

    # 세로
    for n in range(N):
        # 홀수 판별
        for i in range(N):
            di = 1
            total = 1
            while i+di < N and i-di >= 0:
                if matrix[i+di][n] == matrix[i-di][n]:
                    di += 1
                else:
                    break
            total = 1 + 2 * (di-1)
            result = max(result, total)
            # 짝수 판별
            if i + 1 < N and matrix[i + 1][n] == matrix[i][n]:
                di = 1
                total = 2
                while i+1+di < N and i-di >= 0:
                    if matrix[i+1+di][n] == matrix[i-di][n]:
                        di += 1
                    else:
                        break
                total = 2 + 2 * (di - 1)
                result = max(result, total)

    print(f'#{tc} {result}')