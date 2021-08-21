import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):

    N = int(input())
    matrix = [list(input().split()) for _ in range(N)]

    m_90 = []
    m_180 = []
    m_270 = []
    for j in range(N):
        temp_90 = ''
        temp_180 = ''
        temp_270 = ''
        for i in range(N):
            temp_90 += matrix[N-1-i][j]
            temp_180 += matrix[N-1-j][N-1-i]
            temp_270 += matrix[i][N-1-j]
        m_90.append(temp_90)
        m_180.append(temp_180)
        m_270.append(temp_270)

    print(f'#{tc}')
    for n in range(N):
        print(m_90[n], m_180[n], m_270[n])
