# 01. 모험가 길드
N = int(input())
fears = list(map(int, input().split()))
fears.sort()
cnt = 0
result = 0
for i in fears:
    cnt += 1
    if i <= cnt:
        result += 1
        cnt = 0
print(result)