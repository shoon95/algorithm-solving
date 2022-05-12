import sys
sys.stdin = open('input.txt')

T = int(input())

for _ in range(T):
    N = int(input())
    arr = [0]*N
    arr[0:3] = [1,1,1]              # dp 배열 기저 조건 초기화

    for i in range(3,N):
        arr[i] = arr[i-3]+arr[i-2]  # 현재 idx의 값은 idx-3의 값 + idx-2
    print(arr[-1])                  # 순회 종료 후 제일 마지막 값 출력
