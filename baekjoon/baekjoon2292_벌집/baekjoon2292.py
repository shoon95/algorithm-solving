N = int(input())
base = 1                # 시작값을 1로 설정
i = 0                   # i번 째의 최대 범위를 찾자
while True:
    base = base + 6*i   # i번의 최대 범위는 기존 base에서 6*현재 i의 수
    i += 1              # 다음 차례로 넘어갈 때 i를 +1 해준다
    if N <= base:       # 찾는 수 N이 최대 범위 base보다 작다면 스탑
        break

print(i)