# 05. 볼링공 고르기
N, M = list(map(int, input().split()))
K = list(map(int, input().split()))
K_set = list(set(K))
result = 0
for i in K_set:
    now = K.count(i) # 2
    for j in range(N-now, N-2*now, -1):
        result += N - now
answer = int(result / 2)
print(answer)