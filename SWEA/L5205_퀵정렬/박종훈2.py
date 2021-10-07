import sys
sys.stdin = open('input.txt')


def quick_sort(array):
    if len(array) <= 1:
        return array

    p = array[0]
    t = array[1:]

    left = [x for x in t if x <= p]
    right = [x for x in t if x > p]

    return quick_sort(left) + [p] + quick_sort(right)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    result = quick_sort(arr)[N // 2]
    print(f'#{tc} {result}')