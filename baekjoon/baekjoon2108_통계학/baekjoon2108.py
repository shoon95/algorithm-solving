import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())

arr = [0]*8001              # 주어진 input의 갯수를 담을 리스트 생성 ( input이 음수도 존재함으로 4000 더해줘서 음수를 양수 범위로 바꾸어줌)
data =[]                    # 주어진 input의 값을 담은 빈리스트 생성
result = [0] * N            # 정렬된 값을 담을 리스트 생성

for _ in range(N):
    value=int(input())
    arr[value+4000]+= 1     # input의 갯수 카운팅
    data.append(value)

mmax=max(arr)
temp=[]
for i in range(len(arr)):   # 최댓값의 idx 구하기
    if arr[i]==mmax:
        temp.append(i)

for i in range(len(arr)-1):     # 누적합 구하기
    arr[i+1] = arr[i]+arr[i+1]

for i in data:                  # 카운팅 정렬
    result[arr[i+4000]-1]=i
    arr[i+4000]-=1

def solv_1():
    return round(sum(result)/N)

def solv_2():
    return result[N//2]

def solv_3():
    if len(temp) == 1:
        return temp[0]-4000
    else:
        return temp[1]-4000

def solv_4():
    return result[N-1]-result[0]

print(solv_1())
print(solv_2())
print(solv_3())
print(solv_4())