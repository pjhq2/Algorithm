import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):

    N = int(input())
    numbers = input()

    # 숫자 개수 계산
    result = [0] * 10
    for number in numbers:
        result[int(number)] += 1
    
    # 출력 결과 계산
    answer = [0, 0]
    for idx, value in enumerate(result):
        if value >= answer[1]:
            answer = [idx, value]

    print(f'#{tc} {answer[0]} {answer[1]}')