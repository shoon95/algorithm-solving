import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

def bi_search(value):               # 이진 탐색
    min = 0                         # 시작 idx
    max = N-1                       # 마지막 idx
    while min <= max:               # min 값이 max 를 초과하면 stop
        mid = (max + min) // 2      # mid 는 max+min을 2로 나눈 값
        if arr_N[mid] > value:      # 찾는 값이 배열의 중간 값보다 작다면 max의 값을 mid-1로 끌어옴
            max = mid-1
        elif arr_N[mid] < value:    # 찾는 값이 배열의 중간 값보다 크다면 min의 값을 mid+1로 끌어옴
            min = mid+1
        else:
            return 1                # 값을 찾았다면 1을 반환
    return 0                        # 값을 못찾았다면 0을 반환



N = int(input())
arr_N = list(map(int, input().split()))
arr_N.sort()

M = int(input())
arr_M = list(map(int, input().split()))

for i in arr_M:
    print(bi_search(i))