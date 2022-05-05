import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split())

dic = {}
for _ in range(N):
    key, value = sys.stdin.readline().rstrip().split()  # input을 key 로 dictionary 생성
    dic[key] = value

for _ in range(M):
    print(dic[sys.stdin.readline().rstrip()])