# 07. 럭키 스트레이트
N = input()
total1 = total2 = 0 # 변수 하나만 설정하고
for i in N[:len(N)//2]:
    total1 += int(i)
for i in N[len(N)//2:]:
    total2 += int(i) # 여기서 값을 빼면서
if total1 == total2: # 변수 == 0으로 확인할 수 있음
    print('LUCKY')
else:
    print('READY')