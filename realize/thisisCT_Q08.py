# 08. 문자열 재정렬 (Facebook 인터뷰)
S = input()
total = 0
result = []
for i in S:
    if 48 <= ord(i) <= 57: # 숫자
        total += int(i)
    elif 65 <= ord(i) <= 90: # 대문자 영어
        result.append(i)
result.sort()
if total != 0: # 숫자가 없을 경우도 생각
    result.append(str(total))
print(''.join(result))