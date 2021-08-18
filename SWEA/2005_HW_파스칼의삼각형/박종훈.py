import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    result = [[0, 1, 0]]
    for i in range(1, N):
        temp = [0]
        for j in range(len(result[i-1])-1):
            temp.append(result[i-1][j] + result[i-1][j+1])
        temp.append(0)
        result.append(temp)

    print(f'#{tc}')
    for i in range(N):
        print(' '.join(map(str, result[i][1:-1])))
