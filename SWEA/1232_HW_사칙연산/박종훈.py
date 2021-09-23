import sys
sys.stdin = open('input.txt')


def solution(n):
    if type(tree[left[n]]) == str:
        tree[left[n]] = solution(left[n])
    if type(tree[right[n]]) == str:
        tree[right[n]] = solution(right[n])

    if type(tree[left[n]]) != str and type(tree[right[n]]) != str:
        if tree[n] == '+':
            tree[n] = tree[left[n]] + tree[right[n]]
        elif tree[n] == '-':
            tree[n] = tree[left[n]] - tree[right[n]]
        elif tree[n] == '*':
            tree[n] = tree[left[n]] * tree[right[n]]
        elif tree[n] == '/':
            tree[n] = tree[left[n]] / tree[right[n]]
        return tree[n]


T = 10
for tc in range(1, T+1):
    N = int(input())
    tree = [0] * (N+1)
    left = [0] * (N+1)  # 인덱스가 부모
    right = [0] * (N+1)

    for _ in range(1, N+1):
        line = input().split()
        if len(line) == 2:
            tree[int(line[0])] = int(line[1])
        if len(line) == 4:
            tree[int(line[0])] = line[1]
            left[int(line[0])] = int(line[2])
            right[int(line[0])] = int(line[3])

    solution(1)
    print(f'#{tc} {int(tree[1])}')
