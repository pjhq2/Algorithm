# 02. 곱하기 혹은 더하기
# 0, 1만 주의, 나머지는 다 곱하기
S = input()
result = 0
for s in S:
    if result <= 1:
        result += int(s)
    else:
        if int(s) > 1:
            result *= int(s)
        else:
            result += int(s)
print(result)