import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split())
arr = [input() for _ in range(N)]

check1 = ['BWBWBWBW','WBWBWBWB'] *4 # B부터 시작하는 2차원 배열 생성
check2 = ['WBWBWBWB','BWBWBWBW'] *4 # W부터 시작하는 2차원 배열 생성

mmin = 1000000000                   # 최소값을 구하기 위해 나올 수 없는 큰 수로 초기화

for i in range(0,N-7):
    for j in range(0,M-7):
        cnt1 = 0
        cnt2 = 0
        for p in range(8):
            for q in range(8):
                if list(map(lambda n:n[j:j+8],arr[i:i+8]))[p][q] != check1[p][q]: # 8x8배열을 순회하며 B 부터 시작하는 check1과 비교
                    cnt1+=1
                if list(map(lambda n:n[j:j+8],arr[i:i+8]))[p][q] !=check2[p][q]: # 8x8배열을 순회하며 W 부터 시작하는 check2와 비교
                    cnt2+=1
        mmin = min(cnt1,mmin,cnt2) # 가장 작은 값으로 갱신
print(mmin)