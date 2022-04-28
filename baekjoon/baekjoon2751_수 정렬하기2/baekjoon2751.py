import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())

arr = [[] for _ in range(2000001)]  # 음수 최대 범위로 배열을 미리 생성
for _ in range(N):
    arr[int(input())+1000000] = 1   # 음수를 없애주기 위해 1000000을 더해줌

for i in range(2000001):            # 배열을 순회하면서 해당 idx에 값이 존재하면 idx 출력
    if arr[i]:
        print(i-1000000)            # idx-1000000 으로 출력