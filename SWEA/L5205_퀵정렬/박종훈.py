import sys
sys.stdin = open('input.txt')


def quick_sort(array, s, e):
    if s >= e:
        return

    p = s
    l = s+1
    r = e

    while l <= r:
        while l <= r and array[l] <= array[p]:
            l += 1
        while l <= r and array[r] >= array[p]:
            r -= 1
        if l <= r:
            array[l], array[r] = array[r], array[l]
        else:
            array[p], array[r] = array[r], array[p]

    quick_sort(array, s, r-1)
    quick_sort(array, r+1, e)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    quick_sort(arr, 0, len(arr) - 1)
    result = arr[N//2]
    print(f'#{tc} {result}')
