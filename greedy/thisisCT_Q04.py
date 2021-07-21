# 04. 만들 수 없는 금액
N = int(input())
money = list(map(int, input().split()))
money.sort()
# x-1원까지 만들 수 있을 때, x를 만들 수 있는가?
target = 1
for x in money:
    if target < x:
        break
    target += x
print(target)