import sys
sys.stdin = open('input.txt')

N, M = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()


def find(N):
    mmin = 0
    for i in range(N-2):
        for j in range(i+1,N-1):
            for p in range(j+1,N):
                if arr[i]+arr[j]+arr[p]<=M:
                    mmin=max(mmin,arr[i]+arr[j]+arr[p])
                else:
                    mmin = min(mmin, arr[i] + arr[j] + arr[p])
    return mmin
print(find(N))