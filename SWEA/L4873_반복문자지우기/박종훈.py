import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    temp = input()
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

    print(f'#{tc} {len(password)}')