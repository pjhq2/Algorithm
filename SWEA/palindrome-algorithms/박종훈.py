import sys
sys.stdin = open('input-long.txt')


T = int(input())

for tc in range(1, T+1):

    chars = input()
    if chars == chars[::-1]:
        print(True)
    else:
        print(False)
