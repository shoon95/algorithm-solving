import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())

rear = front = -1
Q = []
for _ in range(N):
    data = input()
    if 'push' in data:
        rear += 1
        Q.append(data.split()[1])
    elif 'front' in data:
        if front == rear:
            print(-1)
        else:
            print(Q[front+1])
    elif 'back' in data:
        if front == rear:
            print(-1)
        else:
            print(Q[rear])
    elif 'size' in data:
        print(rear-front)
    elif 'pop' in data:
        if front == rear:
            print(-1)
        else:
            print(Q[front+1])
            front += 1
    elif 'empty' in data:
        if front == rear:
            print(1)
        else:
            print(0)