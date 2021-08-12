import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):

    N, M = list(map(int, input().split()))
    matrix = [list(map(int, input().split())) for _ in range(N)]

    total = 0
    for i in range(0, N-M+1):
        for j in range(0, N-M+1):
            temp = 0
            for y in range(M):
                for x in range(M):
                    temp += matrix[j+x][i+y]
            total = max(total, temp)

    print(f'#{tc} {total}')