import sys
sys.stdin = open('input.txt')

T = int(input())
for _ in range(T):
    N, idx = map(int, sys.stdin.readline().rstrip().split())
    arr = list(map(int, sys.stdin.readline().rstrip().split()))

    i = 0
    while True:
        if idx == 0:                        # 원하는 값의 idx가 0일 때
            if arr[0] != max(arr):          # 값이 최대가 아니면 맨 뒤로 보내고 idx를 제일 마지막으로 갱신
                arr.append(arr.pop(0))
                idx = len(arr) - 1
            else:                           # 만약 원하는 값이 최대값이면 횟수를 카운팅하고 종료
                i += 1
                break
        else:                               # 원하는 값의 idx가 0이 아닐 때는
            idx -= 1                        # idx를 하나 앞으로 당겨주고
            if arr[0] != max(arr):          # 제일 앞의 수가 최대값이 아니면
                arr.append(arr.pop(0))      # 빼서 제일 뒤로 보내줌
            else:                           # 제일 앞의 수가 최대값이면 빼고 횟수를 카운팅
                arr.pop(0)
                i += 1
    print(i)                                # 원하는 수가 pop됐을 때 현재까지 몇 번의 출력이 있었는데 카운팅한 값을 출력