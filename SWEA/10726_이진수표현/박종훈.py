import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    M = bin(M)[2:]
    result = 'OFF'
    if M[len(M)-N:] == '1' * N:
        result = 'ON'
    print(f'#{tc} {result}')