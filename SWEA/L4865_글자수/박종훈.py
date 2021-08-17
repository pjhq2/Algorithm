import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):

    str1, str2 = input(), input()
    str_dict = {}

    for s1 in set(str1):
        for s2 in str2:
            if s1 == s2:
                if s1 in str_dict:
                    str_dict[s1] += 1
                else:
                    str_dict[s1] = 1

    result = 0
    for v in str_dict.values():
        if v > result:
            result = v

    print(f'#{tc} {result}')