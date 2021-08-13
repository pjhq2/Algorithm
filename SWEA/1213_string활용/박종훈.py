import sys
sys.stdin = open('input.txt', 'rt', encoding='UTF8')

T = 10

for _ in range(1, T+1):

    tc = int(input())
    target = input()
    chars = input()

    cnt = 0
    for i in range(len(chars)-len(target)+1):
        if chars[i:i+len(target)] == target:
            cnt += 1

    print(f'#{tc} {cnt}')
