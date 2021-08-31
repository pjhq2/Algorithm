import sys
from itertools import combinations
sys.stdin = open('input.txt')

T = int(input())


def solution(cases, start, end, result):
    global answer

    if len(start) > 2:
        for case in cases:
            temp_start = start[:]  # start 백트래킹
            temp_end = end[:]  # end 백트래킹
            temp_end.extend(case)
            temp_start.remove(case[0])
            temp_start.remove(case[1])
            temp_start.append(min(temp_end))
            temp = result
            result += max(case) + min(temp_end)
            temp_end.remove(min(temp_end))
            temp_cases = list(combinations(temp_start, 2))  # cases 백트래킹
            if result < answer:
                solution(temp_cases, temp_start, temp_end, result)
            result = temp  # result 백트래킹
    elif len(start) == 2:
        result += max(start[0], start[1])
        answer = min(answer, result)


for tc in range(1, T+1):
    N = int(input())
    start = list(map(int, input().split()))
    end = []
    if N > 1:
        cases = list(combinations(start, 2))
        result = 0
        answer = int(1e9)
        solution(cases, start, end, result)
    else:
        answer = start[0]

    print(f'#{tc} {answer}')
