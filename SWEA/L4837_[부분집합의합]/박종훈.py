import sys
sys.stdin = open('input.txt')

T = int(input())
A = set(range(1, 13))  # {1, 2, 3, 4, 5}


def combinations2(A: set, n: int) -> list:  # 예시: 5C3

    A_list = list(A)  # [1, 2, 3, 4, 5]
    noe = len(A)  # number_of_elements == 5

    result = []
    for i in range(2 ** noe):  # 가능한 subset 경우의 수
        number = bin(i)[2:]  # (ex. i == 11 == '0b1011' -> '1011')
        while len(number) < noe:  # (ex. '1011' -> '01011') -> 아래의 idx 연산을 위해서 len(number)을 고정시키기 위함
            number = '0' + number

        temp = list()  # subset 임시 저장용 변수
        for idx in range(len(number)):  # idx는 0 ~ 4
            if number[idx] == '1':
                temp.append(A_list[idx])

        if len(temp) == n:
            result.append(temp)

    return result


def subset_K(A: set, n: int, k: int) -> bool:
    subsets = combinations2(A, n)  # subset list
    cnt = 0
    for subset in subsets:
        if sum(subset) == k:
            cnt += 1
    return cnt


for tc in range(1, T+1):

    N, K = map(int, input().split())
    answer = subset_K(A, N, K)

    print(f'#{tc} {answer}')
