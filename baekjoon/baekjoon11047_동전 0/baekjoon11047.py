import sys
sys.stdin = open('input.txt')

N, M = map(int,input().split())

arr = []
for _ in range(N):
    value = int(sys.stdin.readline().rstrip())
    if M >= value:                              # 동전의 값이 M보다 같거나 작으면 배열에 담기
        arr = [value] + arr                     # 큰 동전이 앞으로 오도록 배열을 뒤집어서 받아준다.

cnt = 0
for i in arr:                                   # 배열을 순회
    cnt += M//i                                 # 동전으로 나눈 몫이 해당 동전을 내는 수
    M %= i                                      # 동전으로 나눈 나머지가 남은 동전들로 내야되는 남은 값
print(cnt)                                      # 모든 동전을 내는 수를 더해서 출력