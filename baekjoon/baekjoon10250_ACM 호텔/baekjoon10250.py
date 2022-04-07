import sys
sys.stdin = open('input.txt')
T = int(input())

for tc in range(T):
    H, W, N = map(int, input().split())

    h=str(N%H)                              # 높이는 사람 수를 높이로 나눈 나머지

    w=str(N//H+1)                           # 가로 번호는 사람 수를 높이로 나눈 몫 +1
    if h=='0':                              # 만약 높이로 사람 수를 나누었을 떄 나머지가 0이면
        h = str(H)                          # 높이는 주어진 높이
        w = str(int(w)-1)                   # 방 수는 사람 수를 높이로 나눈 몫
    if len(w)==1:
        print(f'{str(h)+str(0)+str(w)}')
    else:
        print(f'{str(h) + str(w)}')