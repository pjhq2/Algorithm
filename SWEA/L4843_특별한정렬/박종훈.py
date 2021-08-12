import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):

    N = int(input())

    numbers = sorted(map(int, input().split()), reverse=True)
    idx = len(numbers) // 2

    result = []
    for i in range(idx):
        result.append(numbers[i])
        result.append(numbers[len(numbers)-1-i])
    if len(numbers) % 2:
        result.append(numbers[len(numbers) // 2])

    answer = ' '.join(map(str, result))

    print(f'#{tc} {answer}')