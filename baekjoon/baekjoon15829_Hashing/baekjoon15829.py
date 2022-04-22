import sys
sys.stdin = open('input.txt')
N = int(input())
arr = input()
cnt = 0
for i in range(N):
    cnt += (ord(arr[i])-96) * (31**i)
print(cnt%1234567891)