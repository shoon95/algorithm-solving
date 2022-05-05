import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split())

dic = {}
for _ in range(N):                          # N 까지의 input을 key로 dictionary에 담음
    value = sys.stdin.readline().rstrip()
    dic[value] = 1

arr = []
for _ in range(M):                          # N+1:M 까지의 input이 dictionary의 key에 존재하면 arr에 추가
    value = sys.stdin.readline().rstrip()
    if value in dic.keys():
        arr.append(value)

arr.sort()                                  # arr를 정렬 후 개수와 value를 순차적으로 출력

print(len(arr))
for i in arr:
    print(i)