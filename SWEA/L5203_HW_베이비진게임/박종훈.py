import sys
sys.stdin = open('input.txt')


def is_baby_gin(player, card):
    # triplet
    if player[card] >= 3:
        return True
    # run
    if card >= 2:
        if (player[card-2] >= 1 and player[card-1] >= 1) or (player[card-1] >= 1 and player[card+1] >= 1) or (player[card+1] >= 1 and player[card+2] >= 1):
            return True
    elif card == 1:
        if (player[card-1] >= 1 and player[card+1] >= 1) or (player[card+1] >= 1 and player[card+2] >= 1):
            return True
    elif card == 0:
        if (player[card+1] >= 1 and player[card+2] >= 1):
            return True
    # nothing
    return False


T = int(input())
for tc in range(1, T+1):
    player = [[0] * 12 for _ in range(3)]
    for idx, card in enumerate(list(map(int, input().split()))):
        n = idx % 2 + 1
        player[n][card] += 1
        if is_baby_gin(player[n], card):
            print(f'#{tc} {n}')
            break
    else:
        print(f'#{tc} 0')
