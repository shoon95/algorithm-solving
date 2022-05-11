import sys
sys.stdin = open('input.txt')

def get_result(dic):
    global cnt

    for i in dic:                   # 각각 종류에서 1개 또는 0개를 고르는 경우의 수
        cnt *= len(dic[i])+1
    print(cnt-1)                    # 모든 종류의 옷을 0개씩 고른 경우를 제외

T = int(input())

for tc in range(T):

    N = int(input())

    dic = {}
    cnt = 1
    for _ in range(N):                  # 주어진 input 중 옷의 종류가 dictionary에 없으면 key에 추가, 있으면 해당 키에 value 추가
        value, idx = input().split()
        if idx in dic:
            dic[idx] += [value]
        else:
            dic[idx] = [value]
    get_result(dic)