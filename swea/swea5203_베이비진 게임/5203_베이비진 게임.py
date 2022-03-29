import sys
sys.stdin = open('input.txt')

T = int(input())

def check_run(player, i):
    if i == 0:
        if player[0] >0 and player[1] > 0 and player[2] > 0:
            return True
    elif i == 1:
        if player[0]> 0 and player[1] > 0 and player[2] > 0 or player[1] <0 and player[2] > 0 and player[3]>0:
            return True
    elif i == 9:
        if  player[9]> 0 and player[8] > 0 and player[7] > 0:
            return True
    elif i ==8:
        if player[9]> 0 and player[8] > 0 and player[7] > 0 or player[6]> 0 and player[8] > 0 and player[7] > 0:
            return True
    else:
        for j in range(i-2,i+1):
            if player[j]> 0 and player[j+1]>0 and player[j+2] >0:
                return True

def check_triplet(player,i):
    if player[i] >= 3:
        return True
    else:
        return False

for tc in range(T):
    arr = list(map(int,input().split()))

    player_1 = [0] * 10
    player_2 = [0] * 10
    for i in range(len(arr)):
        if i%2 == 0:
            player_1[arr[i]] += 1
            if check_triplet(player_1,arr[i]) or check_run(player_1,arr[i]):
                print(f'#{tc+1} {1}')
                break
        else:
            player_2[arr[i]] += 1
            if check_triplet(player_2,arr[i]) or check_run(player_2,arr[i]):
                print(f'#{tc+1} {2}')
                break
    else:
        print(f'#{tc + 1} {0}')