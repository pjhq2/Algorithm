import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):

    N = int(input())
    numbers = list(map(int, input().split()))

    max_number = 0
    min_number = 1000001
    for number in numbers:
        if number > max_number:
            max_number = number
        if number < min_number:
            min_number = number

    result = max_number - min_number
    print(f'{tc} {result}')