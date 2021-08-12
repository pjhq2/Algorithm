import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):

    N = int(input())
    numbers = list(map(int, input().split()))
    
    # 버블 정렬
    for i in range(N-2, -1, -1):
        for j in range(0, i+1):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

    result = ' '.join(map(str, numbers))
    print(f'#{tc} {result}')