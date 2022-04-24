import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


N = int(input())
arr = [[] for _ in range(200001)]       # 미리 x좌표 만큼의 배열 생성

for _ in range(N):
    x, y = map(int, input().split())
    arr[x+100000].append(y)             # 음수를 제거해주기 위해 음수 최대 범위 만큼을 더해줌

for i in range(200001):
    if len(arr[i])>0:
        for j in sorted(arr[i]):        # 해당 idx에 값이 존재하면 정렬해서 순차적으로 뽑아낸다.
            print(f'{i-100000} {j}')
