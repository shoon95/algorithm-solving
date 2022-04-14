N = int(input())
start = N
result = []
while N!=0:
    N -= 1
    cnt = 0
    for i in str(N):
        cnt+= int(i)
    if cnt+N == start:
        result.append(N)
if len(result) > 0:
    print(result[-1])
else:
    print(0)
