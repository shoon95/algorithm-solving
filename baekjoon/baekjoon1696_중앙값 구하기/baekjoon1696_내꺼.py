import sys
sys.stdin = open('input.txt')

T = int(input())

for _ in range(T):

    size = int(input())
    print(size//2+1)

    arr = []
    for j in range(size//10+1):                     # 10개가 넘어가는 input 값 받기 (10개씩 잘라서)
        arr.extend(list(map(int,input().split())))

    value = []
    for i in range(0,size,2):                       # step을 2씩 주면서 배열의 해당 범위만 정렬 후 가운데 값 뽑기
        temp = sorted(arr[0:i+1])
        value.append(temp[i//2])

    for i in range(len(value)//10+1):               # 10개씩 끊어서 출력하기
        print(*value[i*10:i*10+10])
