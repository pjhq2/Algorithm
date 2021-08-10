import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):

    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))

    max_number = 0
    min_number = 10000 * M + 1
    for i in range(N-M+1):
        if max_number < sum(numbers[i:i+M]):
            max_number = sum(numbers[i:i+M])
        if min_number > sum(numbers[i:i+M]):
            min_number = sum(numbers[i:i+M])

    result = max_number - min_number

    print(f'{tc} {result}')