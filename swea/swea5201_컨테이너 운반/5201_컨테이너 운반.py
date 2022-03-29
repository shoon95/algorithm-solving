import sys
sys.stdin = open('input.txt')

def get_cnt(w, truck, cnt):
    idx = 0
    while truck:
        value = truck.pop()
        for i in w[idx:]:
            idx += 1
            if i <= value:
                cnt += i
                if idx == len(w):
                    return cnt
                break
    return cnt

T = int(input())

for tc in range(T):
    N, M = map(int, input().split())
    w = list(map(int, input().split()))
    truck = list(map(int, input().split()))
    if tc !=0:
        continue
    w.sort(reverse=True)
    truck.sort()
    print(w)
    print(truck)
    print(f'#{tc+1} {get_cnt(w, truck,0)}')

