import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    boxes = sorted(list(map(int, input().split())), reverse=True)
    trucks = sorted(list(map(int, input().split())), reverse=True)

    weight = 0
    for truck in trucks:
        for box in boxes:
            if truck >= box:
                weight += box
                boxes.remove(box)
                break
        else:
            break
    print(f'#{tc} {weight}')
