import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split())

arr = list(map(int,sys.stdin.readline().split()))

for i in range(1,len(arr)):
    arr[i] = arr[i-1] + arr[i]                              # 입력 받은 배열의 누적합을 구한다

for _ in range(M):
    start, end = map(int, sys.stdin.readline().split())
    if start == 1:                                          # 합을 구하는 구간이 1부터면 end-1을 idx로 하는 value가 누적합
        print(arr[end-1])
    else:
        print(arr[end-1] - arr[start-2])                    # 합을 구하는 구간의 시작이 1보다 크면 end-1을 idx로하는 value에서 start-2를 idx로 하는 value를 빼줌