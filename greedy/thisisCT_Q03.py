# 03. 문자열 뒤집기
# 0만 다 뒤집어보고, 1만 다 뒤집어본 뒤 비교
S = input()
check = S[0]
cnt0 = 0
cnt1 = 0
for s in S[1:]:
    if check == '0':
        if check != s:
            cnt0 += 1
        check = s # 0을 1로 뒤집음
    if check == '1':
        if check != s:
            cnt1 += 1
        check = s # 1을 0으로 뒤집음
print(min(cnt0, cnt1))