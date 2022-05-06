import sys
sys.stdin = open('input.txt')

def get_result(N):
    global arr
    length = len(arr)

    for i in range(length):
        for j in range(i,length):
            for q in range(j, length):
                for p in range(q, length):
                    if i >= 1:                              # pointer 4개를 돌면서 i가 1보다 크면 더 확인할 필요 없이 4개가 필요
                        return 4
                    if arr[p]+arr[q]+arr[j]+arr[i] == N:    # pointer 4개의 합이 N과 같으면 해당 포인터 출력
                        return (p,q,j,i)

N = int(input())

arr = []
i = 0
while i**2<=N:                                              # N보다 큰 값이 나오기 전까지 i**2를 리스트에 추가
    arr.append(i**2)
    i+=1

result = get_result(N)

if result ==4 :
    print(4)
else:
    cnt = 0
    for i in result:
        if i != 0:
            cnt+=1
    print(cnt)