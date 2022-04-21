import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

def lower_search(value):            # 찾는 값보다 이상인 값이 처음 나타나는 곳을 찾는다.
    min = 0                         # left
    max = N                         # right (결국에는 min이 한 칸씩 max방향으로 딸려오면서 위치를 파악하니까 max의 범위는 N까지)
    while min < max:                # 값을 찾으면 max는 그 위치로 이동하고 min을 계속 당겨오면서 값이 처음 나타나는 곳을 찾는다.
        mid = (max+min)//2
        if arr_N[mid] >= value:     # 현재 값이 value보다 크거나 같으면 max값을 당겨옴 (제일 처음 위치로 점점 이동)
            max = mid
        else:
            min = mid+1             # 현재 값이 value보다 작으면 mid+1 위치로 min 값을 이동
    return min

def upper_search(value):            # 찾는 값을 초과하는 값이 처음 나타나는 곳을 찾는다.
    min = 0
    max = N
    while min < max:                # 값을 찾으면 min을 계속 당겨오면서 값을 초과하는 순간 max만 계속해서 당겨와진다. 결국 교차되는 순간 종료
        mid = (max+min)//2
        if arr_N[mid] <= value:
            min = mid+1
        else:
            max=mid
    return min

N = int(input())
arr_N = list(map(int,input().split()))
arr_N.sort()

M= int(input())
arr_M = list(map(int, input().split()))

for i in arr_M:
    print(upper_search(i)-lower_search(i), end=' ')
