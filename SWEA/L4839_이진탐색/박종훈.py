import sys
sys.stdin = open('input.txt')

INF = int(1e9)
T = int(input())


def binary_search(book, target_page, start, end):
    if start > end:
        return INF
    else:
        cnt = 1
        while start <= end:
            mid = int((start + end) / 2)
            if book[mid-1] == target_page:
                return cnt
            elif book[mid+1] > target_page:
                end = book[mid-1] - 1
            else:
                start = book[mid-1] + 1
            cnt += 1
        return cnt


for tc in range(1, T+1):

    page, target_page_A, target_page_B = list(map(int, input().split()))
    book = list(range(1, page+1))
    A = binary_search(book, target_page_A, 1, page)
    B = binary_search(book, target_page_B, 1, page)

    result = 'A' if A < B else 'B' if A > B else 0

    print(f'#{tc} {result}')
