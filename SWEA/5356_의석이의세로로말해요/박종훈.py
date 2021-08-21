import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):

    matrix = []
    length = 0
    for i in range(5):
        matrix.append(input())
        length = max(length, len(matrix[i]))

    result = ''
    for i in range(length):
        for j in range(5):
            try:
                result += matrix[j][i]
            except:
                continue

    print(f'#{tc} {result}')
