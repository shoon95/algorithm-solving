import sys
sys.stdin = open('input.txt')

N, M, B = map(int, input().split())

arr = [list(map(int,sys.stdin.readline().strip().split())) for _ in range(N)]
temp = [0] * 257                # 2차원 배열인 input을 1차원 배열로 변환해주기 위해 1차원 배열 초기화

mmin = 257                      # input의 최소값 받아오기
mmax = 0                        # input의 최대값 받아오기

for i in range(N):
    for j in range(M):
        temp[arr[i][j]] += 1    # temp 배열에 input의 값을 idx로 해서 value를 +1
        if arr[i][j] > mmax:
            mmax = arr[i][j]
        if arr[i][j] < mmin:
            mmin = arr[i][j]


result = 1000000000              # 나올 수 없는 높은 시간으로 result 초기화
height = -1                      # 나올 수 없는 낮은 높이로 height 초기화

for num in range(mmin, mmax+1):
    cnt = 0
    cnt_B = B
    for i in range(257):
        if cnt > result:
            continue

        if i > num:
            cnt += (i-num)*temp[i]*2            # idx가 num 보다 크면 블록을 빼주고 해당 idx의 value의 크기만큼 곱하고 다시 *2 해서 시간을 구해줌
            cnt_B += (i - num)*temp[i]          # 위와 같이 인벤토리 블록 수를 추가
        elif i < num:
            cnt_B -= (num - i) * temp[i]        # idx가 num 보다 작으면 블록을 빼주고 해당 idx의 value의 크기만큼 곱해서 인벤토리 블록 수를 빼줌
            cnt += (num - i) * temp[i]          # 위와 같이 계산해서 걸리는 시간을 더해줌

    if cnt_B < 0:                               # 위 작업이 다 끝났을 때 인벤토리 블록 수가 - 라면 더이상 진행하지 않고 다음으로 순회로 넘어감
        continue
    else:
        if cnt < result:                        # 걸린 시간이 기존보다 적게 걸렸다면 높이와 시간을 새로 갱신해줌
            height = num
            result = cnt
        elif cnt == result and num > height:    # 걸린 시간이 같고 높이는 더 높다면 높이만 새로 갱신해줌
            height = num
print(result, height)