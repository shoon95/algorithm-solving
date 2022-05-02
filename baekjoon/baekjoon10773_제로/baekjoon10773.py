import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
N = int(input())
j = -1
arr = [[] for _ in range(100000)] # 미리 배열을 생성
for _ in range(N):
    value = int(input())
    if value:
        j += 1                    # 추가되면 pointer를 우측으로 이동시키고 value 추가
        arr[j] = value

    else:
        j -= 1                    # input이 0 이면 pointer를 좌측으로 이동

if j > -1:                        # pointer가 -1 이면 0, 그것보다 크면 포인터 +1 까지 더한 값 출력
    print(sum(arr[:j+1]))
else:
    print(0)