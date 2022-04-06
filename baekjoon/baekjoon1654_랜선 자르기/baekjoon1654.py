import sys
sys.stdin = open('input.txt')

K, N = map(int,input().split())

arr = [int(input()) for _ in range(K)]

start = 1
end = max(arr)

while start <= end:                                 # start가 end를 넘어서면 종료
    mid = (start + end) // 2                        # 가운데를 중심으로 양쪽 탐색
    if sum(list(map(lambda n:n//mid, arr))) >= N:   # 주어진 N과 값이 같거나 크면 start를 mind+1로 당겨옴
        start = mid+1
    else:                                           # 그렇지 않다면 마지막 지점을 당겨옴
        end = mid-1
        mid = (start+end)//2
print(mid)