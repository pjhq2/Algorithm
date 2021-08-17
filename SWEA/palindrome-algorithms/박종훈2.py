import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):

    chars = input()

    if len(chars) % 2:  # 홀수일 때
        for i in range(len(chars)//2 + 1):  # 반띵 for문
            if chars[len(chars)//2 + i] == chars[len(chars)//2 - i]:
                continue
            else:
                print(False)
                break
        else:
            print(True)

    else:  # 짝수일 때
        if chars[len(chars)//2] == chars[len(chars)//2 - 1]:
            for i in range(len(chars) // 2):
                if chars[len(chars) // 2 + i] == chars[len(chars) // 2 - 1 - i]:
                    continue
                else:
                    print(False)
                    break
            else:
                print(True)
