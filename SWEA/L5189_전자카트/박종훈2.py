# 외판원 순회
import sys
sys.stdin = open('input.txt')

INF = int(1e9)


def func(current, visit):
    # 방문 종료
    if visit == (1 << N) - 1:  # 111 이라면
        return area[current][0]
    
    # 이미 방문
    if dp[current][visit] != INF:
        return dp[current][visit]
    
    for i in range(1, N):
        # 방문 안함
        if not visit & (1 << i):
            dp[current][visit] = min(dp[current][visit], func(i, visit|(1 << i)) + area[current][i])

    return dp[current][visit]


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    area = [list(map(int, input().split())) for _ in range(N)]
    dp = [[INF]*(1 << N) for _ in range(N)]  # N이 3이면 INF 8개 있는 리스트가 3개
    
    print(f'#{tc}', func(0, 1))
