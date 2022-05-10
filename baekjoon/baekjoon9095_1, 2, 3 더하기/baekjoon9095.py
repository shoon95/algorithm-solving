import sys
sys.stdin = open('input.txt')

def get_combi(nums, N, arr):            # 중복 조합을 이용해 문제를 풀자
    global cnt                          # 조건을 만족할 때 cnt += 1
    if sum(arr) > N:                    # 현재 담긴 조합의 합이 N을 초과했다면 함수 종료
        return

    if sum(arr) == N:                   # 현재 담긴 조합의 합이 N과 같다면 cnt += 1 후 함수 종료
        cnt += 1
        return
    for i in nums:                      # [1,2,3] 배열에서 하나씩 중복해서 빼오면서 재귀 함수 호출
        get_combi(nums, N, arr+[i])


N = int(input())
nums = [1,2,3]
for _ in range(N):
    cnt = 0
    get_combi(nums, int(input()), [])
    print(cnt)


