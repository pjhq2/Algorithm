import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):

    corridor = [0] * 201  # 복도
    N = int(input())
    for _ in range(N):
        start, end = map(int, input().split())
        start = start//2 if start % 2 else start//2 - 1
        end = end//2 if end % 2 else end//2 - 1

        if start < end:  # 작은 번호 -> 큰 번호일 때
            for i in range(start, end+1):
                corridor[i] += 1
        else:  # 큰 번호 -> 작은 번호일 때
            for i in range(end, start+1):
                corridor[i] += 1

    print(f'#{tc} {max(corridor)}')
