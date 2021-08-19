import sys
sys.stdin = open('input.txt')

T = 10

for tc in range(1, T+1):
    N, temp = input().split()
    password = []
    for t in temp:
        password.append(t)

    i = 0
    while i < len(password)-1:
        if password[i] == password[i+1]:
            password.pop(i+1)
            password.pop(i)
            i = i-1
            continue
        i += 1

    result = ''
    for i in password:
        result += i
    print(f'#{tc} {result}')