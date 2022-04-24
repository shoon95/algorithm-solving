N = int(input())

arr = list(range(1,N+1))
                            # 시간 초과 해결을 위해 pointer 사용
rear = N-1                  # 값의 마지막 부분
front = 0                   # 값의 시작 부분
while rear!=front:          # front가 rear를 따라잡으면 종료
    front += 1              # front +=1 (처음 원소의 삭제를 의미)
    arr.append(arr[front])  # front가 가리키는 값을 배열의 맨 뒤에 추가(리스트의 맨뒤에 추가하는 경우 시간 복잡도는 굉장히 낮다(O(1))
    rear+=1                 # 배열의 크기가 늘어났으니 rear도 그만큼 한칸 후퇴
    front += 1              # 뒤로 보낸 위치는 다시 취급하지 않기 위해 front를 1만큼 전진
print(arr[-1])